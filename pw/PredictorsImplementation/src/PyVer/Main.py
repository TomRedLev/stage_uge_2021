#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import *
from math import *
from Graphs import *




def naive_min_max(array, len_array) :
    # Counters : 
    cmpt_compar = 0

    # Graphs :
    tbsc_1 = create_tbsc()
    tbsc_2 = create_tbsc()

    minmax = [array[0], array[0]]
    for i in range(1, len_array) :
        if (tbsc_1.evolving_graph(array[i] < minmax[0])) :
            minmax[0] = array[i]
        if (tbsc_2.evolving_graph(array[i] > minmax[1])) :
            minmax[1] = array[i]
        cmpt_compar += 2

    print("First counter's current state :", tbsc_1.current_state)
    print("Second counter's current state :", tbsc_2.current_state)

    print("Naive_Min :", minmax[0], "\nNaive_Max :", minmax[1])
    print("Naive Comparisons :", cmpt_compar, "==", (2 * len_array) - 2)
    print("Naive Mispredictions :", tbsc_1.mispredictions + tbsc_2.mispredictions,"==", 2*log(len_array))

    return minmax


def min_max(array, len_array) :
    # Counters : 
    cmpt_compar = 0

    # Graphs : 
    tbsc_1 = create_tbsc()
    tbsc_2 = create_tbsc()
    tbsc_3 = create_tbsc()
    tbsc_4 = create_tbsc()
    tbsc_5 = create_tbsc()

    minmax = [array[len_array - 1], array[len_array - 1]]
    for i in range(len_array - 1) :
        if (tbsc_1.evolving_graph(array[i] < array[i + 1])) :
            if (tbsc_2.evolving_graph(array[i] < minmax[0])) :
                minmax[0] = array[i]
            if (tbsc_3.evolving_graph(array[i + 1] > minmax[1])) :
                minmax[1] = array[i + 1]
        else :
            if (tbsc_4.evolving_graph(array[i + 1] < minmax[0])) :
                minmax[0] = array[i + 1]
            if (tbsc_5.evolving_graph(array[i] > minmax[1])) :
                minmax[1] = array[i]
        cmpt_compar += 3

    print("First counter's current state :", tbsc_1.current_state)
    print("Second counter's current state :", tbsc_2.current_state)
    print("Third counter's current state :", tbsc_3.current_state)
    print("Fourth counter's current state :", tbsc_4.current_state)
    print("Fifth counter's current state :", tbsc_5.current_state)

    print("Min :", minmax[0],"\nMax :", minmax[1])
    print("Normal Comparisons :", cmpt_compar, "==", 3 / 2 * len_array)
    print("Normal Mispredictions :", tbsc_1.mispredictions + tbsc_2.mispredictions + tbsc_3.mispredictions + tbsc_4.mispredictions + tbsc_5.mispredictions, "==", len_array / 4 + log(len_array))
    return minmax

def complete_array(array, len_array) :
    for i in range(len_array) :
        array[i] = randrange(1000000)


def main() :
    len_array = randrange(2, 1000000)
    array = [0 for i in range(len_array)]
    print("len_array :", len_array)
    complete_array(array, len_array)
    # First test :
    naive_min_max(array, len_array)
    # Second test : 
    min_max(array, len_array)

if __name__ == "__main__":
    main()
