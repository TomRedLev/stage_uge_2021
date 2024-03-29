#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include "Graphs.h"

int cmpt_compar_naive = 0;
int cmpt_compar = 0;

int misprediction_naive = 0;

int* naive_min_max(int* array, int len_array) {
    Graph * tbsc_1 = create_tbsc();
    Graph * tbsc_2 = create_tbsc();
    int * minmax = (int *) malloc(2 * sizeof(int));
    minmax[0] = minmax[1] = array[0];
    int i;
    for (i = 1; i < len_array; i++) {
        /* First comparison : */
        if (check_current_state(tbsc_1) == 1) {
            if (array[i] < minmax[0]) {
                minmax[0] = array[i];
                running_graph(tbsc_1, 1);
            } else {
                running_graph(tbsc_1, 0);
                misprediction_naive += 1;
            }
        }
        else {
            if (array[i] < minmax[0]) {
                minmax[0] = array[i];
                running_graph(tbsc_1, 1);
                misprediction_naive += 1;
            } else {
                running_graph(tbsc_1, 0);
            }
        }

        /*printf("Current state tbsc_1 = %d\n", tbsc_1->head->num_state);*/

        /* Second comparison : */
        if (check_current_state(tbsc_2) == 1) {
            if (array[i] > minmax[1]) {
                running_graph(tbsc_2, 1);
                minmax[1] = array[i];
            } else {
                running_graph(tbsc_2, 0);
                misprediction_naive += 1;
            }
        } else {
            if (array[i] > minmax[1]) {
                minmax[1] = array[i];
                running_graph(tbsc_2, 1);
                misprediction_naive += 1;
            } else {
                running_graph(tbsc_2, 0);
            }
        }

        cmpt_compar_naive += 2;
    }
    printf("%d\n", tbsc_1->head->num_state);
    printf("%d\n", tbsc_2->head->num_state);
    return minmax;
}


int* min_max(int* array, int len_array) {
    int * minmax = (int *) malloc(2 * sizeof(int));
    minmax[0] = minmax[1] = array[len_array - 1];
    int i;
    for (i = 0; i < len_array - 1; i += 2) {
        if (array[i] < array[i + 1]) {
            if (array[i] < minmax[0])
                minmax[0] = array[i];
            if (array[i + 1] > minmax[1])
                minmax[1] = array[i + 1];
        } else {
            if (array[i + 1] < minmax[0]) 
                minmax[0] = array[i + 1];
            if (array[i] > minmax[1])
                minmax[1] = array[i];
        }
        cmpt_compar += 3;
    }
    return minmax;
}

void complete_array(int* array, int len_array) {
    srand(time(NULL));
    int i;
    for (i = 0; i < len_array; i++) {
        array[i] = rand() % 1000;
    }
}


int main(void) {
    srand(time(NULL));
    int len_array = rand() % 1000000 + 2;
    int* array = (int *) malloc(len_array * sizeof(int));
    printf("len_array : %d\n", len_array);
    complete_array(array, len_array);
    int* naiveminmax = naive_min_max(array, len_array);
    printf("Naive_Min : %d\nNaive_Max : %d\n", naiveminmax[0], naiveminmax[1]);
    printf("Naive Comparisons : %d == %d\n", cmpt_compar_naive, (2 * len_array) - 2);
    printf("Naive Mispredictions : %d == %f\n", misprediction_naive, 2*log((double) len_array));
    int* minmax = min_max(array, len_array);
    printf("Min : %d\nMax : %d\n", minmax[0], minmax[1]);
    printf("Comparisons counter : %d == 3/2 * len_array\n", cmpt_compar);
    return 0;
}
