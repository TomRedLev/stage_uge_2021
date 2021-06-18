#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implémentation d'un graphe à l'aide d'une matrice d'adjacence. Les n sommets
sont identifiés par de simples naturels (0, 1, 2, ..., n-1).
"""

from copy import deepcopy
import numpy as np
import sympy as sp


class MatriceAdjacence(object):
    def __init__(self, num=0):
        """
        Initialise un graphe sans arêtes sur num sommets.

        >>> G = MatriceAdjacence()
        >>> G._matrice_adjacence
        []
        """
        self._matrice_adjacence = [[0] * num for _ in range(num)]

    def ajouter_arete(self, source, destination, p):
        """
        Ajoute l'arête {source, destination} au graphe, en créant les
        sommets manquants le cas échéant.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_arete(0, 1, 1)
        >>> G._matrice_adjacence
        [[0, 1], [0, 0]]
        """
        while (self.contient_sommet(source) != True) :
            self.ajouter_sommet()
        while (self.contient_sommet(destination) != True) :
            self.ajouter_sommet()
        self._matrice_adjacence[source][destination] += p

    def ajouter_aretes(self, iterable):
        """
        Ajoute toutes les arêtes de l'itérable donné au graphe. N'importe
        quel type d'itérable est acceptable, mais il faut qu'il ne contienne
        que des couples de naturels.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1, 1), (0, 3, 1)])
        >>> G._matrice_adjacence
        [[0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        """
        for elem in iterable :
            if elem[0] >= 0 :
                if elem[1] >= 0 :
                    self.ajouter_arete(elem[0], elem[1], elem[2])

    def ajouter_sommet(self):
        """
        Ajoute un nouveau sommet au graphe et renvoie son identifiant.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_sommet()
        0
        >>> G._matrice_adjacence
        [[0]]
        >>> G.ajouter_sommet()
        1
        >>> G._matrice_adjacence
        [[0, 0], [0, 0]]
        """
        i = 0
        while i < self.nombre_sommets() :
            j = len(self._matrice_adjacence[i])
            while j < (self.nombre_sommets() + 1):
                self._matrice_adjacence[i].append(0)
                j += 1
            i += 1
        self._matrice_adjacence.append([0] * (self.nombre_sommets() + 1))
        return self.nombre_sommets() - 1

    def aretes(self):
        """
        Renvoie l'ensemble des arêtes du graphe sous forme de couples (si on
        les stocke sous forme de paires, on ne peut pas stocker les boucles,
        c'est-à-dire les arêtes de la forme (u, u)).

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1, 1), (0, 3, 1)])
        >>> G.aretes()
        [(0, 1), (0, 3)]
        """
        lst = []
        i = 0
        while i < self.nombre_sommets() :
            j = 0
            while j < len(self._matrice_adjacence[i]) :
                if (i != j) :
                    if (self._matrice_adjacence[i][j] != 0) :
                        lst.append((i, j))
                j += 1
            i += 1
        return lst

    def boucles(self):
        """
        Renvoie les boucles du graphe, c'est-à-dire les arêtes reliant un
        sommet à lui-même.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 0, 1), (3, 3, 1)])
        >>> G.boucles()
        [(0, 0), (3, 3)]
        """
        lst = []
        i = 0
        while i < self.nombre_sommets() :
            j = 0
            while j < len(self._matrice_adjacence[i]) :
                if (i == j) :
                    if (self._matrice_adjacence[i][j] != 0) :
                        lst.append((i, j))
                j += 1
            i += 1
        return lst

    def contient_arete(self, u, v):
        """
        Renvoie True si l'arête {u, v} existe, False sinon.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1, 1), (3, 3, 1)])
        >>> G.contient_arete(0, 1)
        True
        """
        if (self.contient_sommet(u) == True) :
            i = 0
            if (v < len(self._matrice_adjacence[u])) :
                if (self._matrice_adjacence[u][v] != 0) :
                    return True
        return False

    def contient_sommet(self, u):
        """
        Renvoie True si le sommet u existe, False sinon.

        >>> G = MatriceAdjacence(2)
        >>> G.contient_sommet(1)
        True
        >>> G.contient_sommet(2)
        False
        """
        if (u < self.nombre_sommets()) :
            return True
        return False

    def degre(self, sommet):
        """
        Renvoie le degré d'un sommet, c'est-à-dire le nombre de voisins
        qu'il possède.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1, 1), (0, 3, 1)])
        >>> G.degre(0)
        2
        """
        count = 0
        if (self.contient_sommet(sommet) == True) :
            i = 0
            while (i < len(self._matrice_adjacence[sommet])) :
                if (self._matrice_adjacence[sommet][i] != 0) :
                    count += 1
                i += 1
        return count

    def nombre_aretes(self):
        """
        Renvoie le nombre d'arêtes du graphe.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1, 1), (0, 3, 1), (1, 3, 1)])
        >>> G.nombre_aretes()
        3
        """
        count = 0
        for i in range(self.nombre_sommets()) :
            for j in range(len(self._matrice_adjacence[i])) :
                if (self._matrice_adjacence[i][j] != 0) :
                    count += 1
        return count

    def nombre_boucles(self):
        """
        Renvoie le nombre d'arêtes de la forme {u, u}.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1, 1), (0, 3, 1), (1, 3, 1)])
        >>> G.nombre_boucles()
        0
        >>> G.ajouter_aretes([(0, 0, 1), (3, 3, 1)])
        >>> G.nombre_boucles()
        2
        """
        count = 0
        for i in range(self.nombre_sommets()) :
            if (self._matrice_adjacence[i][i] != 0) :
                count += 1
        return count

    def nombre_sommets(self):
        """
        Renvoie le nombre de sommets du graphe.

        >>> from random import randint
        >>> n = randint(0, 1000)
        >>> MatriceAdjacence(n).nombre_sommets() == n
        True
        """
        return len(self._matrice_adjacence)

    def retirer_arete(self, u, v):
        """
        Retire l'arête {u, v} si elle existe; provoque une erreur sinon.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0, 0, 1), (1, 1, 1)])
        >>> G.retirer_arete(0, 0)
        >>> G._matrice_adjacence
        [[0, 0], [0, 1]]
        """
        try :
            if (self.contient_sommet(u)) :
                if (v < len(self._matrice_adjacence[u])) :
                        self._matrice_adjacence[u][v] = 0
        except ValueError :
            print("error\n")
            raise

    def retirer_aretes(self, iterable):
        """
        Retire toutes les arêtes de l'itérable donné du graphe. N'importe
        quel type d'itérable est acceptable, mais il faut qu'il ne contienne
        que des couples d'éléments (quel que soit le type du couple).

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0, 0, 1), (1, 1, 1)])
        >>> G.retirer_aretes([(0, 0), (1, 1)])
        >>> G._matrice_adjacence
        [[0, 0], [0, 0]]
        """
        for elem in iterable :
            if type(elem[0]) == type(elem[1]) :
                self.retirer_arete(elem[0], elem[1])

    def retirer_sommet(self, sommet):
        """
        Déconnecte un sommet du graphe et le supprime.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0, 1, 1), (1, 1, 1)])
        >>> G.retirer_sommet(0)
        >>> G._matrice_adjacence
        [[1]]
        """
        for i in range(self.nombre_sommets()) :
            for j in range(len(self._matrice_adjacence[i])) :
                if j == sommet :
                    self.retirer_arete(i, j)
                    self._matrice_adjacence[i].pop(j)
        self._matrice_adjacence.pop(sommet)


    def retirer_sommets(self, iterable):
        """
        Efface les sommets de l'itérable donné du graphe, et retire toutes
        les arêtes incidentes à ces sommets.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0, 1, 1), (1, 1, 1)])
        >>> G.retirer_sommets([1, 0])
        >>> G._matrice_adjacence
        []
        """
        for elem in iterable :
            self.retirer_sommet(elem)

    def sommets(self):
        """
        Renvoie l'ensemble des sommets du graphe.

        >>> G = MatriceAdjacence(4)
        >>> G.sommets()
        [0, 1, 2, 3]
        """
        list = []
        for i in range(self.nombre_sommets()) :
            list.append(i)
        return list


    def sous_graphe_induit(self, iterable):
        """
        Renvoie le sous-graphe induit par l'itérable de sommets donné.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0, 1, 1), (1, 2, 1)])
        >>> G.sous_graphe_induit([0, 1])
        [(0, 1)]
        """
        lst = []
        for i in iterable :
            for j in range(self.nombre_sommets()) :
                for k in range(len(self._matrice_adjacence[j])) :
                    if i == k :
                        if self._matrice_adjacence[j][k] != 0 :
                            lst.append((j, k))
        return lst

    def voisins(self, sommet):
        """
        Renvoie la liste des voisins d'un sommet.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(1, 1, 1), (1, 2, 1)])
        >>> G.voisins(1)
        [1, 2]
        """
        list = []
        if (self.contient_sommet(sommet) == True) :
            for i in range(len(self._matrice_adjacence[sommet])) :
                if (self._matrice_adjacence[sommet][i] != 0) :
                    list.append(i)
        return list

    def ord_voisins(self, sommet):
        """
        Renvoie la liste des voisins d'un sommet.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(1, 1, 1), (1, 2, 1)])
        >>> G.ord_voisins(1)
        [1, 2]
        """
        p = sp.var("p")
        list = [-1, -1]
        if (self.contient_sommet(sommet) == True) :
            for i in range(len(self._matrice_adjacence[sommet])) :
                if (self._matrice_adjacence[sommet][i] == p) :
                    list[1] = i
                elif (self._matrice_adjacence[sommet][i] == 1 - p) :
                    list[0] = i
                elif (self._matrice_adjacence[sommet][i] == 1) : 
                    list[0] = i
                    list[1] = i
        return list

    # TODO
    def check_entrees(self) :
        """
        Renvoie True si chaque sommet a une arête entrante.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0, 1, 1), (1, 0, 1)])
        >>> G.check_entrees()
        True
        """
        lstmp = [0 * self.nombre_sommets() for _ in range(self.nombre_sommets())]
        for lst in self._matrice_adjacence :
            for i in range(len(lst)) :
                if lst[i] != 0 :
                    lstmp[i] = 1
        return lstmp == [1 * 1 for _ in range(self.nombre_sommets())]



def identity_matrix(n) :
    """
    Create a graph that is an identity.

    >>> identity_matrix(2)._matrice_adjacence
    [[1, 0], [0, 1]]
    """
    G = MatriceAdjacence(n)
    G.ajouter_aretes([(x, x, 1) for x in range(n)])
    return G

def export_dot(graphe, num, states):
    """
    Renvoie une chaîne encodant le graphe au format dot.

    >>> G = MatriceAdjacence(4)
    >>> G.ajouter_aretes([(0, 1, 1), (1, 2, 1), (2, 3, 1)])
    >>> print(export_dot(G, 0))
    graph graph0 {
    0;
    1;
    2;
    3;
    0 -> 1;
    1 -> 2;
    2 -> 3;
    }
    """
    p = sp.var("p")
    graph = "digraph graph" + str(num) +" {\ncenter=true;\npad=1;\ngraph [label=\"Graphe " + str(num) + " :\\n\", labelloc=t; labeljust=center, fontname=Helvetica, fontsize=18];\n"
    for sommet in graphe.sommets():
        var = sp.var("q" + str(sommet + 1))
        if states[var] == 1 :
            graph = graph + "node [color=black, shape=\"ellipse\", style=\"filled\", width=1, height=1, fillcolor=green] " + str(sommet) + ";\n"
        else :
            graph = graph + "node [color=black, shape=\"ellipse\", style=\"filled\", width=1, height=1, fillcolor=red] " + str(sommet) + ";\n"
    for boucle in graphe.boucles():
        if graphe._matrice_adjacence[boucle[0]][boucle[1]] == 1 :
            graph = graph + str(boucle[0]) + " -> " + str(boucle[1]) + "[style=dotted];\n"
            graph = graph + str(boucle[0]) + " -> " + str(boucle[1]) + ";\n"
        elif graphe._matrice_adjacence[boucle[0]][boucle[1]] == p :
            graph = graph + str(boucle[0]) + " -> " + str(boucle[1]) + ";\n"
        elif graphe._matrice_adjacence[boucle[0]][boucle[1]] == (1 - p) :
            graph = graph + str(boucle[0]) + " -> " + str(boucle[1]) + "[style=dotted];\n"
    for arete in graphe.aretes():
        if graphe._matrice_adjacence[arete[0]][arete[1]] == 1 :
            graph = graph + str(arete[0]) + " -> " + str(arete[1]) + "[style=dotted];\n"
            graph = graph + str(arete[0]) + " -> " + str(arete[1]) + ";\n"
        elif graphe._matrice_adjacence[arete[0]][arete[1]] == p :
            graph = graph + str(arete[0]) + " -> " + str(arete[1]) + ";\n"
        elif graphe._matrice_adjacence[arete[0]][arete[1]] == (1 - p) :
            graph = graph + str(arete[0]) + " -> " + str(arete[1]) + "[style=dotted];\n"
    graph = graph + "}"
    return graph

def tarjan(G) :
    """
    Take a graph and applies Tarjan Algorithm on it.

    >>> G = MatriceAdjacence(3)
    >>> G.ajouter_aretes([(0, 1, 1), (1, 2, 1), (2, 3, 1)])
    >>> tarjan(G)
    [[[3, 3, 3, False], [2, 2, 2, False]], [[1, 1, 1, False]], [[0, 0, 0, False]], []]
    """
    num = 0
    p = []
    partition = []
    lst = []

    def parcours(G, lst, num, p, partition, v) :
        """
        Aux function of tarjan.
        """
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
