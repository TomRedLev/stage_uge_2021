# Notes de lecture :

## Good Predictions Are Worth A Few Comparisons :

Processeurs modernes -> paralélisés et utilise les producteurs pour deviner les sorties des branchements conditionnels. <br />
<br />
Etudes de deux algorithmes : exponentiation rapide et la recherche dichotomique dans un tableau trié.
Ces deux algos sont codés dans une façon que les misspredictions soient moins nombreuses, cependant cela augmente le nombre d'opérations. <br />
<br />
Implémentations des deux algos en version récursive Python dans pw/GoodPredictions. <br />
<br />
Exemple d'introduction : <br />
But - Chercher le minimum et le maximum <br />
Approche naïve - 2n comparaisons | Approche optimale - 3n / 2 comparaisons <br />
Seulement, l'implémentation naïve est deux fois plus rapide. <br />
Une des raisons simples pourrait être - Difference dans le nombre de cache misses. <br />
Les deux implémentations font cependant les mêmes accès mémoires, dans le même ordre. <br />
<br />
A chaque conditionnelle dans un programme, il y a un mécanisme (le prédicteur) qui essaye de deviner si le saut conditionnel va être pris ou non. <br />
Le coût de la missprediction doit être pris en compte, car il peut être assez élevé. <br />
Peut expliquer l'attitude des algorithmes utilisants des comparaisons. <br />
<br />
L'exemple d'introduction est assez marquant au vu du fait que la différence entre les deux implémentations est une branche conditionnelle qui est imprévisible (input pris au hasard, uniformément) et cela va donc augmenter le nombre de misspredictions. <br />
<br />
Misspredictions pour la version naïve :  O(log(n)) <br />
Misspredictions pour la version optimale : ![e2](http://www.sciweavers.org/free-online-latex-equation-editor) <br />







