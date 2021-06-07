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




