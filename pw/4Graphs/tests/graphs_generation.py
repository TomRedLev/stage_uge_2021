#!/usr/bin/env python3
# -*- coding: utf-8

import copy

# Old version :
def determine_combinations(val) :
    """
    Construct all combinations_with_replacement of a val-length with values between
    0 and val (not included).

    >>> [i for i in determine_combinations(2)]
    [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1)]
    """
    return combinations_with_replacement([i for i in range(val)], (val)*2)


#Old version of isomorphism :
def create_matrix_p(k) :
    """
    Return a list of Matrix established on permutations of size k.
    """
    return [sp.Matrix([[0 if (elem != x) else 1 for x in range(k)] for elem in perm]) for perm in permutations(arange(k))]

def isomorphism_graphs(lstG, G2, lst_matrix_p) :
    """
    Verify if two graphs are isomorphs.
    Return True or False.
    """
    for G in lstG :
        for p in lst_matrix_p :
            A1 = sp.Matrix(G._matrice_adjacence)
            left = p * A1 * p**(-1)
            A2 = sp.Matrix(G2._matrice_adjacence)
            if (left == A2) :
                # print("skipped")
                return True
    return False


# Need to be called like :
# lstG = []
# lst_matrix_p = create_matrix_p(k)
# not isomorphism_graphs(lstG, G, lst_matrix_p)
# lstG.append(G)




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


def main() :
    """
    Main function of the first practical work.
    """
    n = int(input("Enter n : "))
    test = generate_edges(n)
    print(test)
    print(len(test))



if __name__ == "__main__":
    # execute only if run as a script
    main()
