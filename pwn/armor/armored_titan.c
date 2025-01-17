#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void init_proc(){
    setvbuf(stdin,NULL,2,0);
    setvbuf(stdout,NULL,2,0);

}
void escape(){
    puts("looks like you defeated the armor");
    system("cat flag.txt\0");
    exit(0);
}
void armour(){
    char buffer[64];
    memset(buffer,0,64);
    void *idx = buffer;
    puts("What is your Titan Count");
    int num=0;
    scanf("%d",&num);
    for(int i=0;i<num;i++){
        printf("Name of %d Titan\n",i);
        scanf("%ld",idx);
        idx = idx+8;
    }
    
}

int main(){
    init_proc();
    puts("As you can see, the Armored Titan is one that specializes in hardening abilities.");
    puts("The ARMORED TITAN stands in your way to the ESCAPE room");
    puts("Find a way to bypass the ARMOR and get the SECRET of the escape room");
    printf("room key: %p\n",&escape);
    armour();
    puts("You lie helplessly in the battle field and soon to be devoured by the ARMORED TITAN");
    return 0;
    
}