<!-- PROJECT HEADER -->
<p align="center">
  <img src="https://img.icons8.com/color/96/cookbook.png" alt="Project Logo"/>
</p>

<h1 align="center">Firebase Recipe Analytics Pipeline</h1>

<p align="center">
  📘 Recipe Analytics Pipeline  
  Firebase → ETL → Validation → Analytics → Charts  
  <br/>
</p>

---

## 📑 Table of Contents
- 🚀 Project Overview
- 🏗 Architecture
- 📁 Project Structure
- 📦 Data Model
- 🔥 Firebase Source Setup
- ⚙️ ETL Pipeline
- 🧹 Data Quality Validation
- 📊 Analytics & Insights
- 📈 Charts
- ▶️ How to Run
- ⚠️ Known Limitations
- 🎯 Conclusion

---

## 🚀 Project Overview
This project implements a complete **Data Engineering Pipeline** using:

- Firebase Firestore  
- Python ETL  
- Data Quality Validation  
- Recipe Analytics  
- Visualization Charts  

The goal is to build an end-to-end pipeline from source data to insights.

---

## 🏗 Architecture

```bash

Sample Data
↓
Firebase Firestore
↓
JSON Export
↓
ETL Pipeline (Python)
↓
Normalized CSVs
↓
Data Validation
↓
Analytics & Insights
↓
Charts
```

---

## 📁 Project Structure

```bash
Data Engineering Assessment Folder
│
├── input/                     → Raw JSON files (recipes, interactions, users)
│   ├── recipe.json
│   ├── interactions.json
│   └── users.json
│
├── output/                    → Normalized CSVs + Validation report
│   ├── recipes.csv
│   ├── ingredients.csv
│   ├── steps.csv
│   ├── interactions.csv
│   └── validation_report.txt
│
├── scripts/                   → All Python scripts for the pipeline
│   ├── upload_to_firestore.py       → Upload JSON files to Firestore
│   ├── export_firestore.py          → Export Firestore data (manual export)
│   ├── etl_transform.py             → Transform JSON → normalized CSV
│   ├── validator.py                 → Data Quality Validation
│   ├── analytics.py                 → Analytics insights summary
│   └── analytics_charts.py          → Generates visualization charts
│
├── screenshots/                → Firestore UI screenshots
│   ├── recipes_collection.png
│   ├── interactions_collection.png
│   ├── users_collection.png
│   └── recipe_expanded.png
│
├── charts/                     → Visualization charts
│   ├── difficulty_distribution.png
│   ├── top_ingredients.png
│   ├── most_viewed.png
│   └── most_liked.png
│
├── requirements.txt            → Python dependencies for running the pipeline
├── README.md                   → Project documentation
└── .gitignore
```

---

## 📦 1. Data Model Overview

### 📌 Recipe Entity
- recipe_id  
- title, description  
- cuisine, difficulty  
- prep_time_minutes  
- cook_time_minutes  
- total_time_minutes  
- servings  
- tags  
- ingredients[]  
- steps[]  
- created_at, created_by  

### 👥 Users
User IDs: `user_100` → `user_115`

### ⭐ User Interactions
- interaction_id  
- user_id  
- recipe_id  
- type: `view`, `like`, `attempt`, `rating`  
- rating (1–5)  
- timestamp  

---

## 🔥 2. Firebase Source Setup

Uploaded to Firestore:

- ✔ Your recipe (Curd Rice)  
- ✔ 20 synthetic recipes  
- ✔ 150+ user interactions  

### Collections Used

| Collection     | Purpose                     |
|----------------|-----------------------------|
| recipes        | Recipe data                 |
| interactions   | User engagement events      |
| users          | Synthetic users             |

---

## 📸 Screenshots

Available in `/screenshots/`:

- recipes_collection.png  
- recipe_extended.png  
- interactions_collection.png  
- users_collection.png  

---

## ⚙️ 3. ETL Pipeline

Firestore export requires billing → **Manual JSON export used**.

Scripts:

- `export_firestore.py` — Export collections  
- `etl_transform.py` — Convert JSON → normalized CSVs  

### Output CSVs

| File              | Description                     |
|------------------|---------------------------------|
| recipes.csv       | Recipe metadata                 |
| ingredients.csv   | One row per ingredient          |
| steps.csv         | One row per step                |
| interactions.csv  | Clean user interactions         |

---

## 🧹 4. Data Quality Validation

Performed using `validator.py`.

### ✔ Recipe Rules
- Required fields present  
- Difficulty ∈ {easy, medium, hard}  
- Positive numeric values  
- Non-empty ingredients and steps  

### ✔ Interaction Rules
- Valid type  
- Rating 1–5  
- Timestamp exists  

### Validation Results
- ✅ All 20 recipes valid  
- ✅ All 180 interactions valid  

Full report:  
`output/validation_report.txt`

---

## 📊 5. Analytics & Insights

### 1️⃣ Most Common Ingredients
- Salt (6)  
- Rice (4)  
- Oil (4)  
- Tomato (3)  
- Flour (3)  

### 2️⃣ Average Preparation Time  
👉 **12.75 minutes**

### 3️⃣ Difficulty Distribution  
- Easy: 10  
- Medium: 10  
- Hard: 0  

### 4️⃣ Most Viewed Recipes
- Curd Rice (7)  
- r_0009 (7)  
- r_0011 (7)  

### 5️⃣ Most Liked Recipes
- Curd Rice (6)  
- r_0010 (4)  

### 6️⃣ Ingredients Linked to Engagement  
Rice, Oil, Spice Mix → highest engagement.

### 7️⃣ Prep Time vs Likes  
Shorter recipes get more likes.

### 8️⃣ Longest Recipes  
Low engagement.

### 9️⃣ Most Attempted  
- Curd Rice  

### 🔟 Overall Engagement Ranking
1. Curd Rice  
2. r_0009  
3. r_0011  

---

## 📈 Charts  
Available in `/charts/`:

- difficulty_distribution.png  
- top_ingredients.png  
- most_viewed.png  
- most_liked.png  

---

## ▶️ How to Run

### 🧪 6. How to Run the Pipeline

1️⃣ Install Dependencies -

      pip install -r requirements.txt

or manually 

      pip install pandas firebase-admin matplotlib

2️⃣ Run ETL - 

      python scripts/etl_transform.py

3️⃣ Run Validation -

      python scripts/validator.py

4️⃣ Run Analytics -

      python scripts/analytics.py

5️⃣ Run Analytics_charts -

      python scripts/analytics_charts.py



Charts saved in `/charts`.

---

## 🚫 Known Limitations
- Firestore export not used due to billing restrictions  
- Synthetic data may not fully reflect real trends  
- Timestamps are artificial  

---

## 🎯 Conclusion
This project demonstrates a full end-to-end **Data Engineering workflow**, including:

- Data Modeling  
- Firestore Data Ingestion  
- ETL Pipeline  
- Data Validation  
- Analytics & Visualizations  
- Final Documentation.  



