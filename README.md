# 🔧 AI-Powered Predictive Maintenance for IoT Devices

## 📌 Overview

This project is an **end-to-end AI-powered predictive maintenance system** that predicts machine failures using IoT sensor data such as **temperature, vibration, and current**.

The system leverages **Machine Learning** to identify patterns and detect potential failures before they occur, helping industries reduce downtime and maintenance costs.

---

## 🎯 Problem Statement

Traditional maintenance is:

* Reactive (fix after failure)
* Expensive
* Causes downtime

This project solves it by:

* Predicting failures in advance
* Enabling proactive maintenance
* Improving operational efficiency

---

## 🏭 Industry Relevance

This solution is widely used in:

* Manufacturing plants
* Automotive industry
* Power plants
* Aviation systems
* Smart factories (Industry 4.0)

Companies like **Siemens, GE, Bosch, IBM, Tesla** use similar systems.

---

## ⚙️ Tech Stack

* **Programming:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Random Forest)
* **Visualization:** Matplotlib
* **Dashboard:** Streamlit
* **Model Storage:** Joblib

---

## 🧠 Project Architecture

```
IoT Sensor Data → Data Preprocessing → Feature Engineering
        ↓
   Machine Learning Model (Random Forest)
        ↓
   Failure Prediction (0 / 1)
        ↓
   Streamlit Dashboard (Visualization + Alerts)
```

---

## 📂 Project Structure

```
AI-Predictive-Maintenance-IoT/
│
├── data/                     # Dataset (sensor readings)
├── src/                      # Source code
│   ├── data_loader.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   ├── prediction.py
│   └── app_streamlit.py
│
├── models/                   # Trained model (excluded from GitHub)
├── outputs/                  # Graphs & results
├── images/                   # Screenshots for README
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Features

* ✅ Data preprocessing & cleaning
* ✅ Feature engineering
* ✅ Machine learning model training
* ✅ Model evaluation (Accuracy, Confusion Matrix)
* ✅ Real-time prediction
* ✅ Interactive Streamlit dashboard
* ✅ KPI metrics (Failure rate, total records)
* ✅ Business decision insights

---

## 📈 Sample Outputs

### 🔹 Dashboard

* KPI Metrics
* Dataset Preview
* Sensor Inputs
* Prediction Result

### 🔹 Visualizations

* Temperature vs Failure
* Vibration vs Failure
* Current vs Failure

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/AI-Predictive-Maintenance-IoT.git
cd AI-Predictive-Maintenance-IoT
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Train Model

```
python src/model_training.py
```

### 5️⃣ Run Dashboard

```
streamlit run src/app_streamlit.py
```

---

## ⚠️ Note

The trained model file (`.pkl`) is not uploaded due to GitHub size limitations.

To generate the model:

```
python src/model_training.py
```

---

## 📸 Screenshots (Add Here)

* Dashboard UI
* Prediction Output
* Graphs

---

## 📚 Learning Outcomes

* End-to-end ML pipeline development
* Real-world problem solving
* Data preprocessing & feature engineering
* Model building & evaluation
* Dashboard development using Streamlit
* GitHub project structuring

---

## 👩‍💻 Author

**Asma Khanum**
Aspiring Data Engineer | AI & Analytics Enthusiast

---

## 🙏 Acknowledgment

Special thanks to mentors and industry experts for guidance and support throughout the project.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
