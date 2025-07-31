# 📧 Spam Detection Model with Flask Web App

A simple but powerful machine learning project to detect spam messages using natural language processing (NLP) techniques. The project includes a fully functional **Flask web app** that allows users to interact with the model in real time.

---

## 🚀 Project Overview

This project uses a dataset of labeled SMS messages to train a model that can classify whether a message is **Spam** or **Not Spam**. It involves text preprocessing, feature extraction, model training, evaluation, and real-time prediction via a web interface.

---

## 🧠 Features

- ✅ Text preprocessing (e.g., removing stopwords, punctuation, etc.)
- ✅ Feature extraction using `CountVectorizer` or `TF-IDF`
- ✅ Model training with Logistic Regression or Naive Bayes
- ✅ Evaluation using Accuracy, Precision, Recall, and F1-score
- ✅ Real-time message prediction via web form
- ✅ Flask-based UI for non-technical users

---

## 🛠️ Tech Stack

### 🔤 Machine Learning & NLP
- Python 3
- scikit-learn
- pandas
- NumPy
- NLTK
- `re` (regex for text cleaning)

### 🌐 Web Application
- Flask
- Jinja2 templating
- Bootstrap 4 (for responsive UI)

---

## 📁 Project Structure

spam_detection_project/
├── app.py # Main Flask application
├── prediction.py # Preprocessing, vectorization, prediction functions
├── model.pkl # Trained ML model (if pickled)
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Web form and result display
├── static/
│ └── main.css # Optional custom CSS
└── README.md # Project documentation


---

## 🌐 Web App (Flask UI)

The Flask app allows users to input a message and get an instant classification. Here's how it works:

1. **Input**: User types a message into the text box.
2. **Backend**: The message is preprocessed, vectorized, and passed to the trained model.
3. **Prediction**: The model returns whether the message is spam or not.
4. **Output**: Result is displayed on the same page.


---

## ▶️ How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/UDLHS/spam_detection_project.git
cd spam-detection-flask
```

### 2. Set Up Virtual Environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Server

```bash
python app.py
```

### 5. Access the App

Open your browser and visit:
```cpp
http://127.0.0.1:5000/
```

## 🧪 Sample Predictions

| Input Message                                                                 | Prediction |
|------------------------------------------------------------------------------|------------|
| "Congratulations! You've won a $1000 Walmart gift card. Click here now!"     | Spam       |
| "Can we meet tomorrow at 2PM?"                                               | Not Spam   |
| "You’ve been selected for a free cruise to the Bahamas. Reply YES to claim."| Spam       |
| "I'll call you in the evening to discuss the project."                       | Not Spam   |
| "URGENT! Your account has been compromised. Click here to verify your ID."  | Spam       |



---

Let me know if:
- You want a short version
- You want me to generate a `requirements.txt`
- You want deployment instructions included (e.g., for Render, Heroku)

I'm here to help make this project portfolio-ready!
