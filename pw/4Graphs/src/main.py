#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matriceadjacence import *
from itertools import combinations_with_replacement
from itertools import permutations
from time import *
from numpy import *
import sympy as sp

def determine_combinations(val) :
    """
    Construct all combinations_with_replacement of a val-length with values between
    0 and val (not included).
    
    >>> [i for i in determine_combinations(2)]
    [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1)]
    """
    return combinations_with_replacement([i for i in range(val)], (val)*2)
    
    
def construct_graph_from_permutation(permut, k, p) :
    """
    Supposed to construct a strongly connected k-states graph.
    There is a probability of p on Taken brenches, and a probability of 1-p on Not Taken branches.
    p must be between 0 and 1.
    
    >>> construct_graph_from_permutation((0, 1, 0, 1), 2, 0.25)._matrice_adjacence
    [[0.25, 0.75], [0.25, 0.75]]
    """
    G = MatriceAdjacence(k)
    for i in range(0, len(permut), 2) :
        G.ajouter_aretes([(i//2, permut[i], p), (i//2, permut[i+1], 1-p)])
    return G


def calculate_stationary_stats(k, G, variables) :
    """
    Calculate the stationary stats for a given graph.
    
    >>> calculate_stationary_stats(2, construct_graph_from_permutation((0, 1, 0, 1), 2, 0.25), generate_variables(2))
    {q2: 0.750000000000000, q1: 0.250000000000000}
    """
    lst_eq = dot(array(variables), subtract(array(identity_matrix(k)._matrice_adjacence), array(G._matrice_adjacence))).tolist()
    lst_eq.append(sum(variables) - 1)
    return sp.solve(lst_eq)
    
    
def generate_variables(k) :
    """
    Generate the variables, using sympy, needed to create systems of equations.
    
    >>> generate_variables(2)
    (q1, q2)
    """
    return sp.var(" ".join(["q" + str(i) for i in range(1, k+1)]))

def main() :
    """
    Main function of the first practical work.
    """
    # Functions tests :
    # import doctest
    # doctest.testmod()
    
    # Variables :
    k = int(input("Insert the value k of the k-graphs you want to generate : "))
    p = float(input("Insert the value p of the probability to go on a Taken branch : "))
    i = 0
    f = open("graphs.gv", "w")
    cmpt = 0
    variables = generate_variables(k)
    
    # Starting the timer :
    time_perf = perf_counter()
    # Main loop :
    for combi in determine_combinations(k) :
        for permut in set(map(lambda x: tuple(x),permutations(combi, len(combi)))) :
            G = construct_graph_from_permutation(permut, k, p)
            
            if (G.check_entrees()) :
                
                # Check :
                if (len(tarjan(G)) == 1) :
                    f.write(export_dot(G, str(i)))
                    f.write("\n")
                    res = calculate_stationary_stats(k, G, variables)
                    # Comment to save a few seconds :
                    print("graph", i, " : ", res)
                    i += 1
                    
            cmpt += 1
            
    print((perf_counter() - time_perf), " seconds to run the generation of strongly connected ", k, "-states graphs.")
    print("Number of loops : ", cmpt)
    f.close()


if __name__ == "__main__":
    # execute only if run as a script
    main()
