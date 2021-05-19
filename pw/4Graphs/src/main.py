#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matriceadjacence import *
from itertools import combinations_with_replacement
from itertools import permutations
from time import *
from numpy import *
from colorama import *
import sympy as sp
import doctest

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


def calculate_stationary_probas(k, G, variables, rational_activation, not_solved) :
    """
    Calculate the stationary stats for a given graph.

    >>> calculate_stationary_probas(2, construct_graph_from_permutation((0, 1, 0, 1), 2, 0.25), generate_variables(2), False, False)
    {q2: 0.750000000000000, q1: 0.250000000000000}
    """

    lst_eq = dot(array(variables), subtract(array(identity_matrix(k)._matrice_adjacence), array(G._matrice_adjacence))).tolist()
    lst_eq.append(sum(variables) - 1)
    if (not_solved == True) :
        return lst_eq

    return sp.solve(lst_eq, simplify=False, minimal=True, rational=rational_activation)


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
    res = calculate_stationary_probas(k, G, variables, True, False)
    res.append(p - p_val)
    print("Probabiblities calculation : ")
    print(sp.solve(res))
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
    nb_mis = 0
    res = calculate_stationary_probas(k, G, variables, True, True)
    probas = sp.solve(res)
    print(probas)
    if len(probas) == 1 : # Need to put the block under in this condition
        for dic in probas :
            if (isinstance(dic,dict)) :
                # Need to find the good variable in here to correct the bugs of the lasts graphs (in k = 3 for example)
                q_val = sp.var("q" + str(k))

               # if (len(probas) > 1 and not p in dic.keys()):
               #     print(dic)
               #     break
               #
               # elif (len(probas) > 1 and p in dic.keys()) :
               #     print()
               #     break

               # Added to avoid TypeError during integrate calculations :
                if (dic[p].is_integer) :
                    break

                for i in range(1, k+1) :
                    if not (sp.var("q" + str(i)) in dic.keys()) :
                        q_val = sp.var("q" + str(i))

                expr = sp.solve(dic[p] - p, q_val)
                if (len(expr) == 1) :
                    expr = expr[0]
                    # print(Fore.CYAN + str(q_val), ":", expr)
                    # print(Fore.GREEN, "Not taken :", sp.simplify(sp.integrate(expr * (1 - p), (p, 0, 1))))
                    # print(Fore.GREEN, "Taken :", sp.simplify(sp.integrate(expr * p, (p, 0, 1))))
                    # We take the state where the integrate is the most important :
                    if (sp.integrate(expr * (1 - p), (p, 0, 1)) <= sp.integrate(expr * p, (p, 0, 1))) :
                        print(Fore.GREEN, "Taking state", q_val)
                    else :
                        print(Fore.GREEN, "Not taking state", q_val)

                for key in dic.keys() :
                    if (key != p) :
                        dic[key] = dic[key].subs(q_val, expr)
                        # print(Fore.CYAN + str(key), ":", dic[key])
                        # print(Fore.GREEN, "Not taken :", sp.integrate(dic[key] * (1 - p), (p, 0, 1)))
                        # print(Fore.GREEN, "Taken :", sp.integrate(dic[key] * p, (p, 0, 1)))
                        if (sp.integrate(dic[key] * (1 - p), (p, 0, 1)) <= sp.integrate(dic[key] * p, (p, 0, 1))) :
                            print(Fore.GREEN, "Taking state", key)
                        else :
                            print(Fore.GREEN, "Not taking state", key)
                nb_mis += 1

    print()
    return nb_mis


def main() :
    """
    Main function of the first practical work.
    2 ## are for basic uses.

    >>> G = MatriceAdjacence(3)
    >>> G.ajouter_aretes([(0, 0, 0.9), (0, 1, 0.05), (0, 2, 0.05), (1, 0, 0.7), (1, 2, 0.3), (2, 0, 0.8), (2, 2, 0.2)])
    >>> variables = sp.var("q1 q2 q3")
    >>> calculate_stationary_probas(3, G, variables, True, False)
    {q3: 13/181, q2: 8/181, q1: 160/181}
    """
    # Variables :
    k = int(input("Insert the value k of the k-graphs you want to generate : "))
    p = sp.var("p")
    i = 0
    f = open("graphs.gv", "w")
    cmpt = 0
    cmpt_tarj = 0
    ## cmpt_rates = 0 # Necessary if rational=False is activated
    variables = generate_variables(k)
    nb_found = 0

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
##                    res = calculate_stationary_probas(k, G, variables, False, False)
##                    # Necessary if rational=False is activated
##                    if res == [] :
##                        res = calculate_stationary_probas(k, G, variables, True, False)
##                        cmpt_rates += 1
                    # Comment to save a few seconds :
                    print(Fore.RED + "graph", i, " : ") # "# print(Fore.RED + "graph", i, " : ", res)
                    ## test_stationary_probas(k, G, variables) # Can be use to test the probabilities
                    nb_found += integrate_probabilities(k, G, variables)
                    i += 1
                    cmpt_tarj += 1

            cmpt += 1

    print(Style.RESET_ALL + str((perf_counter() - time_perf)), "seconds to run the generation of strongly connected", k, "- states graphs.")
    print("Number of loops :", cmpt)
    ## print("Number of missing solutions (now catched up) :", cmpt_rates)
    print("Number of founded solutions :", nb_found, "on", cmpt_tarj)
    f.close()


if __name__ == "__main__":
    # execute only if run as a script
    doctest.testmod()
    main()
