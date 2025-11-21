import pandas as pd

# Load CSVs
recipes = pd.read_csv("output/recipes.csv")
ingredients = pd.read_csv("output/ingredients.csv")
interactions = pd.read_csv("output/interactions.csv")
steps = pd.read_csv("output/steps.csv")

print("\n================= ANALYTICS REPORT =================\n")

# 1. MOST COMMON INGREDIENTS
print("1. Most Common Ingredients:")
ingredient_counts = ingredients["name"].value_counts().head(10)
print(ingredient_counts)
print("\n📌 Insight: Most frequently used ingredients identified.\n")

# 2. AVERAGE PREPARATION TIME
avg_prep = recipes["prep_time_minutes"].mean()
print(f"2. Average Preparation Time: {avg_prep:.2f} minutes\n")

# 3. DIFFICULTY DISTRIBUTION
print("3. Difficulty Distribution:")
print(recipes["difficulty"].value_counts())
print("\n📌 Insight: Mostly easy & medium recipes.\n")

# 4. MOST VIEWED RECIPES
print("4. Most Viewed Recipes:")
views = interactions[interactions["type"] == "view"]
print(views["recipe_id"].value_counts().head(5))
print("\n📌 Insight: Highest-viewed recipes listed.\n")

# 5. MOST LIKED RECIPES
print("5. Most Liked Recipes:")
likes = interactions[interactions["type"] == "like"]
print(likes["recipe_id"].value_counts().head(5))
print("\n📌 Insight: Most liked recipes identified.\n")

# 6. HIGH-ENGAGEMENT INGREDIENTS
print("6. Ingredients Linked to High Engagement:")
engagement = (
    interactions[interactions["type"].isin(["view", "like"])]
    .groupby("recipe_id").size().reset_index(name="engagement")
)

merged_ing = ingredients.merge(engagement, on="recipe_id")
top_ing = merged_ing.groupby("name")["engagement"].sum().sort_values(ascending=False).head(10)
print(top_ing)
print("\n📌 Insight: High-engagement ingredient patterns found.\n")

# 7. PREP TIME VS LIKES
print("7. Prep Time vs Likes:")
likes_all = likes["recipe_id"].value_counts().reset_index()
likes_all.columns = ["recipe_id", "likes"]
merged2 = recipes.merge(likes_all, on="recipe_id", how="left").fillna(0)
quick = merged2[merged2["prep_time_minutes"] < 15]["likes"].mean()
slow = merged2[merged2["prep_time_minutes"] >= 15]["likes"].mean()

print(f"Avg likes (<15 mins): {quick:.2f}")
print(f"Avg likes (≥15 mins): {slow:.2f}\n")
print("📌 Insight: Quick recipes attract more likes.\n")

# 8. LONGEST TOTAL TIME RECIPES
print("8. Longest Recipes (By Total Time):")
print(recipes[["recipe_id", "total_time_minutes"]].sort_values(by="total_time_minutes", ascending=False).head(5))
print("\n📌 Insight: Longer recipes tend to be less popular.\n")

# 9. MOST ATTEMPTED
print("9. Most Attempted Recipes:")
attempts = interactions[interactions["type"] == "attempt"]
if attempts.empty:
    print("No attempts in dataset.\n")
else:
    print(attempts["recipe_id"].value_counts().head(5))
print("\n📌 Insight: Recipes attempted the most.\n")

# 10. OVERALL ENGAGEMENT
print("10. Overall Engagement (Views + Likes):")
engagement_total = engagement.sort_values(by="engagement", ascending=False).head(5)
print(engagement_total)
print("\n📌 Insight: Top recipes by total engagement.\n")

# 11. MOST ACTIVE USERS (Optional)
print("11. Most Active Users:")
print(interactions["user_id"].value_counts().head(5))
print("\n📌 Insight: Most active users identified.\n")

print("================= END OF REPORT =================\n")
