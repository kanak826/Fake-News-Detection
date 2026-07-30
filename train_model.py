import pandas as pd
import string
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# LOAD DATASETS

fake_data = pd.read_csv('Datasets/Fake.csv')
true_data = pd.read_csv('Datasets/True.csv')

# LABELS

fake_data['class'] = 0
true_data['class'] = 1

# COMBINE DATA

data = pd.concat([fake_data, true_data])

# KEEP REQUIRED COLUMNS

data = data[['text', 'class']]

# CLEAN TEXT FUNCTION

def clean_text(text):

    text = text.lower()

    text = ''.join(
        char for char in text
        if char not in string.punctuation
    )

    return text

# CLEAN DATA

data['text'] = data['text'].apply(clean_text)

# SPLIT DATA

x = data['text']
y = data['class']

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42
)

# TF-IDF
vectorizer = TfidfVectorizer(
    stop_words='english',
    max_df=0.7,
    min_df=2
)

xv_train = vectorizer.fit_transform(x_train)

# TRAIN MODEL

model = LogisticRegression(
    max_iter=1000
)

model.fit(xv_train, y_train)

# SAVE MODEL

pickle.dump(
    model,
    open("model.pkl", "wb")
)

pickle.dump(
    vectorizer,
    open("vectorizer.pkl", "wb")
)

print("Model Saved Successfully")