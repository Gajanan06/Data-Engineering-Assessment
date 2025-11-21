import json
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Disable Firestore emulator if active
os.environ.pop("FIRESTORE_EMULATOR_HOST", None)
os.environ.pop("FIREBASE_FIRESTORE_EMULATOR_ADDRESS", None)
os.environ.pop("GCLOUD_PROJECT", None)

# 1️⃣ Initialize Firebase Admin SDK
cred = credentials.Certificate(r"D:\Gajanan\THINKSCHOOL\Assesment\gajanan-info-firebase-adminsdk-fbsvc-22bd2686ba.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# 2️⃣ Load JSON files
with open("input/recipe.json", "r") as f:
    recipes = json.load(f)

with open("input/users.json", "r") as f:
    users = json.load(f)

with open("input/interactions.json", "r") as f:
    interactions = json.load(f)

# 3️⃣ Upload Recipes
print("\n⏫ Uploading Recipes...")
recipe_ref = db.collection("recipes")
for r in recipes:
    recipe_ref.document(r["recipe_id"]).set(r)
print("✅ Recipes uploaded successfully!")

# 4️⃣ Upload Users
print("\n⏫ Uploading Users...")
user_ref = db.collection("users")
for u in users:
    user_ref.document(u["user_id"]).set(u)
print("✅ Users uploaded successfully!")

# 5️⃣ Upload Interactions
print("\n⏫ Uploading Interactions...")
interaction_ref = db.collection("interactions")
for i in interactions:
    interaction_ref.document(i["interaction_id"]).set(i)
print("✅ Interactions uploaded successfully!")

print("\n🎉 ALL DATA UPLOADED TO FIRESTORE!")
