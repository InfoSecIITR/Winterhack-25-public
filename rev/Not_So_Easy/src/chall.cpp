#include <iostream>
#include <iomanip>
#include <queue>
#include <unordered_map>
#include <vector>
#include <memory>
#include <cstring>
#include <cstdlib>
#include <bitset>
#include <unistd.h>
#include <fcntl.h>
#include <sstream>
#include <openssl/evp.h> // red herring >:)
#include <openssl/err.h>

const char PROGRAM_KEY[] = "aint no party like diddy party";
const size_t PROGRAM_KEY_LEN = sizeof(PROGRAM_KEY) - 1;
size_t PROGRAM_KEY_INDEX = 0;

std::string obfuscate_str(const char* input, size_t len) {
    std::string output;
    output.reserve(len);
    for (size_t i = 0; i < len; i++) {
        output += input[i] ^ PROGRAM_KEY[PROGRAM_KEY_INDEX];
        PROGRAM_KEY_INDEX = (PROGRAM_KEY_INDEX + 1) % PROGRAM_KEY_LEN;
    }
    return output;
}

std::string bin_to_hex_str(const std::string& binary) {
    static const char hex_digits[] = "0123456789abcdef";
    std::string result;
    size_t padding = (4 - (binary.size() % 4)) % 4;
    std::string padded = std::string(padding, '0') + binary;
    result.reserve(padded.size() / 4);
    for (size_t i = 0; i < padded.size(); i += 4)
        result.push_back(hex_digits[((padded[i] - '0') << 3) | ((padded[i + 1] - '0') << 2) | ((padded[i + 2] - '0') << 1) | (padded[i + 3] - '0')]);
    return result;
}

class Huffman {
    struct Node {
        char ch;
        int freq;
        std::shared_ptr<Node> left, right;
        Node(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
    };

    struct CompareNodes {
        inline bool operator()(const std::shared_ptr<Node>& a, const std::shared_ptr<Node>& b) const {
            return a->freq > b->freq;
        }
    };

    std::shared_ptr<Node> root;
    std::unordered_map<char, std::vector<bool>> codes;

    void gen_codes(std::shared_ptr<Node> node, std::vector<bool> code = {}) {
        if (!node) return;
        if (!node->left && !node->right) codes[node->ch] = code;
        code.emplace_back(false);
        gen_codes(node->left, code);
        code.back() = true;
        gen_codes(node->right, code);
        code.pop_back();
    }

public:
    std::pair<std::string, std::unordered_map<char, std::vector<bool>>> encode(const std::string& text) {
        std::unordered_map<char, int> freq;
        for (char c : text) freq[c]++;

        std::priority_queue<std::shared_ptr<Node>, std::vector<std::shared_ptr<Node>>, CompareNodes> pq;
        for (const auto& [ch, f] : freq) {
            pq.push(std::make_shared<Node>(ch, f));
        }

        while (pq.size() > 1) {
            auto left = pq.top(); pq.pop();
            auto right = pq.top(); pq.pop();
            auto parent = std::make_shared<Node>('\0', left->freq + right->freq);
            parent->left = left;
            parent->right = right;
            pq.push(parent);
        }

        root = pq.top();
        gen_codes(root);

        std::string encoded;
        for (char c : text) {
            for (bool bit : codes[c]) {
                encoded += (bit ? '1' : '0');
            }
        }
        return { encoded, codes };
    }

    // std::string decode(const std::string& encoded, const std::unordered_map<char, std::vector<bool>>& codes) {
    //     std::unordered_map<std::vector<bool>, char> reverseMap;
    //     for (const auto& [ch, code] : codes) {
    //         reverseMap[code] = ch;
    //     }

    //     std::string decoded;
    //     std::vector<bool> current;
    //     for (char bit : encoded) {
    //         current.emplace_back(bit == '1');
    //         if (reverseMap.count(current)) {
    //             decoded += reverseMap[current];
    //             current.clear();
    //         }
    //     }
    //     return decoded;
    // }
};

// obvious red herring
int get_flag() {
    static constexpr unsigned char key[] = "\x02\x88\xf0\x27\x83\xc4\xa3\x22\x8c\xd9\xc2\x8d\x3a\x17\x42\x70";
    static constexpr unsigned char iv[] = "\xd1\x4a\xd8\x26\x75\x48\x18\x27\x74\xbd\xc9\x16\xe1\xf9\x74\xeb";

    // unsigned char flag[] = "winterhack{https://youtu.be/uJlqghMxLLU}"; // GYATT 4 GYATT
    static constexpr unsigned char enc_flag[] = "\x21\x33\xe3\x9c\x3b\x07\x90\xe3\x12\x79\xb9\xe7\x08\xbd\xb4\xef\x40\x27\xce\x7d\x5e\xd2\x08\x3d\xd0\x05\xf9\x0e\xaf\x6f\xf3\x99\x95\xbb\x1d\x45\xd6\xb1\x7f\x1d\xc7\xe7\x99\xd5\xf2\x43\x11\x76";
    // unsigned char enc_flag[64];

    int len;
    // int ptlen = 0;
    unsigned char flag[48];

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    // EVP_DecryptInit(ctx, EVP_aes_128_cbc(), key, iv);

    EVP_DecryptInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv);

    EVP_DecryptUpdate(ctx, flag, &len, enc_flag, sizeof(enc_flag));

    // ptlen += len;

    EVP_DecryptFinal_ex(ctx, flag + len, &len);

    EVP_CIPHER_CTX_free(ctx);

    // printf("ptlen: %d\n", ptlen);
    // printf("flag: ");
    // puts((char*)flag);
    // printf("\n");

    return !!flag[0];
}


int main(void) {
    int p2c[2]; // parent -> child
    int c2p[2]; // child -> parent

    pipe(p2c);
    pipe(c2p);


    if (fork()) {
        // parent

        close(p2c[0]);
        close(c2p[1]);

        char buffer[2048];

        int nbytes = read(c2p[0], buffer, sizeof(buffer));
        if (nbytes > 0) {
            buffer[nbytes] = 0;
        }

        std::string data = obfuscate_str(buffer, nbytes);

        Huffman h;

        auto [encoded, codes] = h.encode(data);

        std::stringstream ss;
        ss << "encrypted: " << bin_to_hex_str(encoded);

        ss << "00000000";

        std::unordered_map<char, int> freq;
        for (char c : data) freq[c]++;

        for (const auto& [ch, f] : freq) {
            ss << std::setw(2) << std::setfill('0') << std::hex << (int)ch;
            ss << std::setw(2) << std::setfill('0') << std::hex << f;
        }

        memcpy(buffer, ss.str().c_str(), ss.str().size());

        write(p2c[1], buffer, ss.str().size());

        close(p2c[1]);
        close(c2p[0]);

    }
    else {
        // child

        close(p2c[1]);
        close(c2p[0]);

        std::cout << "input: ";
        std::string input;
        std::getline(std::cin, input);

        write(c2p[1], input.c_str(), input.size());

        char buffer[2048];

        int nbytes = read(p2c[0], buffer, sizeof(buffer));
        if (nbytes > 0) {
            buffer[nbytes] = 0;
            std::cout << buffer << std::endl;
        }

        // std::cout << "received " << nbytes << " bytes" << std::endl;

        close(p2c[0]);
        close(c2p[1]);
    }

    return(0);
}
