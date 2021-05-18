#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int global_history[3] = {0, 0, 0};
double cmpt[6] = {0, 0, 0, 0, 0, 0};

int dichotomie(int* array, int start, int end, int val) {
    int mid = (start + end) / 2;
    if (global_history[0] >= 2 && (start == end || start == mid) && val != array[mid]) {
        cmpt[1] += 1;
        if (global_history[0] < 3) {
            global_history[0] += 1;
        }
        return -1;
    } else if ((start == end || (start == mid)) && val != array[mid]) {
        cmpt[0] += 1;
        cmpt[1] += 1;
        global_history[0] += 1;
        return -1;
    } else {
        if (global_history[0] > 0) {
            global_history[0] -= 1;
        }
    }
    
    if (global_history[1] >= 2 && val == array[mid]) {
        cmpt[3] += 1;
        if (global_history[1] < 3) {
            global_history[1] += 1;
        }
        return mid;
    } else if (val == array[mid]) {
        cmpt[2] += 1;
        cmpt[3] += 1;
        global_history[1] += 1;
        return mid;
    } else {
        if (global_history[1] > 0) {
            global_history[1] -= 1;
        }
    }
    
    if (global_history[2] >= 2 && val < array[mid]) {
        cmpt[5] += 1;
        if (global_history[2] < 3) {
            global_history[2] += 1;
        }
        return dichotomie(array, start, mid - 1, val);
    } else if (val < array[mid]) {
        cmpt[4] += 1;
        cmpt[5] += 1;
        global_history[2] += 1;
        return dichotomie(array, start, mid - 1, val);
    } else {
        if (global_history[2] > 0) {
            global_history[2] -= 1;
        }
    }
    return dichotomie(array, mid + 1, end, val);;
}

void complete_array(int* array, int len_array) {
    srand(time(NULL));
    int i;
    for (i = 0; i < len_array; i++) {
        array[i] = i + rand() % 2;
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
    int val = rand() % len_array;
    int* array = (int *) malloc(len_array * sizeof(int));
    complete_array(array, len_array);
    printf("Array completed\n");
    int dicho = dichotomie(array, 0, len_array, val);
    printf("Found or not at pos : %d\n%d == %d\n", dicho, val, array[dicho]);
    
    printf("State of first if predictor : %d\nState of second if predictor : %d\nState of third if predictor : %d\n", global_history[0], global_history[1], global_history[2]);
    printf("Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\nStat of mispredictions of the predictor 3 : %f\n", cmpt[0]/cmpt[1], cmpt[2]/cmpt[3], cmpt[4]/cmpt[5]);
    
    /* display_array(array, len_array); */
    return 0;
}
