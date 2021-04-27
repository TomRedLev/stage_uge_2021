#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implémentation d'un graphe à l'aide d'une matrice d'adjacence. Les n sommets
sont identifiés par de simples naturels (0, 1, 2, ..., n-1).
"""


class MatriceAdjacence(object):
    def __init__(self, num=0):
        """
        Initialise un graphe sans arêtes sur num sommets.

        >>> G = MatriceAdjacence()
        >>> G._matrice_adjacence
        []
        """
        self._matrice_adjacence = [[0] * num for _ in range(num)]

    def ajouter_arete(self, source, destination):
        """
        Ajoute l'arête {source, destination} au graphe, en créant les
        sommets manquants le cas échéant.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_arete(0, 1)
        >>> G._matrice_adjacence
        [[0, 1], [0, 0]]
        """
        while (self.contient_sommet(source) != True) :
            self.ajouter_sommet()
        while (self.contient_sommet(destination) != True) :
            self.ajouter_sommet()
        self._matrice_adjacence[source][destination] = 1

    def ajouter_aretes(self, iterable):
        """
        Ajoute toutes les arêtes de l'itérable donné au graphe. N'importe
        quel type d'itérable est acceptable, mais il faut qu'il ne contienne
        que des couples de naturels.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1), (0, 3)])
        >>> G._matrice_adjacence
        [[0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        """
        for elem in iterable :
            if elem[0] >= 0 :
                if elem[1] >= 0 :
                    self.ajouter_arete(elem[0], elem[1])

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
        >>> G.ajouter_aretes([(0, 1), (0, 3)])
        >>> G.aretes()
        [(0, 1), (0, 3)]
        """
        lst = []
        i = 0
        while i < self.nombre_sommets() :
            j = 0
            while j < len(self._matrice_adjacence[i]) :
                if (i != j) :
                    if (self._matrice_adjacence[i][j] == 1) :
                        lst.append((i, j))
                j += 1
            i += 1
        return lst

    def boucles(self):
        """
        Renvoie les boucles du graphe, c'est-à-dire les arêtes reliant un
        sommet à lui-même.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 0), (3, 3)])
        >>> G.boucles()
        [(0, 0), (3, 3)]
        """
        lst = []
        i = 0
        while i < self.nombre_sommets() :
            j = 0
            while j < len(self._matrice_adjacence[i]) :
                if (i == j) :
                    if (self._matrice_adjacence[i][j] == 1) :
                        lst.append((i, j))
                j += 1
            i += 1
        return lst

    def contient_arete(self, u, v):
        """
        Renvoie True si l'arête {u, v} existe, False sinon.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1), (3, 3)])
        >>> G.contient_arete(0, 1)
        True
        """
        if (self.contient_sommet(u) == True) :
            i = 0
            if (v < len(self._matrice_adjacence[u])) :
                if (self._matrice_adjacence[u][v] == 1) :
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
        >>> G.ajouter_aretes([(0, 1), (0, 3)])
        >>> G.degre(0)
        2
        """
        count = 0
        if (self.contient_sommet(sommet) == True) :
            i = 0
            while (i < len(self._matrice_adjacence[sommet])) :
                if (self._matrice_adjacence[sommet][i] == 1) :
                    count += 1
                i += 1
        return count

    def nombre_aretes(self):
        """
        Renvoie le nombre d'arêtes du graphe.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1), (0, 3), (1, 3)])
        >>> G.nombre_aretes()
        3
        """
        count = 0
        for i in range(self.nombre_sommets()) :
            for j in range(len(self._matrice_adjacence[i])) :
                if (self._matrice_adjacence[i][j] == 1) :
                    count += 1
        return count

    def nombre_boucles(self):
        """
        Renvoie le nombre d'arêtes de la forme {u, u}.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_aretes([(0, 1), (0, 3), (1, 3)])
        >>> G.nombre_boucles()
        0
        >>> G.ajouter_aretes([(0, 0), (3, 3)])
        >>> G.nombre_boucles()
        2
        """
        count = 0
        for i in range(self.nombre_sommets()) :
            if (self._matrice_adjacence[i][i] == 1) :
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
        >>> G.ajouter_aretes([(0, 0), (1, 1)])
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
        >>> G.ajouter_aretes([(0, 0), (1, 1)])
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
        >>> G.ajouter_aretes([(0, 1), (1, 1)])
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
        >>> G.ajouter_aretes([(0, 1), (1, 1)])
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
        >>> G.ajouter_aretes([(0, 1), (1, 2)])
        >>> G.sous_graphe_induit([0, 1])
        [(0, 1)]
        """
        lst = []
        for i in iterable :
            for j in range(self.nombre_sommets()) :
                for k in range(len(self._matrice_adjacence[j])) :
                    if i == k :
                        if 1 == self._matrice_adjacence[j][k] :
                            lst.append((j, k))
        return lst

    def voisins(self, sommet):
        """
        Renvoie la liste des voisins d'un sommet.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(1, 1), (1, 2)])
        >>> G.voisins(1)        
        [1, 2]
        """
        list = []
        if (self.contient_sommet(sommet) == True) :
            for i in range(len(self._matrice_adjacence[sommet])) :
                if (self._matrice_adjacence[sommet][i] == 1) :
                    list.append(i)
        return list


def export_dot(graphe, num):
    """
    Renvoie une chaîne encodant le graphe au format dot.
    >>> G = MatriceAdjacence(4)
    >>> G.ajouter_aretes([(0,1), (1,2), (2,3)])
    
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
    graph = "graph graph" + str(num) +" {" + '\n'
    for sommet in graphe.sommets():
        graph = graph + str(sommet) + ";" + '\n'
    for boucle in graphe.boucles():
        graph = graph + str(boucle[0]) + " -> " + str(boucle[1]) + ";" + '\n'
    for arete in graphe.aretes():
        graph = graph + str(arete[0]) + " -> " + str(arete[1]) + ";" + '\n'
    graph = graph + "}"
    return graph


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()