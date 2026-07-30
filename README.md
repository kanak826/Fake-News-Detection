
# 📰 Fake News Detection using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Machine Learning based Fake News Detection System that classifies news articles as **Fake** or **Real** using Natural Language Processing (NLP) and multiple supervised machine learning algorithms.

The project includes a **Streamlit Web Application** for real-time news prediction and demonstrates the complete machine learning workflow from data preprocessing to model deployment.

---

# 📌 Table of Contents

- Overview
- Features
- Technology Stack
- Machine Learning Models
- Project Structure
- Dataset
- Installation
- Training the Model
- Running the Application
- How It Works
- Results
- Future Improvements
- Contributing
- License
- Author

---

# 📖 Overview

The rapid spread of fake news through social media and online platforms has become a serious challenge. This project aims to automatically detect whether a news article is **Fake** or **Real** using Machine Learning and Natural Language Processing techniques.

The application preprocesses news text, converts it into numerical vectors using **TF-IDF Vectorization**, and predicts its authenticity using trained classification models.

---

# ✨ Features

- Detect Fake and Real News
- User-friendly Streamlit Web Interface
- Text Preprocessing using NLP
- TF-IDF Feature Extraction
- Multiple Machine Learning Algorithms
- Fast Prediction
- Easy Model Retraining
- Beginner Friendly Project

# 🛠 Technology Stack

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Regular Expressions (Regex)
- Pickle

---

# 🤖 Machine Learning Models Used

The project compares multiple supervised machine learning algorithms.

| Model | Purpose |
|--------|----------|
| Logistic Regression | Text Classification |
| Decision Tree Classifier | Classification |
| Gradient Boosting Classifier | Ensemble Learning |
| Random Forest Classifier | Ensemble Learning |

---

# 📂 Project Structure

```text
Fake-News-Detection
│
├── app.py
├── train_model.py
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── requirements.txt
├── Fake News Detection using machine learning.ipynb
├── .gitignore
│
├── Datasets/
│
└── screenshots/
```

---

# 📊 Dataset

The model is trained on a labelled dataset consisting of:

- True News Articles
- Fake News Articles

The dataset is preprocessed before training.

Preprocessing includes:

- Lowercase Conversion
- Removing Special Characters
- Removing Punctuation
- Removing URLs
- Tokenization
- TF-IDF Vectorization

---

# 💻 System Requirements

## Hardware

- Intel i3 Processor or above
- 4 GB RAM
- 500 MB Free Storage

## Software

- Python 3.10+
- VS Code / Jupyter Notebook
- Git

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/27abhaymishra/Fake-News-Detection.git
```

Move into project folder

```bash
cd Fake-News-Detection
```

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Train the Model

Run

```bash
python train_model.py
```

This generates

- model.pkl
- vectorizer.pkl

---

# ▶ Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# ⚡ How It Works

1. User enters a news article.
2. Text is cleaned using NLP.
3. TF-IDF converts text into numerical vectors.
4. Trained Machine Learning model predicts.
5. Output is displayed as:

✅ Real News

or

❌ Fake News

---

## Project Screenshots

#### Not a Fake News
![Not a Fake News](https://github.com/kapilsinghnegi/Fake-News-Detection/assets/118688453/3d079c46-118a-4c53-a515-43b9146001c5)

#### Fake News
![Fake News](https://github.com/kapilsinghnegi/Fake-News-Detection/assets/118688453/2f5262f7-801d-4293-824c-13c29fb97fed)

# 📈 Results

The project evaluates different Machine Learning algorithms using:

- Accuracy
- Precision
- Recall
- F1 Score

Among the implemented models, **Logistic Regression** achieved the best overall performance for this dataset.

---

# 📦 Requirements

Example dependencies

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
nltk
```

Install using

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Improvements

- Deep Learning Models (LSTM)
- BERT Based Fake News Detection
- Live News API Integration
- Explainable AI (SHAP)
- Docker Deployment
- Cloud Deployment
- User Authentication

---

# 🤝 Contributing

Contributions are welcome.

1. Fork this repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Abhay Mishra**

GitHub

https://github.com/27abhaymishra

If you found this project useful, don't forget to ⭐ this repository.

---

## ⭐ Show Your Support

If you like this project,

⭐ Star this repository

🍴 Fork it

📢 Share it

Happy Coding ❤️
