#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

void init_proc(){
    setvbuf(stdin,NULL,2,0);
    setvbuf(stdout,NULL,2,0);
    setvbuf(stderr,NULL,2,0);
}

int main(){
    init_proc();
    char secret[32];
    char check[32]; 
    char cart[80];
    int fp = open("secret.txt",O_RDONLY);
    read(fp,secret,32);
    puts("You are devising a plan to defeat the BEAST TITAN....");
    puts("But without defeating the CART TITAN , the plan seems impossible to work");
    puts("It seems like there is a way to leak the contents of the cart and further destroying it");
    puts("how will you do so??");
    fgets(cart,80,stdin);
    printf(cart);
    puts("Thats all you get, tell me the contents of the cart :"); 
    fgets(check, 32, stdin); 
    if(!strcmp(secret, check)){
        puts("Okay here you go !");
        system("/bin/sh"); 
    }
    else {
        puts("Try harder !"); 
    }
    
    return 0;
    
}