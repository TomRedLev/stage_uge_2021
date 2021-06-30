# Notes de réunions :

## Réunion du Lundi 26 Avril 2021 :
hennessy et patterson <br />
https://arxiv.org/pdf/1804.00261.pdf <br />
https://www.irisa.fr/caps/people/seznec/ISCA05.pdf <br />
algo de distance d’édition entre deux mots <br />
https://fr.wikipedia.org/wiki/Distance_de_Levenshtein <br />
Google scholar <br />
<br />
1. Etude expérimentale (PAPY) <br />
2. Simuler les prédicteurs <br />
3. Etude théorique <br />
https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_Markov <br />
<br />
Inversion de matrice <br />
<br />
RDV Jeudi 29 Avril à 17h <br />
<br />
Installation Pypy. <br />
<br />
Simulateur : écrire programme avec des branchements. <br />
Simuler travaille de la machine. <br />
PoC : Proof of Concept. <br />
Faire un example de prédicteur de branchements : MinMax, Expo rapide, Dichotomie, ... <br />
Récupérer toutes les informations sur le parcours du prédicteur. <br />
Programme de la semaine : faire un PoC, terminer le programme de génération des graphes. <br />
<br />
http://ligm.u-pem.fr/evenements/seminaires/ <br />
Evaluer intégrales, faire calcul numérique. <br /> 
https://fr.wikipedia.org/wiki/Isomorphisme_de_graphes <br />
https://en.wikipedia.org/wiki/Adjacency_matrix#Isomorphism_and_invariants<br />
Checker si dans la liste des graphes avec fonction isomorphisme, si non faire les calculs et rajouter, si oui skip. <br />
<br />
Essayer de multi-threader le programme (en mettant 1/4 sur chaque coeur). <br />
Mise en forme des graphes (tagués les arrêtes). <br />
Faire une explication des chaînes de Markov et du calcul de probabilités sur un graphe donné. <br />
Ne pas utiliser de morceaux de code pour expliquer. <br />
Pypy. <br />
Cython. <br />
<br />
Faire évoluer n entre 100 et ... (trouver la valeur limite d'exécution). <br />
Permettre de vérifier la formule de mispredictions théorique. <br />
Essayer de concaténer le code des calculs de mispredictions. <br />
Idée : Essayer de faire une fonction qui prend la comparaison et effectue le reste des opérations en interne. <br />
<br />
Refaire l'isomorphisme des graphes (parcours à changer et plus de set de sets). <br />
Changer les calculs d'intégrales (quadrature scipy) <br />
https://www.southampton.ac.uk/~fangohr/teaching/python/book/html/16-scipy.html <br />
https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simpson.html <br />
Retravailler sur le papier. <br />
<br />
Exemple LaTeX : <br />
\begin{equation}\label{eq:expr_x}
x = \int_{0}^{1} ((1-p)*(1-p))\, dp = 0.33333
\end{equation}
\begin{equation}
y = \int_{0}^{1} ((1-p)*p)\, dp = 0.16667
\end{equation}
                

