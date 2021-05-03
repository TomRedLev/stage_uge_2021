#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matriceadjacence import *
from pygraphviz import *
from graphviz import *
from itertools import combinations_with_replacement
from itertools import permutations
from time import *

def determine_combinations(val) :
    """
    Construct all combinations_with_replacement of a val-length with values between
    0 and val (not included).
    """
    return combinations_with_replacement([i for i in range(val)], (val)*2)
    
    
def construct_graph_from_permutation(permut, k, p) :
    """
    Supposed to construct a strongly connected k-states graph.
    There is a probability of p on Taken brenches, and a probability of 1-p on Not Taken branches.
    p must be between 0 and 1.
    """
    G = MatriceAdjacence(k)
    for i in range(0, len(permut), 2) :
        G.ajouter_aretes([(i//2, permut[i], p), (i//2, permut[i+1], 1-p)])
    return G

def tarjan(G) :
    """
    Take a graph and applies Tarjan Algorithm on it.
    """
    num = 0
    p = []
    partition = []
    lst = []
    
    def parcours(G, lst, num, p, partition, v) :
        lst[v][1] = num # v.num
        lst[v][2] = num # v.numAccessible
        num = num + 1
        p.append(lst[v])
        lst[v][3] = True # v.dansP
        
        for w in G.voisins(v) :
            if lst[w][2] == None :
                parcours(G, lst, num, p, partition, w)
                lst[v][2] = min(lst[v][2], lst[w][2])
            elif lst[w][3] == True :
                lst[v][2] = min(lst[v][2], lst[w][1])
        
        if lst[v][2] == lst[v][1] :
            c = []
            if p != [] :
                while True :
                    w = p.pop()
                    w[3] = False
                    c.append(w)
                    if (w != lst[v] or p == []) :
                        break
            partition.append(c)
    
    for sommet in G.sommets() :
        lst.append([sommet, None, None, False])
    for sommet in G.sommets() :
        if lst[sommet][1] == None :
            parcours(G, lst, num, p, partition, sommet)
#        if (len(partition) > 1) :
#            return partition
    return partition



def main() :
    """
    Main function of the first practical work.
    """
    # Variables :
    k = int(input("Insert the value k of the k-graphs you want to generate : "))
    p = float(input("Insert the value p of the probability to go on a Taken branch : "))
    i = 0
    f = open("graphs.gv", "w")
    cmpt = 0
    
    # Starting the timer :
    time_perf = perf_counter()
    # Main loop :
    for combi in determine_combinations(k) :
        for permut in set(map(lambda x: tuple(x),permutations(combi, len(combi)))) :
            G = construct_graph_from_permutation(permut, k, p)
            
            if (G.check_entrees()) :
                
                # Check
                if (len(tarjan(G)) == 1) :
#                    print(len(val[0]))
#                    print(permut)
                    f.write(export_dot(G, str(i)))
                    f.write("\n")
                    i += 1
            cmpt += 1
    print(str(perf_counter() - time_perf) + " seconds to run the generation of strongly connected " + str(k) + "-states graphs.")
    print("Number of loops : " + str(cmpt))


if __name__ == "__main__":
    # execute only if run as a script
    main()
