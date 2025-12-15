#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv("data/raw/imdb_top250_basic (1).csv")
df.head()


# In[9]:


import pandas as pd
import os
import re

# Paths
raw_path = "data/raw/imdb_top250_basic (1).csv"
movies_output_path = "data/processed/imdb_movies_clean.csv"
genre_output_path = "data/processed/imdb_genre_clean.csv"

os.makedirs("data/processed", exist_ok=True)

# 1. Load raw data
df = pd.read_csv(raw_path)
print("Raw shape:", df.shape)
display(df.head())

# 2. Basic type cleaning
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["rank"] = pd.to_numeric(df["rank"], errors="coerce")

# 3. Clean URL
df["url"] = df["url"].astype(str)
df = df[df["url"].str.startswith("http")]

# 4. Reasonable value ranges
#    - rating between 1 and 10
#    - year between 1900 and 2025
df = df[(df["rating"] >= 1) & (df["rating"] <= 10)]
df = df[(df["year"] >= 1900) & (df["year"] <= 2025)]

# 5. Convert duration to minutes
def duration_to_minutes(x):
    """
    Convert strings like '2h 22m' to total minutes.
    Return None for invalid or non-numeric formats.
    """
    if not isinstance(x, str):
        return None

    h_match = re.search(r"(\d+)\s*h", x)
    m_match = re.search(r"(\d+)\s*m", x)

    h = int(h_match.group(1)) if h_match else 0
    m = int(m_match.group(1)) if m_match else 0

    if h == 0 and m == 0:
        return None

    return h * 60 + m

df["runtime_min"] = df["duration"].apply(duration_to_minutes)

# 6. Drop rows with missing key fields
df = df.dropna(subset=["rating", "year", "rank", "runtime_min"])

# 7. Add decade feature
df["decade"] = (df["year"] // 10) * 10

# 8. Standardize original genre string (movie-level)
df["genre"] = df["genre"].fillna("").astype(str).str.strip()

# 9. Movie-level table (one row per movie)
movies_df = df.drop_duplicates(
    subset=["name", "year", "duration", "rating", "url"]
).reset_index(drop=True)

print("Movie-level shape:", movies_df.shape)
display(movies_df.head())

movies_df.to_csv(movies_output_path, index=False)
print("Movie-level data saved to:", movies_output_path)

# 10. Genre-level table (one row per movie-genre)
genre_df = movies_df.copy()

# Split and explode genres
genre_df["genre"] = genre_df["genre"].astype(str).str.split(", ")
genre_df = genre_df.explode("genre")

# Clean empty genres
genre_df["genre"] = genre_df["genre"].str.strip()
genre_df = genre_df[genre_df["genre"] != ""]
genre_df = genre_df[genre_df["genre"].notna()]

genre_df = genre_df.drop_duplicates().reset_index(drop=True)

print("Genre-level shape:", genre_df.shape)
display(genre_df.head())

genre_df.to_csv(genre_output_path, index=False)
print("Genre-level data saved to:", genre_output_path)


