// Zion Amsalem ADV 2025 Day 1 C version
#include <stdio.h>
#include <stdlib.h>

void move_right(int *lock, int steps){
    *lock = (*lock + (steps % 100));
    if (*lock >= 100){
        *lock = (*lock - 100);
    };
}

void move_left(int *lock, int steps){
    *lock = (*lock - (steps % 100));
    if (*lock < 0){
        *lock = (*lock + 100);
    };
}

FILE* load_file(const char *path){
    FILE *input = fopen(path, "r");
    if (!input) {
        perror("an error occurred while trying to open this file");
        return NULL;
    };
    return input;
}

int pick(int *lock, FILE* file){
    int result = 0;
    char line[256];

    while (fgets(line, sizeof(line), file)) {
        char direction = line[0];
        int steps = atoi(&line[1]);

        if (direction == 'R'){
            move_right(lock, steps);
        }else if (direction == 'L'){
            move_left(lock, steps);
        };
        if (*lock == 0){
            result++;
        }
    };
    fclose(file);
    return result;
}

int main(){
    int lock = 50;
    const char *path = "../input.txt";
    FILE* loaded_file = load_file(path);

    if (!loaded_file) {
        return 1;
    }
    int res = pick(&lock, loaded_file);
    printf("the result of the secret is: %d\n",res);
    return 0;
}


