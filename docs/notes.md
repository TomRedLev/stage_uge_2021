# Notes de lecture :

## Good Predictions Are Worth A Few Comparisons :

Processeurs modernes -> paralélisés et utilise les producteurs pour deviner les sorties des branchements conditionnels. <br />
<br />
Etudes de deux algorithmes : exponentiation rapide et la recherche dichotomique dans un tableau trié.
Ces deux algos sont codés dans une façon que les mispredictions soient moins nombreuses, cependant cela augmente le nombre d'opérations. <br />
<br />
Implémentations des deux algos en version récursive Python dans pw/GoodPredictions. <br />
<br />
Exemple d'introduction : <br />
But - Chercher le minimum et le maximum d'un tableau de taille n. <br />
Approche naïve - 2n comparaisons | Approche optimale - 3n / 2 comparaisons. <br />
Seulement, l'implémentation naïve est deux fois plus rapide. <br />
Une des raisons simples pourrait être - Difference dans le nombre de cache misses. <br />
Les deux implémentations font cependant les mêmes accès mémoires, dans le même ordre. <br />
<br />
A chaque conditionnelle dans un programme, il y a un mécanisme (le prédicteur) qui essaye de deviner si le saut conditionnel va être pris ou non. <br />
Le coût de la missprediction doit être pris en compte, car il peut être assez élevé. <br />
Peut expliquer l'attitude des algorithmes utilisants des comparaisons. <br />
<br />
L'exemple d'introduction est assez marquant au vu du fait que la différence entre les deux implémentations est une branche conditionnelle qui est imprévisible (input pris au hasard, uniformément) et cela va donc augmenter le nombre de mispredictions. <br />
<br />
mispredictions pour la version naïve :  ![thetaresult](http://www.sciweavers.org/tex2img.php?eq=%20%5CTheta%20%28log%28n%29%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0) <br />
mispredictions pour la version optimale : ![thetaresult](http://www.sciweavers.org/tex2img.php?eq=%20%5CTheta%20%28n%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0) <br />
Sujet déjà étudié pour observer le surcoût des mispredictions.<br />
Vision inverse, proposition d'algorithmes predictor-friendly (aider à éviter les mispredictions).<br />
<br />
Travail effectué : <br />
Version de l'exponentiation rapide avec moins de mispredictions, sans augmenter le nombre de multiplications. <br />
Analyse basée sur les chaînes de Markov qui décrivent les prédicteurs locaux (compteur saturé et flip-on-consecutive). <br />
Version de la recherche dichotomique sur un tableau trié. <br />
Première analyse d'un prédicteur global. <br />
Pour baisser les mispredictions : balance brisé de la méthode "diviser pour mieux régner". <br />
En pratique : troquer des comparaisons et des misspredictions premettent d'augmenter la vitesse d'exécution quand les comparaisons sont faites sur des types primitifs. <br />
<br />
Travaux liés : <br />
Biggar -> la réaction des branches pour des algorithmes de tri. <br />
Brodal, Fagerberg et Moruz -> Troque entre comparaisons et mispredictions sur des algorithmes de tri. <br />
Ces travaux ont ammenés à la première analyse théorique de prédicteurs de branchement statique. <br />






