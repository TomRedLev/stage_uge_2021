#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matriceadjacence import *
from numpy import *
from itertools import combinations_with_replacement
from itertools import permutations
from time import *
from colorama import *
import sympy as sp
import doctest
import warnings
import copy

# New Graphs Generation :
def verify_ongoing_edges(n, lst) :
    for k in range(n) :
        if (lst.count(k) == 0) :
            return False
    return True

def generate_edges_aux(n, i, lst, lst_evolving) :
    if (i == -1) :
        return
    for j in range(n) :
        lst_evolving[i] = j
        if (lst_evolving not in lst and verify_ongoing_edges(n, lst_evolving)) :
            lst.append(copy.deepcopy(lst_evolving))
        generate_edges_aux(n, i-1, lst, lst_evolving)

def generate_edges(n) :
    lst = []
    lst_evolving = [0 for x in range(2*n)]
    generate_edges_aux(n, len(lst_evolving)-1, lst, lst_evolving)
    return lst






# New in-depth courses :
def explore(G, sommet, marked, etiquettes, path) :
    marked[sommet] = True
    etiquettes[sommet] = path
    voisins = G.voisins(sommet)
    if (len(voisins) == 2) :
        if (G._matrice_adjacence[sommet][voisins[0]] == (1-p)) :
            if marked[voisins[0]] != True :
                explore(G, voisins[0], marked, etiquettes, path + "NT")
            if marked[voisins[1]] != True :
                explore(G, voisins[1], marked, etiquettes, path + "T")
        else :
            if marked[voisins[1]] != True :
                explore(G, voisins[1], marked, etiquettes, path + "NT")
            if marked[voisins[0]] != True :
                explore(G, voisins[0], marked, etiquettes, path + "T")
    else :
        if marked[voisins[0]] != True :
            explore(G, voisins[0], marked, etiquettes, path + "NT")
        if marked[voisins[0]] != True :
            explore(G, voisins[0], marked, etiquettes, path + "T")

def indepth_course(G, set_paths) :
    keeped_signatures = set()
    for sommet in G.sommets() :
        marked = [False for x in range(len(G.sommets()))]
        etiquettes = ["" for x in range(len(G.sommets()))]
        explore(G, sommet, marked, etiquettes, "")
        keeped_signatures.add(":".join(etiquettes))
    if keeped_signatures.issubset(set_paths) :
        return False
    set_paths.update(keeped_signatures)
    return True







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


def calculate_stationary_probas(k, G, variables) :
    """
    Calculate the stationary stats for a given graph.

    >>> calculate_stationary_probas(2, construct_graph_from_permutation((0, 1, 0, 1), 2, 0.25), generate_variables(2))
    {q1: 0.250000000000000, q2: 0.750000000000000}
    """

    lst_eq = dot(array(variables), subtract(array(identity_matrix(k)._matrice_adjacence), array(G._matrice_adjacence))).tolist()
    lst_eq.append(sum(variables) - 1)
    return sp.solve(lst_eq, variables)


def test_stationary_probas(k, G, variables) :
    """
    Test if the probabilities seems correct.
    For now, the value of p is fixed but it will change.
    """
    p_val = float(input("Insert the value of the probability you want to applicate (between 0 and 1) : "))
    x = [1]
    x += [0 for i in range(1, k)]
    M = dot(array(G._matrice_adjacence), array(G._matrice_adjacence))
    i = 2
    while i <= k :
        M = dot(array(M), array(M))
        i *= i
    for elem in M :
        if 0 in elem :
            print("Not useful\n")
            return
    lst_eq = dot(array(x), M).tolist()
    # Print the exponentiation by squaring result :
    print("Tests probabilities : ")
    print([elem.subs({p:p_val}) for elem in lst_eq])
    # Print the law of large numbers result :
    lst_eq = dot(array(variables), subtract(array(identity_matrix(k)._matrice_adjacence), array(G._matrice_adjacence))).tolist()
    lst_eq.append(sum(variables) - 1)
    lst_eq.append(p - p_val)
    print("Probabiblities calculation : ")
    print(sp.solve(lst_eq))
    print()

def generate_variables(k) :
    """
    Generate the variables, using sympy, needed to create systems of equations.

    >>> generate_variables(2)
    (q1, q2)
    """
    return sp.var(" ".join(["q" + str(i) for i in range(1, k+1)]))


def integrate_probabilities(k, G, variables) :
    """
    Make integrates calculations to determine if a state should be Taken or Not Taken.
    """
    probas = calculate_stationary_probas(k, G, variables)
    score = 0
    states = {}
    for key in probas.keys() :
        f, g = probas[key] * (1 - p), probas[key] * p
        a, b = 0, 1
        expr_f = ((b - a) / 6) * (f.evalf(subs={p : a}) + 4 * f.evalf(subs={p : (a + b)/ 2}) + f.evalf(subs={p : b}))
        expr_g = ((b - a) / 6) * (g.evalf(subs={p : a}) + 4 * g.evalf(subs={p : (a + b)/ 2}) + g.evalf(subs={p : b}))
        if (expr_f <= expr_g) :
            print(Fore.GREEN, "Taking state", key, Fore.WHITE)
            score += expr_f
            states[key] = 1
        else :
            print(Fore.GREEN, "Not taking state", key, Fore.WHITE)
            score += expr_g
            states[key] = 0
    print(score)
    print()
    return score, states


def main() :
    """
    Main function of the first practical work.
    2 ## are for basic uses.

    >>> G = MatriceAdjacence(3)
    >>> G.ajouter_aretes([(0, 0, 0.9), (0, 1, 0.05), (0, 2, 0.05), (1, 0, 0.7), (1, 2, 0.3), (2, 0, 0.8), (2, 2, 0.2)])
    >>> variables = sp.var("q1 q2 q3")
    >>> calculate_stationary_probas(3, G, variables)
    {q1: 0.883977900552486, q2: 0.0441988950276243, q3: 0.0718232044198895}
    """
    # Variables :
    k = int(input("Insert the value k of the k-graphs you want to generate : "))
    p = sp.var("p")
    i = 0
    f = open("graphs.gv", "w")
    cmpt = 0
    variables = generate_variables(k)
    scores = {1 : (-1,1), 2 : (-1,1)}
    set_paths = set()

    # Starting the timer :
    time_perf = perf_counter()
    # Main loop :
    for edges in generate_edges(k) :
        G = construct_graph_from_permutation(edges, k, p)

        if (G.check_entrees()) :

            # Check :
            if (len(tarjan(G)) == 1) :
                if (indepth_course(G, set_paths)) :
                    res = calculate_stationary_probas(k, G, variables)
                    print("graph", i, " : ", G._matrice_adjacence, "\nprobabilities :", res)
                    #test_stationary_probas(k, G, variables) # Can be use to test the probabilities
                    score, states = integrate_probabilities(k, G, variables)
                    if score > 0 and score < scores[1][1] :
                        scores[1] = (i, score)
                    elif score > 0 and score < scores[2][1] :
                        scores[2] = (i, score)
                    f.write(export_dot(G, str(i), states))
                    f.write("\n")
                    i += 1

        cmpt += 1

    print(Style.RESET_ALL + str((perf_counter() - time_perf)), "seconds to run the generation of strongly connected", k, "- states graphs.")
    print("Number of loops :", cmpt)
    print("Founded optimal solutions are :", scores[1], "and", scores[2])
    f.close()


if __name__ == "__main__":
    doctest.testmod()
    warnings.simplefilter('ignore', np.RankWarning)
    main()
