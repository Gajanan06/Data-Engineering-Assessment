import json
import pandas as pd
import os

# Input paths
recipes_path = "input/recipe.json"
interactions_path = "input/interactions.json"
users_path = "input/users.json"     # ⭐ ADDED

# Output folder
os.makedirs("output", exist_ok=True)

# Load JSON
with open(recipes_path, "r") as f:
    recipes = json.load(f)

with open(interactions_path, "r") as f:
    interactions = json.load(f)

with open(users_path, "r") as f:     # ⭐ ADDED
    users = json.load(f)

# ------------ USERS TABLE ---------------------
users_list = []

for u in users:
    users_list.append({
        "user_id": u["user_id"],
        "name": u.get("name", ""),
        "email": u.get("email", "")
    })

pd.DataFrame(users_list).to_csv("output/users.csv", index=False)
print("✔ users.csv generated")

# ------------ RECIPES TABLE ---------------------
recipes_list = []

for r in recipes:
    recipes_list.append({
        "recipe_id": r["recipe_id"],
        "title": r["title"],
        "description": r.get("description", ""),
        "cuisine": r.get("cuisine", ""),
        "difficulty": r.get("difficulty", ""),
        "prep_time_minutes": r.get("prep_time_minutes", None),
        "cook_time_minutes": r.get("cook_time_minutes", None),
        "total_time_minutes": r.get("total_time_minutes", None),
        "servings": r.get("servings", None),
        "tags": "|".join(r.get("tags", []))
    })

pd.DataFrame(recipes_list).to_csv("output/recipes.csv", index=False)
print("✔ recipes.csv generated")

# ------------ INGREDIENTS TABLE -----------------
ingredients_list = []

for r in recipes:
    for idx, ing in enumerate(r["ingredients"], start=1):
        ingredients_list.append({
            "ingredient_id": f"{r['recipe_id']}_ing_{idx}",
            "recipe_id": r["recipe_id"],
            "name": ing["name"],
            "quantity": ing["quantity"],
            "unit": ing["unit"]
        })

pd.DataFrame(ingredients_list).to_csv("output/ingredients.csv", index=False)
print("✔ ingredients.csv generated")

# ------------- STEPS TABLE -----------------------
steps_list = []

for r in recipes:
    for s in r["steps"]:
        steps_list.append({
            "recipe_id": r["recipe_id"],
            "step_no": s["step_no"],
            "text": s["text"]
        })

pd.DataFrame(steps_list).to_csv("output/steps.csv", index=False)
print("✔ steps.csv generated")

# ------------- INTERACTIONS TABLE ----------------
interactions_list = []

for i in interactions:
    interactions_list.append({
        "interaction_id": i["interaction_id"],
        "user_id": i["user_id"],
        "recipe_id": i["recipe_id"],
        "type": i["type"],
        "rating": i.get("rating", None),
        "timestamp": i.get("timestamp", "")
    })

pd.DataFrame(interactions_list).to_csv("output/interactions.csv", index=False)
print("✔ interactions.csv generated")

print("\n🎉 ETL Completed! All CSV files saved in output folder.")
