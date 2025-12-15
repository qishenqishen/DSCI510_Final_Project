#!/usr/bin/env python
# coding: utf-8

# Figure 1 ： Average rating trend by decade

# In[29]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis_rating_by_decade.csv")

df = df.sort_values("decade")

plt.figure(figsize=(10, 5))

plt.bar(df["decade"].astype(str), df["avg_rating"], color="skyblue", edgecolor="black")

plt.plot(df["decade"].astype(str), df["avg_rating"], 
         color="red", marker="o", linewidth=2, label="Trend")

plt.ylim(df["avg_rating"].min() - 0.05, df["avg_rating"].max() + 0.05)

for i, v in enumerate(df["avg_rating"]):
    plt.text(i, v + 0.01, f"{v:.2f}",
             ha="center", fontsize=9)

plt.xlabel("Decade")
plt.ylabel("Average Rating")
plt.title("IMDb Top 250 - Average Rating Trend by Decade")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("figure1.jpg", format="jpg", dpi=300)

plt.show()


# Figure 2: Number of movies by decade

# In[26]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis_counts_by_decade.csv")

df = df.sort_values("decade")

plt.figure(figsize=(10, 5))

plt.bar(df["decade"].astype(str), df["movie_count"], 
        color="lightgreen", edgecolor="black")

plt.xlabel("Decade")
plt.ylabel("Number of Movies")
plt.title("IMDb Top 250 - Number of  Movies by Decade")

plt.xticks(rotation=45)

for i, v in enumerate(df["movie_count"]):
    plt.text(i, v + 0.3, str(v), 
             ha="center", fontsize=9)

plt.tight_layout()
plt.savefig("figure2.jpg", format="jpg", dpi=300)

plt.show()


# Figure 3: Average rating by genre

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis_rating_by_genre.csv")

df = df.sort_values("avg_rating", ascending=False)

plt.figure(figsize=(12, 6))

plt.bar(df["genre"], df["avg_rating"],
        color="salmon", edgecolor="black")

for i, v in enumerate(df["avg_rating"]):
    plt.text(i, v + 0.01, f"{v:.2f}", 
             ha="center", fontsize=9)
    
plt.ylim(df["avg_rating"].min() - 0.05, df["avg_rating"].max() + 0.05)

plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.title("IMDb Top 250 - Average Rating by Genre")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("figure3.jpg", format="jpg", dpi=300)

plt.show()


# Figure 4: Runtime-Rating correlation by genre

# In[28]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis_runtime_rating_corr_by_decade.csv")

df = df.sort_values("decade")

plt.figure(figsize=(10, 6))

plt.bar(df["decade"].astype(str), df["corr_runtime_rating"],
        color="mediumpurple", edgecolor="black")

plt.axhline(0, color="black", linewidth=1)

for i, v in enumerate(df["corr_runtime_rating"]):
    plt.text(i, v + (0.02 if v >= 0 else -0.05), 
             f"{v:.2f}", ha="center", fontsize=9)

plt.ylim(-0.6, 0.6)

plt.xlabel("Decade")
plt.ylabel("Correlation (Runtime vs Rating)")
plt.title("IMDb Top 250 - Runtime–Rating Correlation by Decade")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("figure4.jpg", format="jpg", dpi=300)

plt.show()

