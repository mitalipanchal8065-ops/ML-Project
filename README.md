# 🎓 Student Result Prediction Using Machine Learning

**Author:** Mitali Panchal  
**Tools Used:** Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
**Date:** January 2026  

---

## 🧾 Abstract / Summary

This project aims to predict whether a student will **pass or fail** based on academic performance features.  
The dataset consists of student-related numerical attributes collected from a CSV file.  
Exploratory Data Analysis (EDA) was performed to detect outliers and skewness.  
Three classification models were built: Logistic Regression, Decision Tree, and Random Forest.  
Models were evaluated using accuracy, confusion matrix, and classification report.  
Random Forest achieved the best overall performance and was selected as the final model.

---

## 🎯 Problem Statement

### Objective
To predict whether a student will **pass (1) or fail (0)** using academic performance features.

### Problem Type
- ✔ Classification  
- ✔ Supervised Learning  

---

## 📁 Dataset Description

### Source
- Dataset loaded from local file: `student_result.csv`

### Columns Description

| Column Name | Description |
|------------|-------------|
| student_id | Unique ID of student |
| Feature columns | Academic performance attributes |
| pass | Target variable (0 = Fail, 1 = Pass) |

### Target Variable
- **Target:** `pass`

---

## ⚙️ Methodology (CORE SECTION)

### 1. Data Collection
- Dataset loaded using `pandas.read_csv()`
- Basic structure inspected using column listing

### 2. Exploratory Data Analysis (EDA)
- Boxplots plotted for all numerical columns
- Checked for outliers
- Skewness calculated using `scipy.stats.skew`

**Observation:**
- All skewness values lie between **-0.5 and +0.5**
- Hence, data is approximately symmetric and **no skewness treatment required**

---

### 3. Data Preprocessing
- Removed irrelevant columns: `student_id`
- Split dataset into:
  - Features (`X`)
  - Target (`y`)
- Performed Train-Test Split (75% train, 25% test)
- Applied **StandardScaler** for Logistic Regression

---

### 4. Feature Engineering
- Feature selection done by removing ID column
- No new features created
- Scaling applied only where required

---

### 5. Model Building

The following models were trained:

#### 🔹 Logistic Regression
- Used scaled data
- Suitable for binary classification

#### 🔹 Decision Tree Classifier
- `max_depth = 5`
- Captures non-linear relationships

#### 🔹 Random Forest Classifier
- `n_estimators = 100`
- `max_depth = 7`
- Ensemble method for better accuracy

---

### 6. Model Evaluation

Evaluation metrics used:
- Accuracy
- Confusion Matrix
- Precision, Recall, F1-score

---

## 📈 Results & Discussion

### Model Performance Summary

| Model | Accuracy | Remarks |
|------|---------|--------|
| Logistic Regression | Moderate | Simple & interpretable |
| Decision Tree | Better | Handles non-linearity |
| Random Forest | Best | High accuracy & stability |

### Final Model Selection
**Random Forest Classifier** was chosen because:
- Highest accuracy
- Better generalization
- Handles feature interactions well

---

## ✅ Conclusion

- Successfully built a student result prediction system
- Compared multiple classification models
- Random Forest performed best among all

### Key Learnings
- Importance of EDA before preprocessing
- Role of feature scaling
- Model comparison is critical

### Limitations
- Dataset size may be limited
- No hyperparameter tuning
- Only academic features used

---

## 🔮 Future Scope

- Add more student behavioral data
- Perform hyperparameter tuning
- Try advanced models like XGBoost
- Deploy model using Flask or Streamlit

---

## 🛠️ Tools & Technologies

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📎 Appendix

### Sample Code Snippet
```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, max_depth=7, random_state=1)
rf.fit(x_train, y_train)
