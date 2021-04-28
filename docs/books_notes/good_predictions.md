# Good Predictions Are Worth A Few Comparisons :

## 1 - Introduction :

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
Sanders et Winkel ont considéré la possibilité de dissocier les comparaisons de leurs branches dans leur algorithme SampleSort, ce qui évite la plupart des coût de mispredictions. <br />
Elmasry, Katajainen and Stenmark ont proposés une version de MergeSort qui n'est pas impacté par les mispredictions en utilisant des instructions propres au processeur.<br />
Kaligosi et Sanders ont analysés des predictors dynamiques pour expliquer les mispredictions qui affectent les algorithmes classiques.
Martinez, Nebel et Wild ont précisé que cela n'était pas suffisant pour expliquer les meilleures performances obtenues avec la version à double pivot de QuickSort.
Brodal et Moruz ont conduit une étude sur les arbres binaires de recherche qui sont biaisés, pour montrer qu'ils pouvaient obtenir de meilleurs performances que des arbres bien équilibrés car les côuts de de branches n'étaient pas obligatoirement les mêmes, dûs aux plans de prédictions de branchements. <br />
<br />
Le travail effectué prend avantage des prédictions de branchements mais est plus lié aux algorithmes que sur les structures de données. <br />
<br />

### 2 - Éléments d'architecture matérielle : 

Pour éviter de bloquer le pipeline quand il faut étudier un saut conditionnel, le prédicteur de branchements essaye de prédire si le saut va s'effectuer ou non. <br />
Si la prédiction est bonne, cela ne ralentit pas le pipeline, alors que si elle est mauvaise, le pipeline est vidé et cela provoque donc une perte signifiante de performance. <br />
<br />
Plusieurs stratégies ont été établies : <br />
static branch predictor - Il ne se sert pas de l'exécution du code pour modifier son choix.<br />
dynamic branch predictor - Il va utiliser les résultats précédents pour déterminer si une certaine branche doit être prise ou non. <br />
<br />
Le 1-bit predictor ne se rappelle que du résultat précédent.<br />
Les 2-bit predictors esssayent d'éviter les mispredictions prennent un chemin inconnu.<br />
Le compteur saturé peut être amélioré (k-bit predictors utilisant 2^k états). <br />
Tous les prédicteurs sont locaux, il en existe un pour chaque conditionnel (Il y a une limite en réalité). <br />
<br />
Une table d'historique à 2^n entrées indexés par la séquence de leurs n dernières branches (1 pour pris, 0 sinon). <br />
Les entrées sont des k-bit predictors. <br />
Une table est locale si ses entrées correspondent au compertement d'une branche et sont utilisées pour cette branche précise.<br />
Une table est globale si toutes les sorties des précédentes branches sont utilisés pour indexer la table et sont partagés avec toutes les conditionnelles.<br />
<br />
Les corrrelating branch predictors se servent des informations locales et globales. <br />
Les tournament predictors utilise un programme dynamique pour décider s'il vaut mieux suivre les prédictions locales ou globales. <br />
Les mispredictions ne peuvent être observé que sur un code assembleur donné. <br />
Les études ont été réalisées sur du code C non-optimisé mais marche aussi sur du code complêtement optimisé. <br />
<br />

## 3 - Recherche du minimum et maximum de façon simultané :

Modèle de probabilité  : distribution aléatoire uniforme d'un tableau de taille n où chaque élément est choisi entre [0,1] de façon indépendante et uniforme.<br />
L'événement ayant une probabilité de 0 (les éléments de l'input ne sont pas identiques), cela revient à choisir au hasard une permutation entre de 1 à n, car seuls les éléments sont comparés dans les deux algorithmes. <br />
Min/max-record : c'est un élément dans un tableau ou une permutation qui est strictement plus petit/grand que tous les autres éléments à sa gauche. <br />
Le nombre de records dans une permutation est une statistique connue. <br />
<br />

### Première proposition : 

Le nombre espéré de mispredictions performé par NaiveMinmax dans un tableau de taille n, est équivalent à 4 log(n) pour le 1-bit predictor, 2log(n) pour les 2-bit predictor et 3-bit compteur saturé. <br />
3/2-Minmax est équivalent à n/4 + O(log(n)) pour tous les prédicteurs considérés. <br />
<br />
En observant ces résultats, le nombre de mispredictions dans NaiveMinmax est négligeable par rapport au nombre de comparaisons. <br />
Le test additionel utilisé pour optimiser 3/2-minmax provoque une augmentation des mispredictions qui deviennent comparables au nombre de comparaison. <br />
Les mispredictions provoquent des cycles CPU, alors que les comparaisons sont des opérations peu coûteuses. <br />
Il y a d'autres facteurs qui peuvent influer les performances de simples programmes, comme les effets de cache. <br />
Pour éviter cela, les éléments ont tous été accédé une seule fois et dans le même ordre. <br />
Utilisation de l'optimisation -O3 de GCC pour vérifier que ces résultats tiennent, même avec des optimisations de code. <br />
Avec cette optimisation, la branche dans 3/2-Minmax est remplacés par des mouvements conditionnels qui ne sont pas vulnérables à la misprediction, cependant il reste toujours 1/4n de mispredictions en moyenne. <br />
Ces résultats ne sont pas identiques si l'on considère une distribution non-uniforme. <br />
Il serait intéressant d'étudier le comportement des deux algorithmes sur des permutations aléatoires avec un nombre donné de records. <br />

## 4 - Exponentiation by Squaring :

