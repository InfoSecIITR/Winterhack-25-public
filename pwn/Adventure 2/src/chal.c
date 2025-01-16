#include <stdio.h>
#include <stdlib.h>

int init() {
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
}
int main() {
    init();
    int balance=9999;
    int sword = 250;
    int shield = 500;
    int flag = 10000;
    int sword_quantity=1000;
    puts("Welcome adventurer to this shop!\nYou have a great battle ahead.") ;
    puts("Your chronicles will be sang with glory.As gratitude I give a special discount on the flag.");
    printf("The flag now costs only %d",flag);
    while (1) {
    puts("\n");
    puts("\n");
    printf("Your current balance is:\t %d\n", balance);
    printf("1. Buy a sword\t\tCost: %d\n", sword);
    printf("2. Buy a shield\t\tCost: %d\n", shield);
    printf("3. Buy the flag\t\tCost: %d\n", flag);
    puts("4. Exit");
    puts("\n");
    puts("What would you like to do?");
    int choice;
    scanf("%d", &choice);
    if (choice == 1) {
        if (balance >= sword) {
            int quantity;
            puts("How many swords would you like to buy?");
            scanf("%d", &quantity);
            if(quantity>sword_quantity){
                printf("Sorry but we only have %d swords left.",sword_quantity);
            }
            else{
            if(balance - quantity * sword < 0){
                puts("You don't have enough money!");
            }else{
                balance -= quantity * sword;
                sword_quantity-=quantity;
                printf("You bought %d swords!\n", quantity);}
            }
        } else {
            puts("You don't have enough money!");
        }
    } else if (choice == 2) {
        if (balance >= shield) {
            int quantity_shield;
            puts("How many shields would you like to buy?");
            scanf("%d", &quantity_shield);
            if(balance  < quantity_shield * shield){
                puts("You don't have enough money!");
            }else{
                balance -= quantity_shield * shield;
                printf("You bought %d shields!\n", quantity_shield);
            }
        } else {
            puts("You don't have enough money!");
        }
    } else if (choice == 3) {
        puts("I have only one flag for sale!");
        if (balance >= flag) {
            balance -= flag;
            puts("You bought the flag!");
            FILE *f = fopen("flag.txt", "r");
            if (f == NULL) {
                puts("flag not found: please run this on the server");
            } else {
                char buf[60];
                fgets(buf, 60, f);
                printf("YOUR FLAG IS: %s\n", buf);
                fclose(f);
                exit(1);
            }
        }
        else{
            puts("You don't have enough money!");
        }
    }
    else if (choice == 4) {
        puts("Goodbye!");
        exit(1);
    }
    else {
        puts("Invalid choice!");
        exit(1);
    }
    }
    
    return 0;
}
