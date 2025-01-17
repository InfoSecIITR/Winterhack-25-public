FLAG="winterhack{h0w_d!d_you_3v3n_puLL_th1s_0ff!!}"
print(len(FLAG))
a=0xdeadbeef
b=0xcafebabe
key="never_gonna_give_you_up_never_gonna_let_you_down_never_gonna_run_around_and_desert_you"
def encrypt(flag):
    enc_flag=[]
    for i in range(len(flag)):
        k=ord(key[i])*b
        k-=a
        enc_flag.append((ord(flag[i])^(k&0xffffffff))&0xff)
    return enc_flag

enc_flag=encrypt(FLAG)
print(enc_flag)
enc_flag_str=''.join([chr(i&0xff) for i in enc_flag])
flag=''.join([chr(enc_flag[i]^((ord(key[i])*b-a)&0xff)) for i in range(len(enc_flag))])
print(flag)
assert(flag==FLAG)
for i in range(len(key)):
    print(hex(ord(key[i])),end=',')
