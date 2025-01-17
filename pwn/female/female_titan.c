#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void init_proc(){
    setvbuf(stdin,NULL,2,0);
    setvbuf(stdout,NULL,2,0);
}
void win(){
    system("/bin/sh");
}

int main(){
    init_proc();
    char leak[16];
    char overwrite[128];
    puts("The Female Titan. It's an all-purpose unit, capable in every area. In addition to high mobility and endurance it posses incredible hardening ability");
    puts("Female Titan has left no RETURN door open for you, All you have is an EXIT door and Extreme LOVE for her.");
    puts("Anne has Surrounded herself by an unbreakable crystal cacoon");
    puts("You need to somehow leak her out??");
    fgets(leak,16,stdin);
    printf(leak);
    puts("Now you have her out of that cacoon, but can you OVERWRITE her Memory to make her LOVE you...");
    fgets(overwrite,128,stdin);
    printf(overwrite);
    exit(0);
}