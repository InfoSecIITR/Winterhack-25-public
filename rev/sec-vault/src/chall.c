#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <fcntl.h>


bool __attribute__((noinline)) verify_key(char* ckey, size_t len) {
    char key[len];
    memcpy(key, ckey, len);
    int valid = 1;

    valid &= (len < 60);
    valid &= (len >= 52);
    if (!valid) return 0;

    valid &= ((key[0] + (key[1] ^ key[3]))==110);
    valid &= ((key[2] + (key[1] ^ key[5]))==139);
    valid &= (((key[7] ^ key[4]) + key[3])==119);
    valid &= ((key[8] + key[3] + key[6])==322);
    valid &= ((key[8] + (key[3] ^ key[5]))==221);
    valid &= ((key[11] + (key[9] ^ key[8]))==188);
    valid &= ((key[10] ^ key[9] ^ key[7])==56);
    valid &= (((key[12] ^ key[10]) + key[5])==62);
    valid &= (((key[3] ^ key[13]) + key[14])==160);
    valid &= (((key[13] ^ key[15]) + key[14])==160);
    valid &= (((key[15] ^ key[12]) + key[0])==95);
    valid &= (((key[0] | key[16]) + key[19])==178);
    valid &= (((key[14] ^ key[16]) + key[12])==207);
    valid &= ((key[16] ^ key[17] ^ key[19])==110);
    valid &= ((key[19] + (key[17] ^ key[12]))==122);
    valid &= ((key[20] + (key[7] ^ key[20]))==140);
    valid &= ((key[6] - (key[21] ^ key[20]))==7);
    valid &= (((key[3] ^ key[8]) + key[21])==98);
    valid &= (((key[22] ^ key[21]) + key[21])==141);
    valid &= (((key[23] | key[29]) + key[17])==167);
    valid &= (((key[6] ^ key[13]) + key[24])==113);
    valid &= ((key[23] + key[12] + key[24])==279);
    valid &= ((key[21] + (key[17] ^ key[24]))==49);
    valid &= ((key[29] ^ key[16] ^ key[17])==106);
    valid &= (((key[17] & key[16]) ^ key[1])==72);
    valid &= (((key[25] & key[14]) ^ key[8])==94);
    valid &= ((key[0] + (key[1] ^ key[26]))==150);
    valid &= ((key[26] + key[1] + key[29])==214);
    valid &= (((key[49] ^ key[50]) + key[51])==200);
    valid &= (((key[49] ^ key[29]) + key[17])==139);
    valid &= (((key[3] ^ key[4]) + key[30])==148);
    valid &= ((key[25] ^ key[14] ^ key[38])==116);
    valid &= ((key[27] ^ key[14] ^ key[28])==111);
    valid &= ((key[23] + key[28] + key[26])==277);
    valid &= ((key[27] + key[29] + key[32])==211);
    valid &= ((key[30] + (key[28] ^ key[32]))==101);
    valid &= ((key[41] ^ key[29] ^ key[31])==114);
    valid &= (((key[18] ^ key[33]) + key[31])==125);
    valid &= ((key[34] + key[33] - key[29])==107);
    valid &= (((key[36] ^ key[34]) + key[34])==199);
    valid &= (((key[36] | key[34]) - key[35])==32);
    valid &= (((key[36] & key[29]) + key[37])==159);
    valid &= ((key[32] + key[39] + key[35])==294);
    valid &= ((key[32] + (key[30] | key[35]))==199);
    valid &= ((key[38] - key[37] + key[31])==2);
    valid &= ((key[43] ^ key[19] ^ key[42])==52);
    valid &= ((key[22] | key[29] | key[51])==127);
    valid &= (((key[23] ^ key[25]) + key[48])==97);
    valid &= ((key[14] + (key[24] ^ key[42]))==56);
    valid &= ((key[43] ^ key[27] ^ key[42])==51);
    valid &= (((key[41] ^ key[44]) + key[45])==188);
    valid &= (((key[42] ^ key[43]) + key[44])==60);
    valid &= ((key[44] + key[45] - key[42])==119);
    valid &= (((key[25] ^ key[39]) + key[46])==159);
    valid &= (((key[44] | key[37]) + key[48])==220);
    valid &= ((key[40] ^ (key[41] & key[42]))==5);
    valid &= (((key[22] ^ key[40]) + key[40])==145);
    valid &= (((key[16] | key[47]) ^ key[47])==76);
    valid &= (((key[47] | key[46]) + key[47])==166);
    valid &= ((key[49] + key[50] - key[51])==48);

    return !!valid;
}


void __attribute__((noinline)) reveal_treasure(char *s) {
    puts("                _.--.");
    puts("            _.-'_:-'||");
    puts("        _.-'_.-::::'||");
    puts("    _.-:'_.-::::::'  ||");
    printf("    .'`-.-:::::::'     ||      winterhack{%s}\n", s);
    puts("/.'`;|:::::::'      ||_");
    puts("||   ||::::::'     _.;._'-._");
    puts("||   ||:::::'  _.-!oo @.!-._'-.");
    puts("\\'.  ||:::::.-!()oo @!()@.-'_.|");
    puts("'.'-;|:.-'.&$@.& ()$%%-'o.'\\U||");
    puts("    `>'-.!@%%()@'@_%%-'_.-o _.|'||");
    puts("    ||-._'-.@.-'_.-' _.-o  |'||");
    puts("    ||=[ '-._.-\\U/.-'    o |'||");
    puts("    || '-.]=|| |'|      o  |'||");
    puts("    ||      || |'|        _| ';");
    puts("    ||      || |'|    _.-'_.-'");
    puts("    |'-._   || |'|_.-'_.-'");
    puts("    '-._'-.|| |' `_.-'");
    puts("        '-.||_/.-'");
}

int main(int argc, char** argv) {
    const char fake_key[] = "1_5w34r_70_60d_1f_7h15_15_7h3_c0rr3c7_k3y.._700_345y_>_>";

    puts("=================================================================================");
    puts("|                            Welcome to Sec-Vault                               |");
    puts("| There is some treasure hidden in this vault! (rumour has it that it's a flag!)|");
    puts("|            As all (safe) vaults, this one is also locked with a key.          |");
    puts("|            Find the key to the valut and the treasure is yours!               |");
    puts("=================================================================================");

    char key[72];
    printf("> ");
    fgets(key, 72, stdin);
    key[strcspn(key, "\n")] = 0;

    if (verify_key(key, strlen(key)) || strncmp(key, fake_key, 56) == 0) {
        puts("Here's your treasure: ");
        reveal_treasure(key);
    }
    else {
        puts("Sike! That was the wrong key!");
    }
}
