# 📊 Loan Default Risk Prediction System  

🔮 *Predicting loan defaults using Machine Learning to assist financial institutions in smarter lending decisions.*  

---

## 🌟 Overview  
This project develops a **Loan Default Risk Prediction System** using two machine learning models:  
- 🟢 **Logistic Regression** (Baseline model)  
- 🌲 **Random Forest Classifier** (Advanced ensemble model)  

The system predicts whether a customer will **repay** or **default** on their loan based on financial and demographic data.  

---

## 🛠 Workflow  

### 🔹 1. Data Cleaning & Preprocessing  
✔️ Handle missing values & outliers  
✔️ Encode categorical features  
✔️ Normalize/standardize numerical columns  

### 🔹 2. Exploratory Data Analysis (EDA)  
📊 Visualizations include:  
- Loan status distribution  
- Income levels vs default rate  
- Correlation heatmap  
- Credit history impact  

### 🔹 3. Train-Test Split  
- Dataset split into **80% Training** and **20% Testing**  

### 🔹 4. Model Training  
- **Logistic Regression** → Simple, interpretable baseline  
- **Random Forest** → Handles non-linearity & improves accuracy  

### 🔹 5. Evaluation Metrics  
✅ Accuracy  
✅ Precision  
✅ Recall  
✅ F1-Score  
✅ ROC-AUC Curve  

---

## 🧰 Tech Stack  

- **Language:** Python 🐍  
- **Libraries:**  
  - `pandas`, `numpy` → Data wrangling  
  - `matplotlib`, `seaborn` → Visualization  
  - `scikit-learn` → Machine Learning  

---

## 📈 Results  

| Model                | Accuracy | Precision | Recall | F1-Score |
|-----------------------|----------|-----------|--------|----------|
| Logistic Regression   | ⭐ Good   | Moderate  | Moderate | Baseline |
| Random Forest         | 🌟 Higher | Better    | Robust | Best |  

📌 *Random Forest outperformed Logistic Regression with improved accuracy and generalization.*  

---
