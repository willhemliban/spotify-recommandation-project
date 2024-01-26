Dans le cadre du module Technique d’Apprentissage Artificiel, nous devions réaliser unprojet d’apprentissage automatique. Pour ce faire nous avons décidé de réaliser unsystème de recommandation.

Problématique

Comment proposer à l’utilisateur de la musique qu’il aime?
Pour répondre à cette problématique, on réalise ce système de recommandation.

Méthodologie

Création de dataset

Tout d’abord on va créer 2 playlist l’une contenant la musique “aimé” et l’autre contenant la playlist “pas aimé”.
A l’aide de l’api spotify et de l’extension spotipy on récupère les 2 playlist. Tout d’abord on récupère les ID de chauqes chansons à l'aide desquelles on récupère les données de chaque titre (tempo, duration, danceability…).
Ensuite on réunit ces 2 playlists dans un seul data frame en y ajoutant un champ “liked” qui permet de savoir si la chanson a été aimée ou non. Ce champ est donc la cible à prédire.

Entrainement

Parmi les données, ou features, que l'on récupère on détermine celle qui sont importantes. Pour cela on utilise l’algorithme Random Forest.

Les 3 features qui apparaissent en bas du classement sont “instrumentalness”, “mode” et “time_signature”. Nous n’avons donc pas utilisé ces données pour entraîner notre modèle.

Ensuite l’algorithme KNN permet de classifier. On entraîne le modèle sur le dataset crée. Le score du modèle est de 84%.

Test
Pour finir on récupère une autre playlist pour là faire passer dans le modèle entraîné. Et on retourne un pourcentage de sur la playlist représentant le nombre de “like” sur le nombre total de chansons.

En perspective, on souhaite pouvoir créer des playlists pour l’utilisateur. On prendra en compte les artistes en utilisant la fonctionnalité related artist de l’api spotify qui permet de trouver artistes lié aux artist présent dans le dataset puis de passer par exemple les titres récents dans le modèle afin de déterminer si la musique va être aimée ou non et l’ajouter automatiquement dans une nouvelle playlist.
