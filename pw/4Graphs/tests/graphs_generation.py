#!/usr/bin/env python3
# -*- coding: utf-8

import copy

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
    test = generate_edges(2)
    print(test)
    print(len(test))



if __name__ == "__main__":
    # execute only if run as a script
    main()
