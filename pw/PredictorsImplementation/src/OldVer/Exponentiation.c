#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int global_history[2] = {0, 0};
double cmpt[4] = {0, 0, 0, 0};

int exponentiation(int x, int n) {



    if (global_history[0] >= 2 && n == 1) {
        cmpt[1] += 1;
        if (global_history[0] < 3) {
            global_history[0] += 1;
        }
        return x;
    } else if (n == 1) {
        cmpt[0] += 1;
        cmpt[1] += 1;
        global_history[0] += 1;
        return x;
    } else {
        if (global_history[0] > 0) {
            global_history[0] -= 1;
        }
    }
    
    
    
    
    if (global_history[1] >= 2 && n%2 == 0) {
        cmpt[3] += 1;
        if (global_history[1] < 3) {
            global_history[1] += 1;
        }
        return exponentiation(x*x, n/2);
    } else if (n%2 == 0) {
        cmpt[2] += 1;
        cmpt[3] += 1;
        global_history[1] += 1;
        return exponentiation(x*x, n/2);
    } else {
        if (global_history[1] > 0) {
            global_history[1] -= 1;
        }
    }
    
    
    
    
    return exponentiation(x*x, (n - 1)/2);
        
}

int main(void) {
    srand(time(NULL));
    int x = rand() % 998 + 2;
    int n = rand() % 1000000 + 2;
    int exp = exponentiation(x, n);
    printf("Res exp %d^%d : %d\n", x, n, exp);
    
    printf("State of first if predictor : %d\nState of second if predictor : %d\n", global_history[0], global_history[1]);
    printf("Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\n", cmpt[0], cmpt[2]);
    
    return 0;
}
