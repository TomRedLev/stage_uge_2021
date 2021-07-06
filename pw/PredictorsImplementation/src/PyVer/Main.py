#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import *
from math import *
from Graphs import *
import matplotlib.pyplot as plt




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

    #print("First counter's current state :", tbsc_1.current_state)
    #print("Second counter's current state :", tbsc_2.current_state)

    #print("Naive_Min :", minmax[0], "\nNaive_Max :", minmax[1])
    #print("Naive Comparisons :", cmpt_compar, "==", (2 * len_array) - 2)
    msp = tbsc_1.mispredictions + tbsc_2.mispredictions
    #print("Naive Mispredictions :", tbsc_1.mispredictions + tbsc_2.mispredictions,"==", 2*log(len_array))

    return cmpt_compar, msp


def naive_min_max_obsc(array, len_array) :
    # Counters :
    cmpt_compar = 0

    # Graphs :
    obsc_1 = create_obsc()
    obsc_2 = create_obsc()

    minmax = [array[0], array[0]]
    for i in range(1, len_array) :
        if (obsc_1.evolving_graph(array[i] < minmax[0])) :
            minmax[0] = array[i]
        if (obsc_2.evolving_graph(array[i] > minmax[1])) :
            minmax[1] = array[i]
        cmpt_compar += 2
    msp = obsc_1.mispredictions + obsc_2.mispredictions

    return cmpt_compar, msp


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
    for i in range(0, len_array - 1, 2) :
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

    #print("First counter's current state :", tbsc_1.current_state)
    #print("Second counter's current state :", tbsc_2.current_state)
    #print("Third counter's current state :", tbsc_3.current_state)
    #print("Fourth counter's current state :", tbsc_4.current_state)
    #print("Fifth counter's current state :", tbsc_5.current_state)

    #print("Min :", minmax[0],"\nMax :", minmax[1])
    #print("Normal Comparisons :", cmpt_compar, "==", 3 / 2 * len_array)
    msp = tbsc_1.mispredictions + tbsc_2.mispredictions + tbsc_3.mispredictions + tbsc_4.mispredictions + tbsc_5.mispredictions
    #print("Normal Mispredictions :", msp, "==", len_array / 4 + log(len_array))
    return cmpt_compar, msp

def complete_array(array, len_array, size) :
    for i in range(len_array) :
        array[i] = randrange(1000000)


def main() :
    size = 10000
    naive_cmpt_compars = []
    naive_msps = []
    cmpt_compars = []
    msps = []
    osbc_cmpt_compars = []
    osbc_msps = []

    for len_array in range(2, size) :
        array = [0 for i in range(len_array)]
        #print("len_array :", len_array)
        complete_array(array, len_array, size)
        # First test :
        naive_cmpt_compar, naive_msp = naive_min_max(array, len_array)
        naive_cmpt_compars.append(naive_cmpt_compar)
        naive_msps.append(naive_msp)
        # Second test :
        cmpt_compar, msp = min_max(array, len_array)
        cmpt_compars.append(cmpt_compar)
        msps.append(msp)
        # Third test :
        osbc_cmpt_compar, osbc_msp = naive_min_max_obsc(array, len_array)
        osbc_cmpt_compars.append(osbc_cmpt_compar)
        osbc_msps.append(osbc_msp)


    fig, ax = plt.subplots()
    axe = [x for x in range(2, size)]
    ax.plot(axe, naive_cmpt_compars, label="naive_cmpt_compars")
    ax.plot(axe, [(2*x - 2) for x in range(2, size)], label="2*x - 2")
    ax.legend()
    plt.savefig('naive_min_max_compars.png', dpi=300, bbox_inches='tight')
    plt.clf()
    fig, ax = plt.subplots()
    axe = [x for x in range(2, size)]
    ax.plot(axe, naive_msps, label="naive_msps")
    ax.plot(axe, [(2 * log(x)) for x in range(2, size)], label="2 * log(x)")
    ax.legend()
    plt.savefig('naive_min_max_msps.png', dpi=300, bbox_inches='tight')
    plt.clf()

    fig, ax = plt.subplots()
    ax.plot(axe, cmpt_compars, label="cmpt_compars")
    ax.plot(axe, [(3/2 * x) for x in range(2, size)], label="3/2 * x")
    ax.legend()
    plt.savefig('min_max_compars.png', dpi=300, bbox_inches='tight')
    plt.clf()
    fig, ax = plt.subplots()
    ax.plot(axe, msps, label="msps")
    ax.plot(axe, [(x/4 + log(x)) for x in range(2, size)], label="x/4 + log(x)")
    ax.legend()
    plt.savefig('min_max_msps.png', dpi=300, bbox_inches='tight')
    plt.clf()

    fig, ax = plt.subplots()
    ax.plot(axe, osbc_cmpt_compars, label="obsc_naive_cmpt_compars")
    ax.plot(axe, [(2 * x - 2) for x in range(2, size)], label="2 * x - 2")
    ax.legend()
    plt.savefig('obsc_naive_min_max_compars.png', dpi=300, bbox_inches='tight')
    plt.clf()
    fig, ax = plt.subplots()
    ax.plot(axe, osbc_msps, label="obsc_naive_msps")
    ax.plot(axe, [(4 * log(x)) for x in range(2, size)], label="4 * log(x)")
    ax.legend()
    plt.savefig('obsc_naive_min_max_msps.png', dpi=300, bbox_inches='tight')
    plt.clf()




if __name__ == "__main__":
    main()
