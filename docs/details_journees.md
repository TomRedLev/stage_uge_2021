# Détails des journées :

## Lundi 26 Avril 2021 :
Lecture de Hennessy Patterson - Computer Architecture (100 pages). <br />
Lecture de la page Wikipédia sur les Chaînes de Markov + reprise du cours de compression. <br />
Mise en place des graphes pour l'exercice demandé. <br />
<br />

## Mardi 27 Avril 2021 :
Lecture et travaux pratiques autour de l'article "Good Predictions are Worth a Few Comparisons". <br />
Lecture de Digital Design (100 pages). <br />
<br />

## Mercredi 28 Avril 2021 :
Génération des graphes à 4 états pour l'exercice demandé. <br />
Continuation de la lecture de l'article "Good Predictions are Worth a Few Comparisons". <br />
Tentative d'installation de PAPI (grand raté, autre programme existant avec le même nom mais étant destiné à réaliser des études astronomiques). <br />
<br />

## Jeudi 29 Avril 2021 :
Fin de lecture détaillée de l'article "Good Predictions are Worth a Few Comparisons". <br />
Continuation de la création des graphes. <br />
<br />

## Vendredi 30 Avril 2021 :
Reprise depuis le début du code de création des graphes à k-états fortement connexes. <br />
Lecture de "Analysis of The OGeometric". <br />
<br />

## Lundi 03 Mai 2021 :
Implémentation des probabilités sur les arêtes des graphes. <br />
Relecture de "Analysis of The OGeometric". <br />
Lecture de Digital Design (100 pages). <br />
<br />

## Mardi 04 Mai 2021 :
Implémetation des calculs de probabilités stationnaires sur les graphes (Temps avec print des stats pour les graphes à 4 états = 686 secondes, soit 11 minutes, 620 secondes sans les prints, sûrement améliorable). <br />
Lecture de Hennessy Patterson - Computer Architecture (100 pages). <br />
<br />

## Mercredi 05 Mai 2021 :
Tentative d'amélioration des performances du programme de génération de graphes. <br />
Lecture de "A survey of Techniques for Dynamic Branch Prediction". <br />
<br />

## Jeudi 06 Mai 2021 :
Tentative d'amélioration des performances du programme de génération de graphes. <br />
Lecture de "A survey of Techniques for Dynamic Branch Prediction". <br />
<br />

## Vendredi 07 Mai 2021 :
La variable p est maintenant une variable non fixée dans la construction de graphes. <br />
Relecture de "A survey of Techniques for Dynamic Branch Prediction". <br />
<br />

## Lundi 10 Mai 2021 :
Tentative d'amélioration des performances des tests de probabilités stationnaires. <br />
Lecture  de Hennessy Patterson - Computer Architecture (100 pages). <br />
<br />

## Mardi 11 Mai 2021 :
Essai de transformation des équations pour toutes les écrires en fonction de p. <br />
Il me reste à trouver comment savoir si une variable est utilisée dans une équation. <br />
Lecture de Digital Design (100 pages). <br />
<br />

## Mercredi 12 Mai 2021 :
Expressions de toutes les variables en fonction de p. <br />
Lecture de Hennessy Patterson - Computer Architecture (100 pages). <br />
<br />

## Vendredi 14 Mai 2021 :
Tentative d'améliorer les performances du programme, devenu très lent depuis le calcul des mispredictions.<br />
Lecture de Hennessy Patterson - Computer Architecture (100 pages). <br />
<br />

## Lundi 17 Mai 2021 :
Ecriture des exemples : dichotomie, exponentiation rapide, MinMax.<br />
Utilisation de ces exemples avec l'implémentation d'un prédicteur de branchements à 4 états saturé. <br />
Lecture de plusieurs documents sur des versions des algorithmes sus-nommés. <br />
<br />

## Mardi 18 Mai 2021 :
Correction de divers bugs dans les exemples. <br />
Ajout de la détermination des statuts des états. <br />
Participation au séminaire du laboratoire. <br />
<br />

## Mercredi 19 Mai 2021 :
Tentative de compréhension de la diminution du nombre de graphes dont on peut déterminer les statuts des états. <br />
Correction des bugs dans "4graphs" (Mauvais calcul des intégrales). <br />
Début de la lecture pour implémenter la recherche d'isomorphisme entre les graphes. <br />
<br />

## Jeudi 20 Mai 2021 :
Implémentation de la vérification de l'isomorphisme entre deux matrices d'adjacence. <br />
Tentative d'amélioration du code et de l'exécution. <br />
Bug persistant sur le 21ème graphe à 4 états. <br />
<br />

## Vendredi 21 Mai 2021 : 
Tentative d'implémentation de linsolve et de réparation du bug lors des calculs d'intégrales. <br />
Je n'ai pas trouvé de solution pour l'instant. <br />
Lecture de diverses documentations. <br />
Lecture de Hennessy Patterson - Computer Architecture (100 pages). <br />
<br />

## Lundi 24 Mai 2021 : 
Tentative de réparation du bug lors des calculs d'intégrales. <br />
J'ai commencé à étudier les calculs numériques d'intégrales. <br />
Lecture de diverses documentations. <br />
<br />

## Mardi 25 Mai 2021 : 
Implémentation d'une solution pour le problème des calculs d'intégrales en utilisant la formule de Simpson. <br />
cf. https://fr.wikipedia.org/wiki/Calcul_num%C3%A9rique_d%27une_int%C3%A9grale#Formules_simples <br />
Améliorations de l'exécution du programme avec cython. <br />
<br />

## Mercredi 26 Mai 2021 :
Implémentation de l'utilisation de Graphviz. <br />
Optimisation de la lisibilité et de l'utilisation de ce dernier. <br />
Relecture des notes pour commencer à préparer le rapport. <br />
<br />

## Jeudi 27 Mai 2021 : 
Tentative d'installation de pypy. <br />
Commencement de la rédaction du rapport de projet. <br />
Rapport disponible au lien suivant : https://fr.overleaf.com/4273838755yzqfhqtpzdkt <br />
Lecture de documentation Cython. <br />
<br />

## Vendredi 28 Mai 2021 :
Continuation de l'écriture du rapport de projet. <br />
Lecture de documentation Cython et Pypy et petits tests effectués. <br />
<br />

## Lundi 31 Mai 2021 :
Tentative d'installation de pypy. <br />
Article le plus intéressant même si Mac pas M1 et pas sous Big Sur.
https://stackoverflow.com/questions/65336789/numpy-build-fail-in-m1-big-sur-11-1 <br />
Le problème d'installationsemble être un problème de compatibilité entre Pypy et Numpy. <br />
Trouvé une solution : installation très simple via Ubuntu. <br />
Envisager de passer en single boot Ubuntu. <br />
https://doc.ubuntu-fr.org/installation_macbook_sans_macosx <br />

## Mardi 01 Juin 2021 :
Installation en single boot Ubuntu. <br />
Installation de tous les packages nécessaires au bon fonctionnement des tests et du programme principal. <br />
Résolution de divers problèmes (Audio, WiFi, ...) <br />
Microphone ne marche pas avant la réunion. <br />
Tentative de correction de la commande dot pour générer le pdf, qui ne marche plus. <br />
<br />

## Mercredi 02 Juin 2021 :
Recherhe et implémentation de l'algorithme pour générer de façon plus optimale les graphes.<br />
Recherche de l'algorithme de parcours en profondeur dans des matrices d'adjacence.<br />
Recherche du fonctionnement des étiquettes liées aux états.<br />
<br />

## Jeudi 03 Juin 2021 :
Recherche et implémentation de l'algorithme de parcours en profondeur dans des matrices d'adjacence.<br />
Travail sur les divers exemples + lecture pour l'implémentation. <br />
Installation de PAPI. <br />
<br />

## Vendredi 04 Juin 2021 :
Réflexion sur la perte de précisions des graphes à 2 états. <br />
L'isomorphisme coupe bien plus de graphes et je ne comprends pas d'où cela vient
. <br />
Cela n'est pas dérengeant pour les graphes à 3/4 états mais bien plus pour les g
raphes à 2 états, où je ne trouve plus la solution optimale, mais seulement deux
 solutions sous optimales. <br />
Je vais continuer à réfléchir sur la manière d'implémenter tout cela. <br />
(J'envisage peut-être de rajouter mon ancienne solution d'isomorphisme pour les
graphes < à 3 états mais cela est peut-être inutile. <br />
<br />

## Lundi 07 Juin 2021 :
Correction de divers problèmes dans le programme principal de génération des graphes. <br />
Tentative de nouvelles implémentations pour les exemples donnés. <br />
<br />

## Mardi 08 Juin 2021 :
Implémentations de l'exemple MinMax. <br />
Création des structures de graphes et d'états en C. <br />
Implémentation de ces structures dans l'exemple cité précédemment. <br />
<br />

## Mercredi 09 Juin 2021 :
Tentative d'amélioration de la détermination des graphes isomorphes. <br />
Implémentation du set de sets avec les frozensets. <br />
J'ai l'impression d'évacuer encore trop de graphes, en observant les graphes à 2 états et en ne trouvant toujours pas les solutions optimales dans les graphes retenus. <br />
Cependant, j'en obtiens tout de même beaucoup plus. Je vais continuer à réfléchir sur la question. <br />

## Jeudi 10 Juin 2021 : 
J'ai peut-être trouvé une solution au fait d'avoir des solutions manquantes lors de la génération des graphes à 2 états. Je pense en obtenir un peu trop désormais, mais cela me semble moins dérengeant que ne pas obtenir de solutions du tout pour k = 2. <br />
Pour k = 4, le programme s'exécute en 277 secondes. <br />
On obtient un nombre de 3695 solutions optimales pour les graphes à 4 états. <br />
On peut obtenir des graphes proches du compteur saturé à 2 bits. <br />
Exemple : Graphe 2560 (p1692), 4643(p113), 4636 (p107), 4983 (p304), 7623(p1284) <br />
Je n'ai cependant pas trouvé le compteur saturé en lui-même. <br />

## Vendredi 11 Juin 2021 : 
Amélioration et études des problèmes liés au programme de génération des graphes. <br />
Détection du problème d'isomorphisme du compteur saturé à 2 bits. <br />
Tentative de patch du bug infructueuse. <br />
Amélioration des structures pour les exemples MinMax donné. <br />
<br />

## Lundi 14 Juin 2021 : 
Amélioration et études des problèmes liés au programme de génération des graphes. <br />
Réécriture de la détection du problème d'isomorphisme du compteur saturé à 2 bits. <br />
Correction du bug, on peut voir les compteurs saturés aux graphes suivants : <br />
iso counter not isomorph 2734 <br />
iso counter not isomorph 4643 <br />
iso counter not isomorph 4803 <br />
iso counter not isomorph 7623 <br />
Assister au séminaire. <br />
<br />

## Mardi 15 Juin 2021 : 
Tentative de compréhension des résultats obtenus sur les graphes non isomorphes, qui
ressemblent à des compteurs saturés à 2 bits (calculs réalisés et vérifiés à la main). <br />
Revérification que le code suit bien la méthodologie et les calculs établis. <br />
Assister au séminaire. <br />
<br />

## Mercredi 16 Juin 2021 : 
Résolution du problème de mauvaises précisions des calculs, qui empéchait d'obtenir des résultats cohérents et réels pour les compteurs à 2 bits saturés. <br />
Solution temporaire établie. <br />
Tentative de solution plus globale, pas encore trouvée. <br />
<br />

## Jeudi 17 Juin 2021 : 
Tentative de solution plus globale, pas encore trouvée, mais je pense avoir une bonne piste pour trouver comment réaliser ces calculs et obtenir les mêmes résultats que ceux obtenus lors des calculs à la main. <br />
Assister au séminaire. <br />
<br />

## Vendredi 18 Juin 2021 : 
Correction des divers problèmes établis hier. <br />
Etablissement d'une nouvelle méthode de détection des isomorphismes. <br />
Rework complet de cet aspect. <br />
Utilisation de Scipy pour les calculs d'intégrales. <br />
Cela semble très bien fonctionner et on obtient un gros gain de performance et de propreté de code. <br />
<br />

## Lundi 21 Juin 2021 : 
Tentative d'améliorations des dernières implémentations. <br />
Patch de certains bugs. <br />
Rendre le code un peu plus propre. <br />
Travailler sur le compte-rendu. <br />
<br />

## Mardi 22 Juin 2021 : 
Tentative d'améliorations des performances générales du programme. <br />
Impossible d'installer scipy sur pypy3. <br />
Je tenterais de le refaire. <br />
Retravailler le compte-rendu et essayer de détailler un peu plus les explications. <br />
<br />

## Mercredi 23 Juin 2021 : 
Tentative d'améliorations des performances générales du programme. <br />
Installation de numba, aucune performance améliorée. <br />
Retravailler le compte-rendu et essayer de reformuler les phrases lourdes. <br />
<br />

## Jeudi 24 Juin 2021 :
Retravail de la structure de graphes dans PredictorsImplementation. <br />
Tentative de dé-enlacer encore plus l'avancement de la structure avec le code basique. <br />
Retravail du compte-rendu. <br />
<br />

## Vendredi 25 Juin 2021 :
Retravailler les sources du "projet" PredictorsImplementation. <br />
Nouvelle tentative de dé-enlacer encore plus l'avancement de la structure avec le code basique. <br />
Je pense avoir trouvé une bonne solution. <br />
Je vais tenter de passer tout mon code en python pour simplifier l'utilisation et la compréhension, ainsi que pour n'avoir plus qu'un unique langage de programmation pour le stage. <br />
Le C aura été utile pour générer facilement les codes en assembleur. <br />
Tentative d'améliorations des performances générales du programme. <br />
Retravail du compte-rendu. <br />
<br />

## Lundi 28 Juin 2021 :
Tentative d'optimisations sur les divers programmes avec des outils extérieurs. <br />
Tests sur l'utilisation de la librairie PAPI. <br />
Relecture et réécriture de certaines parties du compte-rendu. <br />
<br />

## Mardi 29 Juin 2021 :
Ajout de nouvelles sections dans le compte-rendu. <br />
Retravail de certaines parties du compte-rendu. <br />
Tentative de réinstallation de Pypy. <br />
<br />

## Mercredi 30 Juin 2021 :
Ajout de définitions, d'exemples et de propositions dans le compte-rendu. <br />
Restructuration de certaines parties du document. <br />
Mise en place de la prise en charge des solutions optimales et des solutions presques optimales. <br />
J'ai une autre idée pour cette prise en charge, faire une liste, la trier et ne prendre que les éléments jusqu'à un certain score. <br />
Cela permettrait d'éviter certaines pertes. <br />
Mise en place du dessin de graphes de Matplotlib pour les exemples. <br />
<br />

## Jeudi 1 Juillet 2021 :
Travail sur le compte-rendu. <br />
Reformulation de plusieurs parties. <br />
Ajout de définitions et de propositions. <br />
Ajout des sites visités et des dates. <br />
Retravail sur Matplotlib. <br />
<br />

## Vendredi 2 Juillet 2021 :
Travail sur le compte-rendu. <br />
Reformulation de plusieurs parties. <br />
Ajout de définitions et de propositions. <br />
Ajout de sites visités et des dates. <br />
Retravail de l'implémentation de la détection des solutions optimales. <br />
<br />

## Lundi 5 Juillet 2021 :
Travail sur le compte-rendu. <br />
Retravail de certaines parties, reformulation, réécriture, reprécisions, ... <br />
Finalisation de l'implémentation de la détection des solutions optimales. <br />
Re-split des fonctions dessinées via Matplotlib. <br />
Les mispredictions et les comparaisons sont dans deux fichiers différents à partir de maintenant pour pouvoir les comparer facilement aux valeurs théoriques. <br />
<br />
<br />

