#include <stdio.h>
#include <stdlib.h>


void init(){
    setvbuf(stdin,NULL,2,0);
    setvbuf(stdout,NULL,2,0);

}
int main() {
    init();

    int hero_status;
    char buf[64];
    
    printf("Greetings, brave adventurer!\n");
    printf("You stand at the entrance of the Hidden Castle, but the gates remain sealed.\n");
    printf("Prove your worth by speaking the sacred incantation, to prove you are the true hero!\n");
    
    hero_status = 0;
    gets(buf);
    
    if(hero_status == 0x1337){
        printf("The gates creak open, and you are deemed worthy to enter!\n");
        printf("The Demon King awaits...\nBut before the fight be sure to get the equipments first!\n");
        system("cat flag.txt");
    }
    
    return 0;
}
// gcc -m32 -Wimplicit-function-declaration -fno-stack-protector -o chal chal.c
