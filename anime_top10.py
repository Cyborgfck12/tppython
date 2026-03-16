import pandas as pd

# 1 Charger le dataset
df = pd.DataFrame({
    "Anime": [
        "Attack on Titan",
        "Death Note",
        "One Piece",
        "Naruto",
        "Fullmetal Alchemist",
        "Demon Slayer",
        "Steins Gate",
        "Dragon Ball Z",
        "Hunter x Hunter",
        "Cowboy Bebop"
    ],
    "Note": [
        9.1,
        9.0,
        8.8,
        8.3,
        9.2,
        8.7,
        9.1,
        8.9,
        9.0,
        8.8
    ],
    "Popularite": [
        95,
        93,
        98,
        96,
        90,
        92,
        85,
        97,
        89,
        84
    ]
})

print(df)

# 2 Vérifier les valeurs manquantes
print(df.isnull().sum())

# 3 Remplacer les NaN par la moyenne
df["Note"] = df["Note"].fillna(df["Note"].mean())

# 4 Supprimer les doublons
df = df.drop_duplicates()

print(df)

# 5 Créer un score simple
df["Score_final"] = (
    0.6 * df["Note"]
    + 0.4 * (df["Popularite"] / 10)
)

print(df)

# 6 Produire le Top 10
top10 = df.sort_values(
    "Score_final",
    ascending=False
)

print("Top 10 des animes 😊")
print(top10[["Anime", "Score_final"]])
