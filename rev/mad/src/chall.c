#include <fcntl.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>

/* MT19937 PRNG */
typedef struct {
    uint32_t state[624];
    uint32_t index;
} MT19937;

void __attribute__ ((noinline)) MT19937_init(MT19937* const rng, uint32_t seed) {
    rng->index = 0;
    rng->state[0] = seed;
    for (int i = 1; i < 624; i++) {
        rng->state[i] = 0x6c078965 * (rng->state[i - 1] ^ (rng->state[i - 1] >> 30)) + i;
    }
}

uint32_t __attribute__ ((noinline)) MT19937_next(MT19937* const rng) {
    if (rng->index == 0) {
        for (int i = 0; i < 624; i++) {
            uint32_t y = (rng->state[i] & 0x80000000) + (rng->state[(i + 1) % 624] & 0x7fffffff);
            rng->state[i] = rng->state[(i + 397) % 624] ^ (y >> 1);
            if (y & 1) {
                rng->state[i] = rng->state[i] ^ 0x9908b0df;
            }
        }
    }

    uint32_t y = rng->state[rng->index];
    y = y ^ (y >> 11);
    y = y ^ ((y << 7) & 0x9d2c5680);
    y = y ^ ((y << 15) & 0xefc60000);
    y = y ^ (y >> 18);

    rng->index = (rng->index + 1) % 624;
    return y;
}


void display_banner() {
    puts("What were the numbers Mason?");
}

void display_menu() {
    puts("|===============================|");
    puts("|           Main Menu           |");
    puts("|-------------------------------|");
    puts("| 1. Get a Random  Number       |");
    puts("| 2. Guess Hidden Numbers       |");
    puts("| 3. Quit                       |");
    puts("|==============***==============|");
}

int main() {
    setvbuf(stdout, NULL, _IONBF, BUFSIZ);

    display_banner();

    int urandom = open("/dev/urandom", O_RDONLY);
    uint32_t seed;
    read(urandom, &seed, 4);

    MT19937 mt;
    MT19937_init(&mt, seed);

    char choice = 0;
    int tries = 625;
    bool solved = false;

    uint32_t hidden_numbers[10];

    for (int i = 0; i < 10; i++) {
        hidden_numbers[i] = MT19937_next(&mt);
    }

    while (tries > 0 && !solved) {
        display_menu();

        printf("> ");
        choice = getchar();

        if (getchar() != '\n') { // newline
            puts("Only one input at a time. Why rush?");
            return EXIT_FAILURE;
        }
        

        switch (choice) {
            case '1':
                printf(">> %u\n", MT19937_next(&mt));
                tries -= 1;
                break;

            case '2':
                // puts("[DEBUG] State: [");
                // for (int i=0; i<624; i++) {
                //     printf("%u, ", mt.state[i]);
                // }
                // puts("]");

                tries -= 1;
                solved = true;

                for (int i = 0; i < 10; i++) {
                    // printf("[DEBUG] Guess [%2d/10] > %u\n", i+1, hidden_numbers[i]);
                    printf("Guess [%2d/10] > ", i+1);
                    char buf[20];
                    fgets(buf, 20, stdin);
                    uint32_t guess = strtoul(buf, NULL, 10);
                    if (guess != hidden_numbers[i]) {
                        puts("Nope.");
                        solved = false;
                        break;
                    }
                }
                break;

            case '3':
                puts("Bye!");
                return EXIT_SUCCESS;

            default:
                puts("Invalid Choice.");
                return EXIT_FAILURE;
        }
    }
    if (tries < 0) {
        puts("You put too much load on the server! Be careful next time!");
        return EXIT_FAILURE;
    }

    close(urandom);

    if (solved) {
        puts("Here's your flag:");
        int flag = open("flag.txt", O_RDONLY);
        char buf[49];
        read(flag, buf, 48);
        buf[48] = '\0';
        puts(buf);
        close(flag);
    } else {
        puts("NGMI.");
    }

    return 0;
}