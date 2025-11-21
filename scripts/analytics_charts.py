import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load CSVs
recipes = pd.read_csv("output/recipes.csv")
ingredients = pd.read_csv("output/ingredients.csv")
interactions = pd.read_csv("output/interactions.csv")

# -------------------------- 1. TOP INGREDIENTS --------------------------
ingredient_counts = ingredients["name"].value_counts().head(10)

plt.figure(figsize=(10, 5))
ingredient_counts.plot(kind="bar")
plt.title("Top 10 Most Common Ingredients")
plt.xlabel("Ingredient")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/top_ingredients.png")
plt.close()

# ----------------------- 2. DIFFICULTY DISTRIBUTION -----------------------
difficulty_counts = recipes["difficulty"].value_counts()

all_levels = ["easy", "medium", "hard"]
for level in all_levels:
    if level not in difficulty_counts.index:
        difficulty_counts.loc[level] = 0

difficulty_counts = difficulty_counts.reindex(all_levels)

plt.figure(figsize=(8,5))
difficulty_counts.plot(kind="bar")
plt.title("Difficulty Distribution")
plt.xlabel("Difficulty Level")
plt.ylabel("Number of Recipes")
plt.tight_layout()
plt.savefig("charts/difficulty_distribution.png")
plt.close()

# ------------------------- 3. MOST VIEWED RECIPES -------------------------
views = interactions[interactions["type"] == "view"]
view_counts = views["recipe_id"].value_counts().head(5)

plt.figure(figsize=(10, 5))
view_counts.plot(kind="bar")
plt.title("Top 5 Most Viewed Recipes")
plt.xlabel("Recipe ID")
plt.ylabel("View Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/most_viewed.png")
plt.close()

# ------------------------- 4. MOST LIKED RECIPES -------------------------
likes = interactions[interactions["type"] == "like"]
like_counts = likes["recipe_id"].value_counts().head(5)

plt.figure(figsize=(10, 5))
like_counts.plot(kind="bar")
plt.title("Top 5 Most Liked Recipes")
plt.xlabel("Recipe ID")
plt.ylabel("Like Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/most_liked.png")
plt.close()

print("✅ All charts generated and saved inside /charts folder!")
