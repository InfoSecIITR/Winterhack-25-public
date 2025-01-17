#include <stdio.h>
#include <string.h>

void init_proc(){
    setvbuf(stdin,NULL,2,0);
    setvbuf(stdout,NULL,2,0);
    setvbuf(stderr,NULL,2,0);
}
int resistance = 0x20;

int main(){
    init_proc();
    int endurance = 0x20;
    char response[64];
    puts("It's the god of DESTRUCTION, Bigger than any thing imaginable and hot as burning Hell!!");
    puts("To defeat the Colossal_titan you need to have a specific amount of heat resistance capacity and endurance");
    puts("Unfortunately you only have limited capacity for heat resistance (as you are no iron man)");
    puts("But can you save your town from the unimaginable destruction by solely relying on your ENDURANCE"); 
    puts("do you want to fight or flight??");
    fgets(response,64,stdin);
    printf(response);
    puts("what is your endurance??");
    scanf("%d",&endurance);
    endurance = endurance & 0xffff;
    if(endurance*resistance == 0x13371337){
        puts("You proved me wrong, You are indeed a man of iron");
        system("/bin/sh");
    }
    return 0;
}