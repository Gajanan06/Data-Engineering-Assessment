import json

# Load files
with open("input/recipe.json", encoding="utf-8") as f:
    recipes = json.load(f)

with open("input/interactions.json", encoding="utf-8") as f:
    interactions = json.load(f)

with open("input/users.json", encoding="utf-8") as f:
    users = json.load(f)

report = []

# Allowed values
valid_difficulty = ["easy", "medium", "hard"]
valid_interaction_types = ["view", "like", "rating", "attempt"]

# Build lookup sets for FK validation
recipe_ids = {r["recipe_id"] for r in recipes}
user_ids = {u["user_id"] for u in users}

# ------------------ VALIDATE RECIPES ------------------
report.append("---- RECIPE VALIDATION ----")

for r in recipes:
    errors = []

    # Required fields
    required_fields = ["recipe_id", "title", "ingredients", "steps"]
    for field in required_fields:
        if field not in r or r[field] in ["", None]:
            errors.append(f"Missing required field: {field}")

    # Arrays must not be empty
    if isinstance(r.get("ingredients"), list) and len(r["ingredients"]) == 0:
        errors.append("Ingredients list is empty")

    if isinstance(r.get("steps"), list) and len(r["steps"]) == 0:
        errors.append("Steps list is empty")

    # Difficulty check
    if r.get("difficulty") not in valid_difficulty:
        errors.append(f"Invalid difficulty: {r.get('difficulty')}")

    # Positive numeric fields
    for fnum in ["prep_time_minutes", "cook_time_minutes", "total_time_minutes"]:
        if r.get(fnum) is not None and r[fnum] < 0:
            errors.append(f"{fnum} must be positive")

    if errors:
        report.append(f"[INVALID] Recipe ID: {r['recipe_id']} - {errors}")
    else:
        report.append(f"[VALID] Recipe ID: {r['recipe_id']}")

# ------------------ VALIDATE USERS ------------------
report.append("\n---- USER VALIDATION ----")

for u in users:
    errors = []

    if "user_id" not in u or not u["user_id"]:
        errors.append("Missing user_id")

    if "email" not in u or not u["email"]:
        errors.append("Missing email")

    if errors:
        report.append(f"[INVALID] User ID: {u.get('user_id','?')} - {errors}")
    else:
        report.append(f"[VALID] User ID: {u['user_id']}")

# ------------------ VALIDATE INTERACTIONS ------------------
report.append("\n---- INTERACTIONS VALIDATION ----")

for i in interactions:
    errors = []

    required_fields = ["interaction_id", "user_id", "recipe_id", "type"]
    for field in required_fields:
        if field not in i or i[field] in ["", None]:
            errors.append(f"Missing required field: {field}")

    # Check type
    if i.get("type") not in valid_interaction_types:
        errors.append(f"Invalid interaction type: {i.get('type')}")

    # Rating must be 1–5 if type=rating
    if i.get("type") == "rating":
        if "rating" not in i or i["rating"] not in [1, 2, 3, 4, 5]:
            errors.append("Rating must be between 1–5")

    # Foreign key: recipe must exist
    if i.get("recipe_id") not in recipe_ids:
        errors.append(f"Invalid recipe_id: {i.get('recipe_id')} (not found)")

    # Foreign key: user must exist
    if i.get("user_id") not in user_ids:
        errors.append(f"Invalid user_id: {i.get('user_id')} (not found)")

    if errors:
        report.append(f"[INVALID] Interaction ID: {i['interaction_id']} - {errors}")
    else:
        report.append(f"[VALID] Interaction ID: {i['interaction_id']}")

# ------------------ WRITE REPORT ------------------
with open("output/validation_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("Validation complete! Report saved as output/validation_report.txt")
