#include <stdio.h>
#include <string.h>

void init_proc(){
    setvbuf(stdin,NULL,2,0);
    setvbuf(stdout,NULL,2,0);
    setvbuf(stderr,NULL,2,0);
}

int main(){
    char jaws[96];
    init_proc();
    puts("Heavy wind blows!!!");
    puts("And within a snap of time, you found yourself inside the jaws of JAW TITAN");
    puts("But with the help of your newly learned crystaline ability, You manages to survive the devastating bite");
    printf("You soon remembered the secret of this new world %p\n", (void *)puts);
    puts("Help youself out of his mouth and RETURN TO THE NEW WORLD");
    puts("what will you do???");
    read(0,jaws,160);
    return 0;
}