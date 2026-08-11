Website link : https://heartdiseasewebsite-dghwm6kk23rqpkwlee5fc4.streamlit.app/

# ❤️ Heart Disease Predictor

A Streamlit web app that predicts a patient's risk of heart disease from clinical measurements, using a Random Forest classifier trained on the Heart Disease dataset.

**⚠️ Disclaimer:** This tool is for educational and portfolio purposes only. It is **not** a medical diagnosis. Please consult a doctor for real health concerns.

---

## 🔍 Overview

The app collects 13 clinical features commonly used in cardiology risk assessment — age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, resting ECG results, max heart rate, exercise-induced angina, ST depression, slope of the ST segment, number of major vessels, and thalassemia — and predicts whether the patient is at **high risk** or **low risk** of heart disease, along with a confidence score.

## ✨ Features

- **Interactive input form** — all 13 clinical features entered via number inputs and dropdowns, with sensible default values and valid ranges
- **Instant prediction** — Random Forest model classifies risk with one click
- **Confidence score** — predicted probability of heart disease, shown as both a percentage and a progress bar
- **Clean, two-column layout** for fast data entry

## 🧠 Model

- **Algorithm:** Random Forest Classifier
- **Dataset:** Heart Disease dataset (13 clinical features)
- **Output:** Binary risk classification (high / low) with class probabilities

### Input Features

| Feature | Description |
|---|---|
| `age` | Age in years |
| `sex` | Sex (Male / Female) |
| `cp` | Chest pain type (typical angina, atypical angina, non-anginal, asymptomatic) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl (yes/no) |
| `restecg` | Resting ECG results (0–2) |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina (yes/no) |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | Slope of the peak exercise ST segment (0–2) |
| `ca` | Number of major vessels colored by fluoroscopy (0–4) |
| `thal` | Thalassemia (0–3) |

## 📁 Project Structure

```
.
├── app.py               # Streamlit application
├── model.pkl             # Trained Random Forest classifier
├── heart.jpg              # Header image
├── requirements.txt       # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/heart-disease-predictor.git
cd heart-disease-predictor

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## 📊 Usage

1. Fill in the patient's clinical details in the form (age, sex, chest pain type, blood pressure, cholesterol, etc.).
2. Click **Predict**.
3. View the risk classification (High Risk / Low Risk) along with the model's confidence score and risk probability bar.

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [scikit-learn](https://scikit-learn.org/) — Random Forest model
- [pandas](https://pandas.pydata.org/) / [NumPy](https://numpy.org/) — data handling
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) / [Plotly](https://plotly.com/) — visualization (EDA/model development)
- [joblib](https://joblib.readthedocs.io/) — model serialization

## 📈 Dataset

This project uses the **Heart Disease dataset**, a widely used benchmark in machine learning for binary classification of cardiovascular risk based on 13 clinical attributes.

## 👤 Author

**Bishal Tamang**
Data Science Portfolio Project

---

*Built as part of an ongoing machine learning portfolio exploring classification, EDA, and interactive model deployment.*
