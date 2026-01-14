# 📊 Credit Guard: Loan Default Risk Prediction System  

🔮 *It is an end-to-end machine learning solution designed to help financial institutions minimize credit risk. By analyzing historical loan application data, the system identifies key patterns that lead to defaults, allowing lenders to make data-driven decisions on whether to approve or reject a loan.*  

---

## 🛠️ Data Features
The dataset includes the following features for each applicant:
- **Personal:** Gender, Marital Status, Dependents, Education.
- **Financial:** Applicant Income, Co-applicant Income, Loan Amount, Loan Term.
- **Credit:** Credit History (0 or 1), Property Area (Urban/Semiurban/Rural).
- **Target:** `Status` (Y = Approved/Repaid, N = Default/Rejected).

---

## 🚀 Workflow
1. **Data Preprocessing**: Handling missing values and encoding categorical text into numerical format.
2. **Exploratory Data Analysis (EDA)**: Visualizing the relationship between credit history and loan approval.
3. **Feature Selection**: Dropping non-predictive columns like `Loan_ID`.
4. **Model Training**: 
   - **Logistic Regression**: Baseline statistical model.
   - **Random Forest**: Advanced ensemble model for higher accuracy.
5. **Evaluation**: Comparing models using accuracy scores and confusion matrices.

---

## 🧰 Tech Stack  

- **Language:** Python 🐍  
- **Libraries:**  
  - `pandas`, `numpy` → Data wrangling  
  - `matplotlib`, `seaborn` → Visualization  
  - `scikit-learn` → Machine Learning  

---

## 📊 Results Summary
| Model              | Accuracy | Suitability |
| :--- | :--- | :--- |
| Logistic Regression | ~80% | High interpretability |
| Random Forest | ~85% | Better at catching complex patterns |

