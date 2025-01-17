import sys

OPCODES = {
    "mov": 0,
    "movi": 1,
    "addi": 2,
    "muli": 3,
    "add": 4,
    "mul": 5,
    "mmovf": 6,
    "mstore": 7,
    "jz": 8,
    "jnz": 9,
    "cmp": 10,
    "cmpi": 11,
    "xor": 12,
    "and": 13,
    "or": 14,
    "jmp": 15,
    "halt": 16
}

def assemble(input_file, output_file):
    with open(input_file, "r") as f:
        lines = [l.strip() for l in f if l.strip()]

    # First pass: collect labels
    labels = {}
    instr_count = 0
    for line in lines:
        if line.startswith(".label"):
            label = line.split()[1]
            labels[label] = instr_count
        else:
            # skip comments and empty lines
            if not line.startswith(";") and not line.startswith("\n"):
                instr_count += 1

    # Second pass: generate bytecode
    bytecode = []
    current_instr = 0
    for line in lines:
        if line.startswith(".label"):
            continue

        parts = line.split()
        cmd = parts[0]
        if cmd not in OPCODES:
            if cmd ==";":
                continue
            raise ValueError(f"Unknown instruction: {cmd}")

        op = OPCODES[cmd]
        if cmd in ["halt"]:
            bytecode.extend([op, 0, 0])
        elif cmd in ["jmp", "jz", "jnz"]:
            # offset to label
            label = parts[1]
            offset = labels[label] - (current_instr + 1)
            bytecode.extend([op, (offset>>8)&0xFF, offset&0xFF])
        elif cmd in ["mov", "add", "mul", "mmovf", "mstore", "xor", "and", "or", "cmp"]:
            r1 = int(parts[1].replace("r","").replace(",", ""))
            r2 = int(parts[2].replace("r","").replace(",", ""))
            bytecode.extend([op, r1 & 0xFF, r2 & 0xFF])
        elif cmd in ["movi", "addi", "muli", "cmpi"]:
            r1 = int(parts[1].replace("r","").replace(",", ""))
            imm = parts[2].replace("#","")
            if imm.startswith("0x"):
                imm = int(imm[2:], 16)
            else:
                imm = int(imm)
            bytecode.extend([op, r1 & 0xFF, imm & 0xFF])
        else:
            raise ValueError(f"Cannot encode: {line}")

        current_instr += 1

    with open(output_file, "wb") as out:
        out.write(bytes(bytecode))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python assembler.py <input_file> <output_file>")
    else:
        assemble(sys.argv[1], sys.argv[2])