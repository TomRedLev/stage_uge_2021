#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matriceadjacence import *
# from graphviz import *

def determine_combination(val) :
    res = []
    def determine_combination_aux(val, lst_val) :
        if sum(lst_val) > val :
            return
        if sum(lst_val) == val and len(lst_val) >= val-1 :
            res.append(lst_val)
        for i in range(0, 2) :
            determine_combination_aux(val, lst_val + [i + 1])
    determine_combination_aux(val, [])
    
    return res
    

def construct_graphs() :
    """
    Supposed to construct a 4-states graph.
    """
    listG = []
    for lst in determine_combination(6) :
        G = MatriceAdjacence(4)
        G.ajouter_aretes([(0, 0), (3, 3)])
        i = 0
        reverse = False
        if (lst[len(lst)//2] == 2) :
            continue
        for elem in lst :
            if not reverse :
                G.ajouter_arete(i, i+elem)
                i += elem
            else :
                G.ajouter_arete(i, i-elem)
                i -= elem
            if (i == 3) :
                reverse = True
        listG.append(G)
            
    return listG
    
    

def main() :
    """
    Main function of the first practical work.
    """
    listG = construct_graphs()
    for i in range(len(listG)) :
        print(export_dot(listG[i], i))
    print(determine_combination(6))
    # tmp = export_dot(G, 0)
    # s = Source(tmp, filename="graph.dot", format="png")
    # s.view()
    
    

if __name__ == "__main__":
    # execute only if run as a script
    main()