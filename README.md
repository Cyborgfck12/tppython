# Top 10 des Animes - Analyse avec Python & Pandas

# Description

Ce projet Python annalyse un dataset d'animes et génere un clasement basé sur un score combinant la note et la popularité de chaque anime.

# Dataset

On a créé un dataset manuel avec **10 animes populaires**, chacun ayant :
- **Anime** : le nom de l'anime
- **Note** : une note sur 10 (style MAL - MyAnimeList)
- **Popularite** : un score de popularité sur 100

# Etapes du traitement

# 1. Chargement des données
On construit le DataFrame directement avec `pd.DataFrame(...)`, sans fichier externe, pour garder le projet simple et autonaume.

# 2. Vérification des valeurs manquantes
On utilise `df.isnull().sum()` pour detecter d'éventuels NaN. Ici le dataset est propre, mais cette étape est importente dans une vraie analyse.

# 3. Remplacement des NaN par la moyenne
Au cas ou des notes seraient manquantes, on les remplace par la moyenne de la colonne `Note` avec `fillna(mean())`. Ca évite de perdre des lignes et reste representatif.

# 4. Suppression des doublons
`drop_duplicates()` assure qu'un meme anime n'est pas compté deux fois.

# 5. Calcul du Score Final
On a créé une formule pondéré :

```
Score_final = 0.6 × Note + 0.4 × (Popularite / 10)
```

- **60% sur la note** : la qualité perçue compte plus que la popularité
- **40% sur la popularité** : ramenée sur 10 pour être sur la même échelle que la note
- Ce choix reflète notre opinion : un anime peut être très populaire sans être excelent (ex : Dragon Ball Z vs Steins;Gate)

# 6. Classement Top 10
On trie par `Score_final` décroisant avec `sort_values(ascending=False)` pour afficher le meilleur en permier.

# Résultat


Top 10 des animes
                 Anime  Score_final
0      Attack on Titan         9.26
7        Dragon Ball Z         9.22
2            One Piece         9.20


# Lancer le script

bash
pip install pandas
python anime_top10.py


# Technologies utilisées

- Python 3
- Pandas
