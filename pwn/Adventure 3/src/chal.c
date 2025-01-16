#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

__asm__(".global gadget1\n"
        "gadget1:\n"
        "pop %rdi\n"
        "ret\n");

__asm__(".global gadget2\n"
        "gadget2:\n"
        "pop %rsi\n"
        "ret\n");

__asm__(".global gadget3\n"
        "gadget3:\n"
        "pop %rdx\n"
        "ret\n");

int init() {
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
}
void defeat_demon_king(int sacred_sword, int magic_crystal, int hero_sigil) {
    if (sacred_sword == 0x1337cafe && magic_crystal == 0x1337babe && hero_sigil == 0xcafebabe) {
        printf("Congratulations, brave adventurer! You have defeated the Demon King and saved the kingdom!\n");
        system("/bin/sh\x00"); 
    } else {
        printf("Alas, adventurer! You lack the necessary relics to defeat the Demon King. The kingdom falls...\n");
        exit(1);
    }
}

void adventurer_prepares() {
    char backpack[64];
    printf("Adventurer, prepare for this quest. Enter your battle strategy: ");
    printf("You have only one chance to defeat the Demon King!\n");
    fgets(backpack, 0x100, stdin);
}

int main() {
    init();
    printf("Welcome, brave adventurer, the final batlle is about to begin!\n");
    printf("The Demon King resides ijust beyond this gate, awaiting your arrival...\n");
    adventurer_prepares();
    return 0;
}
//gcc chal.c -o chal -fno-stack-protector -no-pie