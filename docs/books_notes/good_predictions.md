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
mispredictions pour la version naïve :  ![thetaresult](https://bit.ly/2Sayh4x) <br />
mispredictions pour la version optimale : ![thetaresult](https://bit.ly/3gPQDlx) <br />
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

## 4 - Exponentiation rapide :

Les branches conditionnelles qui ont autant de chance d'être prises ou non sont très douloureuses pour l'utilisation des prédictions de branchements. <br />
Quelques algos "diviser pour régner" utilisent de telles branches, car ils essayent d'avoir des parts égales pour atteindre une complexité optimale. <br />
Deux façons de disrupter la balance pour finir avec de meilleures performances sur deux algos classiques. <br />

### 4.1 - Algorithmes modifiés :
Les premiers tests de modifications d'algorithmes ont conduit à une réécriture de l'exponentiation rapide, cependant il restait toujours des branchements conditionnels qui possédaient une probabilité de 2 et qui ont pu être modifié en s'intéressant aux deux derniers bits de n. <br />
On peut rajouter des conditions qui ne sont pas obligatoirement nécessaires, mais qui permettent d'obtenir des probabilités de branchements différentes de 1/2. <br />
Expérience : Pour comparer les expériences, la valeur flottante de x^n en utilisant chaque algorithme 5.10^7 périodes, avec n choisi uniformément entre 0 et 2^26 - 1. <br />
Temps d'exécutions et autres paramètres (nombre de mispredictions) mesurés avec la librairie PAPI. <br />
<br />
Différence de vitesse : <br />
GuidedPow > 14% > UnrolledPow <br />
GuidedPow > 29% > ClassicalPow <br />
Le nombre de multiplications est relativement le même entre les 3 algorithmes. <br />
L'explication principale pour la différence de vitesse entre UnrolledPow et ClassicalPow : le nombre de boucles est divisé par 2.<br />
Entre GuidedPow et UnrolledPow : le nombre de boucles est le même, et UnrolledPow utilise 25% en plus de comparaisons. La différence principale est le test "if (n & 3)" qui enlève un quart des mispredictions. <br />
Le test cause des mispredictions supplémentaires mais comme il modifie les probabilités de prédictions des deux autres tests, ce qui entraîne une diminution finale du nombre de mispredictions. <br />
Encore une fois le nombre augmenté de comparaisons est équilibré par le moins grand nombre de mispredictions. <br />
<br />

### 4.2 - Analyse du nombre moyen de mispredictions pour GuidedPow :
Pour l'analyse, on considère que n est pris uniformément  entre 0 et N-1, avec N=4^k et k >= 1. <br />
Considérations des prédicteurs locaux. <br />
<br />
Lk(n) = nombre d'itérations de boucle dans GuidedPow. <br />
==> { Lk(n) = l | 4^l > n } <br />
E[Lk] = k - 1/3 + o(1) ~ k. <br />
<br />
Les chaînes de Markov sont des outils principaux pour ce genre d'analyse. <br />
A chaque itération, la condition est vraie avec une probabilité de 3/4, comme elle  n'est pas satisfaite si les deux derniers bits sont 00. <br />
On peut donc associer aux arêtes "Taken" la probabilité 3/4 et "Not Taken" la probabilité 1/4. <br />
Une misprediction arrive lorsque une arête marqué comme Taken est utilisé depuis un état qui prédit Not Taken. <br />
Il faut aussi connaître l'état de départ du prédicteur, mais cela n'a pas d'influence sur les résultats asymptotiques. <br />
Le problème a été réduit au fait de compter le nombres de fois que certaines arêtes soient prisent dans la chaîne de Markov, en faisant un parcours aléatoire de longueur aléatoire Lk. <br />
<br />
Théorème ergodique : <br />
Considérons (M, Pi0) une chaîne primitive et apériodique de Markov sur un ensemble fini S.
Pi est une distribution stationnaire. <br />
E est l'ensemble d'arêtes de M, qui est un ensemble de paires (i, j) appartenant à S^2 tel que M(i, j) > 0. <br />
Pour n un nombre entier supérieur ou égal à 0, Ln est une variable aléatoire sur les nombres entiers supérieurs ou égaux à 0, tels que la limite de n tend vers 0 est E[Ln] = +inf. <br />
Xn est une variable aléatoire qui compte le nombre d'arêtes dans E qui sont utilisés pendant un parcours aléatoire de longueur Ln dans M (en commençant de la distribution initiale Pi0. <br />
L'équivalence asymptotique est donc : E[Xn] ~E[Ln] * (sum(Pi(i)) pour (i, j) appartenant à E ) * M(i,j). <br />
<br />
En considérant un prédicteur donné, dans lequel la condition est satisfaite avec une probabilité p. <br />
On définit par Mp, la matrice de transition, par Pip le vecteur stationnaire et par Mu(p) la probabilité attendue de mispredictions définie par Mu(p) = (sum(Pip(i)) pour i, j appartenant à E) * M(i, j) où E est un ensemble d'arêtes correspondantes aux mispredictions. <br />
Le théorème est établi pour des valeurs de N qui ne sont pas des puissances de 4, ce qui est plus compliqué car les bits ne sont pas exactement 0 et 1 avec des probabilités de 1/2. <br />
<br />
Théorème 3 : <br />
N est pris uniformèment entre {0, ..., N - 1}. <br />
Le nombre de tests conditionnels dans ClassicalPow et UnrolledPow est asymptotiquement équivalent log(2, N) <br />
Le nombre de tests conditionnels dans GuidedPow est asymptotiquement équivalent à 5/4 log(2,N). <br />
Le nombre espéré de mispredictions est asymptotiquement équivalent à 1/2 log(2, N) pour ClassicalPow et UnrolledPow. <br />
Le nombre espéré de mispredictions est asymptotiquement équivalent à (1/2 Mu(3/4) + 3/4 Mu(2/3)) log(2, N) pour GuidedPow. <br />
Mu est la probabilité de mispredicitons espérés associé au prédicteur local. <br />
<br />
Alpha = (1/2 Mu(3/4) + 3/4 Mu(2/3)) <br />
=> 25/48 (1-bit) <br />
=> 9/20 (2-bit compteur saturé) <br />
=> 2045/4368 (2-bit flip-on-consecutive) <br />
=> 1095/2788 (3-bit compteur saturé) <br />
<br />
On peut comparer ces valeurs au 1/2 des deux autres algorithmes. <br />
En particulier, pour le prédicteur 1-bit, le nombre espéré de mispredictions est plus grand pour GuidedPow que pour ClassicalPow ou UnrolledPow. <br />
Le prédicteur n'est donc pas suffisamment performant pour compenser les mispredictions causées par la conditionnelle ajoutée. <br />
Pour le compteur saturé à 3-bit, GuidedPow utilise 0.25 log(2, N) comparaisons de plus que UnrolledPow, mais 0.11 log(2,N) mispredictions de moins. <br />
<br />

## 5 - Recherche binaire et variantes :

### 5.1 - Déséquilibrer la recherche binaire :
Considération de la recherche binaire classique. <br />
Pour éviter la partition en 2 parties, qui donnerait une probabilité de 1/2 pour la branche conditionnelle, alors il y aurait la possibilité de faire une partition en 4 parties. <br />
En continuant avec la méthode "diviser pour conquérir", on peut obtenir une recherche ternaire en partitionnant par 3 parties. <br />
Le principal problème avec cette approche est que la division par 3 est couteuse en terme d'hardware. <br />
Pour limiter ce coût, il aura été nécessaire de créer deux parties de taille n/4 et une partie de taille n/2,
car l'on utilise que des divisions par des puissances de 2 qui sont de simples shifts binaires, comme dans la recherche binaire standard. <br />
<br />

### 5.2 - Experiences :
La recherche binaire biaisé marche mieux que la recherche binaire classique et la recherche faussée encore mieux. <br />
Contrairement aux exemples précédents, les changements faits sont un peu plus sensibles aux effets de cache (à cause de la façon de partitionner le tableau, qui influence donc la position à laquelle on peut accéder à la mémoire). <br />
Cela a mené à faire des expériences sur des tableaux qui se glissent dans le dernier niveau de cache de la machine pour mesurer les effets des prédictions de branchements. <br />
Pour les tableaux de taille intermédiaire, la recherche fausée est plus rapide de 23% que la recherche binaire classique (Les programmes sont compilés sans optimisations de gcc). <br />
Les expériences menées en Java, utilisant une librairie dédiée au micro-benchmarking donne relativement les même résultats (avec une accélération moins rapide de 12%), en comparant la recherche faussée à la recherche binaire écrite dans la librairie standard. <br />
<br />

### 5.3 - Analyse des Prédicteurs Locaux :
Utilisation du théorème ergodique pour obtenir une bonne courbe asymptotique estimant le nombre de mispredictions. <br />
Il faut aussi obtenir le nombre de fois que chaque conditionnelle est réalisée. <br />
Une estimation du premier ordre sur le nombre de fois qu'une conditionnelle donnée est exécuté peut être réalisée en utilisant le théorème Maître de Roura. <br />
<br />
Théorème Maître : <br />
Considérons k >= 1, et a1, ..., ak, ainsi que b1, ..., bk des entiers positifs réels, tels que sum(ai) = 1 pour i allant de 1à k. <br />
Pour chaque i appartenant à {1, ..., k}, on peut aussi dire que Ei(n) est une suite réelle telle que : bi*n + Ei(n) est un entier positif et Ei(n) = O(1/n). <br />
T(n) est la séquence d'entier réel qui satisfait, pour deux constantes positives c et d : <br />
T(0) = c et T(n) = d + (sum(ai) pour i allant de 1 à k) * T(bi*n + Ei(n)) + O(log(n) / n) pour n >= 1. <br />
Alors T(n) ~d/h log(n) avec h = - (sum(ai) pour i allant de 1 à k) * log(bi) <br />
<br />
Description des étapes de l'analyse de l'algorithme BiasedBinarySearch : <br />
L(n) = 1 + an / (n +1) * L(an) + bn / (n + 1) L(bn), avec an = floor(n/4) + 1 et bn = ceil(3n/4) et L(0) = 0. <br />
L(n) ~ lambda * log(n) avec lambda = 4/(4 log(4) - 3 log(3)) ± 1.78. <br />
<br />
Il est impossible de transformer le prédicteur en chaîne de Markov, car la probabilité an / (n + 1) et bn / (n + 1) ne sont plus fixées (elles dépendent de n). <br />
En considérant, an/(n+1) = 1/4 + O(1/n) et bn/(n + 1) = 3/4 + O(1/n), cette chaîne de Markov devrait fournir une bonne approximation du nombre de mispredictions avec le théorème ergodique. <br />
Une manière simple de prouver cela formellement est d'utiliser un arbre de décomposition T associé aux algorithmes de recherche. <br />
Si l'entrée est de taille n, alors sa racine est labelisée (0, n) et chaque noeud correspond à une valeur possible de d et f pendant une boucle de l'algorithme. Les feuilles sont les paires (i,i) pour i appartenant à {0, ..., n}, ils sont identifiés avec la sortie de l'algorithme en {0, ..., n}. <br />
Il y a une arête directe entre (d, f) et (d', f') chaque fois que les variables d et f peuvent être modifiéesd en d' et f' pendant l'itération courante de la boucle. <br />
Une telle arête est labélisée avec la probabilité que cette mise à jour puisse arriver dans le modèle : ((f' - d' + 1) / (f - d + 1)) <br />
Par construction suivre un chemin de puis la racine jusqu'à une feuille, en choississant à droite ou à gauche en observant les probabilités des arêtes est exactement la même chose que choisir un entier uniformément de façon aléatoire entre {0, ..., n}. <br />
u = (u0, u1, ...) est une suite infinie d'éléments de [0, 1] pris aléatoirement uniformément et indépendamment. <br />
On associe à U le Pathn(T, u) en T, où, à chaque étape i, on peut aller à gauche si ui est plus petit que la probabilité d'arête vers le fils gauche et à la droite sinon. <br />
Ln(T,u) est la longueur de Pathn(T,u) et Pathn(I, u) est le chemin qui suit les valeurs de u dans un arbre infini idéal I où l'on va à gauche avec une probabilité de 1/4 et à droite avec une probabilité de 3/4. <br />
<br />
Lemme 5 : La probabilité que Pathn(T, u) et Pathn(I, u) diffèrent à l'une des (Ln(T, u) - sqrt(log(n))) étapes est de O(1/log(n)). <br />
<br />
L'algorithme BiasedBinarySearch fonctionne presque de la façon idéale, pour la plupart des itérations dans la boucle principale, et l'estimation en terme d'erreur est assez précise. <br />
Ceci est suffisant pour prouver que la version idéale est une approximation correcte du premier ordre du nombre de mispredictions. <br />
La même construction est réalisée pour les trois algorithmes. <br />
Avec un compteur saturé à 2-bit, on a Mu(1/4) = 3/10 et Mu(1/3) = 2/5, soit E[Cn] / log(n) et E[Mn] / log(n) est autour de : <br />
BinarySearch : 1.44, 0.72 <br />
BiasedBinarySearch : 1.78, 0.53 <br />
SkewSearch : 1.68, 0.58 <br />
<br />
Cn et Mn sont les nombres de comparaisons et de mispredictions réalisées dans le modèle établi : <br />
BinarySearch : E[Cn] = log(n) / log(2) ; E[Mn] = log(n)/(2 log(2)) <br />
BiasedBinarySearch : E[Cn] = 4 * log(n) / (4 log(4) - 3 log(3)) ; E[Mn] = Mu(1/4) * E[Cn] <br />
SkewSearch : E[Cn] = 7 * log(n) / (6 log(2)); <br />
<br />

### Analyse du prédicteur global de SkewSearch :

Le prédicteur de chaque entrée est un compteur saturé à 2-bits. <br />
Ce n'est pas le seul choix possible en tant que prédicteur global, mais il est assez simple sans être trivial. <br />
L'analyse est menée dans un framework idéalisé pour ressembler au vrai cas, tout en évitant les effets dûs aux nombres entiers. <br />
Seule considération des suites de Taken/Not Taken produites par les deux tests conditionnels de SkewSearch. <br />
On ne considère pas le test du while, car il ne sera pris que dans la dernière étape (et cela complexifierait le prédicteur sans ajouter d'informations utiles). <br />
Une trace de l'exécution de l'algorithme sera un mot non-vide de l'alphabet {0, 1}. <br />
Considération possible avec l'automate Aif, main => pris avec une probabilité de 1/4 et nested avec une probabilité de 1/3. <br />
L'automate se transforme facilement en chaîne de Markov en utilisant les probabilités de transition.
Le vecteur stationnaire Piif satisfait : Piif(main) = 4/7 et Piif(nested) = 3/7. <br />
<br />
Dans la table globale, seul est enregistré les historiques des conditionnelles main et nested. <br />
l représente la longueur de l'historique (un nombre de bits pair). <br />
Un historique h est comme un mot binaire de longueur l. <br />
0^l est l'historique fait de 0 seulement. <br />
<br />
Quand une conditionnelle est testé à un moment t, le prédicteur utilise l'entrée à la position h[t] pour faire sa prédiction. <br />
Pour suivre l'évolution à un temps t + 1, on peut uniquement garder la traque de la table d'historique Tt, l'historique courant et quelle conditionnelle IFt est étudiée. <br />
Garder IFt est essentiel pour pouvoir calculer la probabilité de la prochaine sortie (0 ou 1). <br />
On peut en déduire une chaîne de Markov (Mup) pour les mises à jour dans l'historique. <br />
Depuis Mup, on peut théoriquement estimé le nombre de mispredictions. <br />
Problème : Piup = O(m^3) avec m le nombre d'états de Mup, et le nombre d'états est exponentiel en l, même en retirant les états non-atteints. <br />
h appartient à B^l un historique qui n'est pas égal à 0^l. Il y a au moins un 1 dans h. <br />
Comme lire un 1 envoie toujours dans l'état main de l'automate Aif, on sait que la condition IFt observé vient d'ajouter une occurence de h au moment t. <br />
On sait donc que la probabilité d'avoir un 0 ou un 1 à t+1, sachant que ht = h. <br />
Chaque entrée de h ≠ 0^l dans la table T agit comme un compteur saturé à 2-bits ayant ses probabilités fixées, telles qu'il y a une probabilité de 1/4 pour les historiques associés au main et 1/3 pour les historiques associés à nested. <br />
h = 0^l concentre toutes les différences entre les prédicteurs globaux et locaux. <br />
Ce qui arrive pour l'entrée 0^l est bien décrite par l'automate de paires (s,i) où s est un état du prédicteur et i la condition courante. Cet automate peut être transformé en chaîne de Markov, et le théorème ergodique permet d'obtenir une estimation précise du nombre de mispredictions. <br />
<br />
Le nombre moyen de mispredictions provoquées pendant l'exécution de SkewSearch dans un tableau de taille n donné en entrée est asymptotiquement équivalent à (12/35 + 1/(592*2^l)) * E[Cn]. <br />
<br />
D'après le théorème 6, avec l'utilisation d'un predicteur à 2-bit local à chaque condition, le nombre de mispredictions est asymptotiquement équivalent à 12/35 E[Cn]. <br />
La différence entre le prédicteur global est vraiment très petite, ce qui n'est pas surprenant car il n'y a une différence que lorsque l'historique est 0^l. <br />
S'il y avait une compétition entre le prédicteur global et un prédicteur local plus précis (Ex : compteur saturé à 3-bit), le prédicteur local obtiendrait de meilleures performances. <br />
Cela peut être un peu perturbé par le producteur global car le selecteur dynamique qui choisit entre les 2 peut choisir le prédicteur global des fois. <br />
<br />

## 6 - Conclusion :
Propositions de versions déséquilibrées predictor-friendly de deux algorithmes classiques (Exponentiation rapide et recherche binaire). <br />
En utilisant une estimation précise du nombre attendu de mispredictions, cela a pu montrer que les algorithmes proposés dans cet article sont intéressant à considérer lorsque le coût de comparaison est raisonnable comparé au coût de misprediction. C'est le cas pour les structures de données primaires. <br />
Ces résultats théoriques, soutenu par des expériences, montre qu'il est intéressant de s'intéresser plus particulièrement à cette fonctionnalité dans les ordinateurs modernes pour la construction et l'analyse d'algorithmes. <br />
Prendre les branches de prédictions en compte peuvent amener à des améliorations remarquables, même sur des algorithmes classiques. <br />
<br />
