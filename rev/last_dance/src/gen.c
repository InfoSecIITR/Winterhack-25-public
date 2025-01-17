#include <stdio.h>
#include <stdint.h>
char flag[] = "winterhack{1_347_z3_1n_br34kf457_4nd_PTRACE_1n_d1nn3r}";
static void
dance(long rdi, long rsi, long rdx, long rcx)
{
    char dance[] = "dancedancedancedancedancedancedanc";
    char c = flag[rdi];
    *(dance + (c >> 3)) ^= (1 << (c % 8));
    dance[32] ^= (rdi);
    c = flag[rsi];
    *(dance + (c >> 3)) ^= (1 << (c % 8));
    dance[33] ^= (rsi);
    for (int i = 0; i < 34; i++)
    {
        printf("0x%x, ", (unsigned char)dance[i] ^ (unsigned char)rdx);
    }
    printf("\n");

    return;
}
static void salsa(long rdi, long rsi, long rdx, long rcx)
{
    char salsa[] = "salsasalsasalsasalsasalsasalsasals";
    char c = flag[rdi];
    *(salsa + (c >> 3)) ^= (1 << (c % 8));
    salsa[32] ^= (rdi);
    c = flag[rsi];
    *(salsa + (c >> 3)) ^= (1 << (c % 8));
    salsa[33] ^= (rsi);
    for (int i = 0; i < 34; i++)
    {
        printf("0x%x, ", (unsigned char)salsa[i] ^ (unsigned char)rdx);
    }
    printf("\n");

    return;
}
static void chacha(long rdi, long rsi, long rdx, long rcx)
{
    char chacha[] = "chachachachachachachachachachachac";
    char c = flag[rdi];
    *(chacha + (c >> 3)) ^= (1 << (c % 8));
    chacha[32] ^= (rdi);
    c = flag[rsi];
    *(chacha + (c >> 3)) ^= (1 << (c % 8));
    chacha[33] ^= (rsi);
    int ret = 1;
    for (int i = 0; i < 34; i++)
    {
        printf("0x%x, ", (unsigned char)chacha[i] ^ (unsigned char)rdx);
    }
    printf("\n");
    return;
}
typedef struct
{
    long rdi;
    long rsi;
    long rdx;
    long rcx;
} state;
int main()
{
    // unsigned char c = ((flag[17] + flag[22] * flag[23] + flag[24]) % 256);
    // printf("flag: 0x%x\n", c);
    dance(17, 22, 23, 0);
    salsa(10, 11, 12, 1);
    chacha(42, 15, 29, 2);
    dance(7, 31, 50, 3);
    salsa(26, 53, 145, 4);
    chacha(19, 48, 28, 5);
    dance(3, 38, 124, 6);
    salsa(14, 55, 209, 7);
    chacha(29, 44, 78, 8);
    dance(8, 37, 89, 9);
    salsa(0, 51, 37, 10);
    chacha(16, 47, 53, 11);
    dance(33, 4, 69, 12);
    salsa(21, 46, 40, 13);
    chacha(9, 36, 123, 14);
    dance(2, 49, 108, 15);
    salsa(27, 41, 99, 16);
    chacha(6, 35, 27, 17);
    dance(32, 54, 57, 18);
    salsa(1, 43, 19, 19);
    chacha(20, 52, 91, 20);
    dance(5, 39, 178, 21);
    salsa(28, 45, 35, 22);
    chacha(18, 40, 87, 23);
    dance(30, 50, 10, 24);
    salsa(25, 34, 38, 25);
    chacha(12, 23, 24, 26);
    dance(13, 24, 94, 27);
    state states[] = {
        {17, 22, 23, 0},
        {10, 11, 12, 1},
        {42, 15, 29, 2},
        {7, 31, 50, 3},
        {26, 53, 145, 4},
        {19, 48, 28, 5},
        {3, 38, 124, 6},
        {14, 55, 209, 7},
        {29, 44, 78, 8},
        {8, 37, 89, 9},
        {0, 51, 37, 10},
        {16, 47, 53, 11},
        {33, 4, 69, 12},
        {21, 46, 40, 13},
        {9, 36, 123, 14},
        {2, 49, 108, 15},
        {27, 41, 99, 16},
        {6, 35, 27, 17},
        {32, 54, 57, 18},
        {1, 43, 19, 19},
        {20, 52, 91, 20},
        {5, 39, 178, 21},
        {28, 45, 35, 22},
        {18, 40, 87, 23},
        {30, 50, 10, 24},
        {25, 34, 38, 25},
        {12, 23, 24, 26},
        {13, 24, 94, 27}};
    return 0;
}