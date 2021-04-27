# Notes de lecture :

## Good Predictions Are Worth A Few Comparisons :

Processeurs modernes -> paralélisés et utilise les producteurs pour deviner les sorties des branchements conditionnels.

Etudes de deux algorithmes : exponentiation rapide et la recherche dichotomique dans un tableau trié.
Ces deux algos sont codés dans une façon que les misspredictions soient moins nombreuses, cependant cela augmente le nombre d'opérations.

Implémentations des deux algos en version récursive Python dans pw/GoodPredictions.

Exemple d'introduction :
But - Chercher le minimum et le maximum
Approche naïve - 2n comparaisons | Approche optimale - 3n / 2 comparaisons
Seulement, l'implémentation naïve est deux fois plus rapide.
Une des raisons simple pourrait être - Difference dans le nombre de cache misses. 
Les deux implémentations font cependant les mêmes accès mémoires, dans le même ordre.






