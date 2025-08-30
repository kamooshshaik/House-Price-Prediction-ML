# 🏠 House Price Prediction (ML + Deployment)

## 📌 Overview
This project predicts **house prices** using Machine Learning.  
It demonstrates the **end-to-end ML workflow**:
1. Exploratory Data Analysis (EDA)
2. Feature Engineering & Preprocessing
3. Model Training & Evaluation
4. Deployment with:
   - 🎛️ **Jupyter Notebook Widgets**
   - 🌐 **Streamlit Web App**

---

## 🚀 Tech Stack
- **Python (3.9+)**
- **Libraries**: pandas, numpy, matplotlib, seaborn  
- **ML Models**: scikit-learn (Linear Regression, Random Forest, Gradient Boosting)  
- **Deployment**: ipywidgets (Jupyter), Streamlit (web app)  

---





---

## 📊 Exploratory Data Analysis (EDA)
We explored the dataset with multiple visualizations:
- **Histograms & Boxplots** – distributions of price, bedrooms, bathrooms, etc.  
- **Pairplots** – correlations among bedrooms, bathrooms, area, and price.  
- **Heatmap** – strongest predictors of price.  

### 🔍 Key Insights
- **Living Area** and **Grade** have the highest correlation with price.  
- Renovation and condition moderately affect value.  
- Outliers exist in lot size and price.

---

## ⚙️ Feature Engineering
- **Log transformation** applied on Price.  
- Derived features:
  - `house_age` (current year – built year)  
  - `renovated` (binary indicator)  
  - `living_area_renov`, `lot_area_renov`  

---

## 🧪 Model Training & Evaluation
We trained 3 models and compared them:

| Model              | R²     | MAE     | RMSE    |
|--------------------|--------|---------|---------|
| Linear Regression  | 0.77   | 0.196   | 0.254   |
| Random Forest      | 0.89   | 0.123   | 0.172   |
| Gradient Boosting  | 0.90   | 0.124   | 0.171   |

✅ **Final Model**: Gradient Boosting Regressor  

---

## 🎛️ Jupyter Notebook Predictor
An **interactive UI** was built using `ipywidgets`:

- Sliders for bedrooms, bathrooms, living area, lot area, etc.  
- Button to trigger prediction.  
- Styled box shows **predicted price + category** (`Cheap`, `Moderate`, `Luxury`).  



## 🌐 Streamlit Web App
A **web app (`app.py`)** allows predictions outside Jupyter.

### Features:
- Input sliders for house details.  
- Hidden defaults for non-user features (like latitude/longitude).  
- Displays predicted price & category in styled box.  

### Run:
```bash
streamlit run app.py

