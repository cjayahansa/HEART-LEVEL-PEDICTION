# ❤️ Heart Level Prediction App

## 🌟 Overview

**Heart Level Prediction App** is a machine learning-based web application developed using **Python**, **Flask**, and **scikit-learn**. It predicts the **risk level of heart disease** based on user-provided health data such as age, cholesterol levels, smoking habits, blood pressure medication, diabetes status, and more.

The application classifies risk into three categories:
- 🟢 Low Risk
- 🟡 Moderate Risk
- 🔴 High Risk

---

## 🚀 Features

- **User-friendly Web Interface**: Clean and intuitive form to collect health data.
- **Real-time Prediction**: Displays the heart disease risk level immediately after form submission.
- **Scalable Architecture**: Built with Flask for easy deployment and scalability.
- **Model Integration**: Uses a pre-trained machine learning model (`myheart_risk_prediction_regression_model.sav`) for risk prediction.

---

## 🛠️ Technologies Used

- **Python** – Backend programming
- **Flask** – Lightweight web framework
- **scikit-learn** – Machine learning modeling and prediction
- **Joblib** – Model serialization and loading
- **HTML/CSS** – User interface

---

## 📦 Prerequisites

Ensure the following are installed:

- Python 3.x
- `pip` (Python package installer)

---

## 🏁 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/heart-level-prediction.git
cd heart-level-prediction
```
### 2. Install Dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```
### 3. Run the Application
```bash
Copy
Edit
python app.py
```
Open your browser and go to http://127.0.0.1:5000/ to start using the app.

## 📝 Usage
### 1. Home Page
Provides a short introduction and a button to proceed to the prediction form.

### 2. Input Form
Fill in the required details:

Name: Your full name

Gender: 1 for Male, 2 for Female

Age: Your age in years

Total Cholesterol (TC): Value in mg/dL

HDL Cholesterol: Value in mg/dL

Smoke: 1 if you smoke, otherwise 0

Blood Pressure Medication (BPM): 1 if on medication, otherwise 0

Diabetes: 1 if diabetic, otherwise 0

### 3. Submit the Form
Click Submit to process your inputs and get the predicted risk level.

### 4. Result Page
Displays:

Entered details (name, age, etc.)

Risk score from the model

Categorized risk level: Low, Moderate, or High

## 🎨 Screenshots
Replace these placeholders with actual image links after uploading your screenshots to the repository or an image host.

🏠 Home Page


📝 Input Form

📊 Result Page

📂 File Structure
php
Copy
Edit
heart-level-prediction/
├── app.py                                      # Main Flask application
├── templates/
│   ├── home.html                               # Home page
│   ├── form1.html                              # Input form
│   ├── Details.html                            # Result page
│   └── thankyou.html                           # Thank you page (optional)
├── static/
│   └── styles.css                              # Custom CSS styling
├── myheart_risk_prediction_regression_model.sav # Pre-trained ML model
├── requirements.txt                            # Required Python libraries
└── README.md                                   # Project documentation
🤝 Contributing
Contributions are welcome! 🚀
If you'd like to improve or fix something, follow these steps:


