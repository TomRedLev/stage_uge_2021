#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include "Graphs.h"

int cmpt_compar_naive = 0;
int cmpt_compar = 0;

int misprediction_naive = 0;
int misprediction = 0;

int* naive_min_max(int* array, int len_array) {
    Graph * tbsc_1 = create_tbsc();
    Graph * tbsc_2 = create_tbsc();
    int * minmax = (int *) malloc(2 * sizeof(int));
    minmax[0] = minmax[1] = array[0];
    int i;
    for (i = 1; i < len_array; i++) {
        /* First comparison : */
        if (evolving_graph(tbsc_1, array[i] < minmax[0], &misprediction_naive)) {
            minmax[0] = array[i];
        }

        /* Second comparison : */
        if (evolving_graph(tbsc_2, array[i] > minmax[1], &misprediction_naive)) {
            minmax[1] = array[i];
        } 

        cmpt_compar_naive += 2;
    }

    printf("First counter's current state : %d\n", tbsc_1->current_state);
    printf("Second counter's current state : %d\n", tbsc_2->current_state);
    return minmax;
}


int* min_max(int* array, int len_array) {
    Graph * tbsc_1 = create_tbsc();
    Graph * tbsc_2 = create_tbsc();
    Graph * tbsc_3 = create_tbsc();
    Graph * tbsc_4 = create_tbsc();
    Graph * tbsc_5 = create_tbsc();

    int * minmax = (int *) malloc(2 * sizeof(int));
    minmax[0] = minmax[1] = array[len_array - 1];
    int i;
    for (i = 0; i < len_array - 1; i += 2) {
        if (evolving_graph(tbsc_1, array[i] < array[i + 1], &misprediction)) {
            if (evolving_graph(tbsc_2, array[i] < minmax[0], &misprediction)) {
                minmax[0] = array[i];
            }
            if (evolving_graph(tbsc_3, array[i + 1] > minmax[1], &misprediction)) {
                minmax[1] = array[i + 1];
            }
        } else {
            if (evolving_graph(tbsc_4, array[i + 1] < minmax[0], &misprediction)) {
                minmax[0] = array[i + 1];
            }
            if (evolving_graph(tbsc_5, array[i] > minmax[1], &misprediction)) {
                minmax[1] = array[i];
            }
        }
        cmpt_compar += 3;
    }
    printf("First counter's current state : %d\n", tbsc_1->current_state);
    printf("Second counter's current state : %d\n", tbsc_2->current_state);
    printf("Third counter's current state : %d\n", tbsc_3->current_state);
    printf("Fourth counter's current state : %d\n", tbsc_4->current_state);
    printf("Fifth counter's current state : %d\n", tbsc_5->current_state);
    return minmax;
}

void complete_array(int* array, int len_array) {
    srand(time(NULL));
    int i;
    for (i = 0; i < len_array; i++) {
        array[i] = rand() % 1000000;
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
    printf("Normal Comparisons : %d == %d\n", cmpt_compar, 3 / 2 * len_array);
    printf("Normal Mispredictions : %d == %f\n", misprediction, len_array / 4 + log(len_array));
    return 0;
}
