
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("sentiment_dataset.csv")
texts = df["text"].tolist()
labels = df["label"].tolist()

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

while True:
    print("This is a program to classify sentences as positive or negative")
    user_input = input("Enter a sentence to analyze sentiment: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye 👋")
        break
    new_X = vectorizer.transform([user_input])
    prediction = model.predict(new_X)
    print(f"Predicted sentiment: {prediction[0]}")
