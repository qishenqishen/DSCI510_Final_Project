# src/run_analysis.py
# Optimized Data Analysis for IMDb Top 250 (No Votes Version)

import os
import pandas as pd

OUT_DIR = "data/processed"


def main():
    print("Running optimized data analysis...")

    movies = pd.read_csv(f"{OUT_DIR}/imdb_movies_clean.csv")
    genres = pd.read_csv(f"{OUT_DIR}/imdb_genre_clean.csv")

    # Basic type safety
    movies["rating"] = pd.to_numeric(movies["rating"], errors="coerce")
    movies["runtime_min"] = pd.to_numeric(movies["runtime_min"], errors="coerce")
    movies["year"] = pd.to_numeric(movies["year"], errors="coerce")

    if "decade" not in movies.columns:
        movies["decade"] = (movies["year"] // 10) * 10

    genres["rating"] = pd.to_numeric(genres["rating"], errors="coerce")

    # TABLE A: Movie count by decade (sample distribution)
    counts_by_decade = (
        movies.dropna(subset=["decade"])
              .groupby("decade")
              .size()
              .reset_index(name="movie_count")
              .sort_values("decade")
    )

    counts_by_decade.to_csv(
        f"{OUT_DIR}/analysis_counts_by_decade.csv",
        index=False
    )
    print("Saved: analysis_counts_by_decade.csv")

    # TABLE B: Average rating by decade
    rating_by_decade = (
        movies.dropna(subset=["decade", "rating"])
              .groupby("decade")["rating"]
              .agg(avg_rating="mean", movie_count="count")
              .reset_index()
              .sort_values("decade")
    )

    rating_by_decade.to_csv(
        f"{OUT_DIR}/analysis_rating_by_decade.csv",
        index=False
    )
    print("Saved: analysis_rating_by_decade.csv")

    # TABLE C: Average rating by genre (n >= 5)
    rating_by_genre = (
        genres.dropna(subset=["genre", "rating"])
              .groupby("genre")["rating"]
              .agg(avg_rating="mean", movie_count="count")
              .reset_index()
              .sort_values("avg_rating", ascending=False)
    )

    rating_by_genre = rating_by_genre[rating_by_genre["movie_count"] >= 5]

    rating_by_genre.to_csv(
        f"{OUT_DIR}/analysis_rating_by_genre.csv",
        index=False
    )
    print("Saved: analysis_rating_by_genre.csv")

    # TABLE D: Runtime–Rating correlation by decade
    corr_rows = []

    for decade, group in movies.dropna(
        subset=["decade", "runtime_min", "rating"]
    ).groupby("decade"):

        if len(group) >= 5:
            corr = group["runtime_min"].corr(group["rating"])
            corr_rows.append({
                "decade": decade,
                "corr_runtime_rating": corr,
                "n_movies": len(group)
            })

    corr_by_decade = pd.DataFrame(corr_rows).sort_values("decade")

    corr_by_decade.to_csv(
        f"{OUT_DIR}/analysis_runtime_rating_corr_by_decade.csv",
        index=False
    )
    print("Saved: analysis_runtime_rating_corr_by_decade.csv")

    print("\nOptimized data analysis completed successfully.")


if __name__ == "__main__":
    main()
