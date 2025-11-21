import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Disable emulator if active
os.environ.pop("FIRESTORE_EMULATOR_HOST", None)
os.environ.pop("FIREBASE_FIRESTORE_EMULATOR_ADDRESS", None)

# Create exports folder if not exists
os.makedirs("exports", exist_ok=True)

# Initialize Firestore
cred = credentials.Certificate(
    r"D:\Gajanan\THINKSCHOOL\Assesment\gajanan-info-firebase-adminsdk-fbsvc-22bd2686ba.json"
)
firebase_admin.initialize_app(cred)

db = firestore.client()

def export_collection(collection_name, output_file):
    docs = db.collection(collection_name).get()
    data = [doc.to_dict() for doc in docs]

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Exported {collection_name} → {output_file}")

# Export all collections
export_collection("recipes", "exports/recipes_export.json")
export_collection("users", "exports/users_export.json")  
export_collection("interactions", "exports/interactions_export.json")
