#include <stdlib.h>
#include <stdio.h>
#include <time.h>



int* min_max(int* array, int len_array) {
    /* Predictors simulator : */
    int* global_history = (int *) calloc(2, sizeof(int)); /* Number of if */
    /* Stats of predictors : */
    double* cmpt = (double *) calloc(4, sizeof(double));
    int* minmax = (int *) malloc(4 * sizeof(int));
    int i;
    minmax[0] = array[0], minmax[1] = 0, minmax[2] = array[0], minmax[3] = 0;
    for (i = 1; i < len_array; i++) {
        /* Modification done to implements a predictor */
        if (global_history[0] >= 2 && array[i] < minmax[0]) {
            cmpt[1] += 1.;
            if (global_history[0] < 3) {
                global_history[0] += 1;
            }
            minmax[0] = array[i];
            minmax[1] = i;
        } else if (array[i] < minmax[0]) {
            cmpt[0] += 1.;
            cmpt[1] += 1.;
            global_history[0] += 1;
            minmax[0] = array[i];
            minmax[1] = i;
        } else {
            if (global_history[0] > 0) {
                global_history[0] -= 1;
            }
        }
        /* Modification done to implements a predictor */
        if (global_history[1] >= 2 && array[i] > minmax[2]) {
            cmpt[3] += 1.;
            if (global_history[1] < 3) {
                global_history[1] += 1;
            }
            minmax[2] = array[i];
            minmax[3] = i;
        } else if (array[i] > minmax[2]) {
            cmpt[2] += 1.;
            cmpt[3] += 1.;
            global_history[1] += 1;
            minmax[2] = array[i];
            minmax[3] = i;
        } else {
            if (global_history[1] > 0) {
                global_history[1] -= 1;
            }
        }
    }
    printf("State of first if predictor : %d\nState of second if predictor : %d\n", global_history[0], global_history[1]);
    printf("Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\n", cmpt[0]/cmpt[1], cmpt[2]/cmpt[3]);
    return minmax;
}

void complete_array(int* array, int len_array) {
    srand(time(NULL));
    int i;
    for (i = 0; i < len_array; i++) {
        array[i] = rand() % 1000;
    }
}

/*
void display_array(int* array, int len_array) {
    int i;
    for (i = 0; i < len_array; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}
*/

int main(void) {
    srand(time(NULL));
    int len_array = rand() % 998 + 2;
    int* array = (int *) malloc(len_array * sizeof(int));
    printf("len_array : %d\n", len_array);
    complete_array(array, len_array);
    int* minmax = min_max(array, len_array);
    printf("Min : %d, at rank : %d\nMax : %d, at rank : %d\n", minmax[0], minmax[1], minmax[2], minmax[3]);
    /* display_array(array, len_array); */
    return 0;
}
