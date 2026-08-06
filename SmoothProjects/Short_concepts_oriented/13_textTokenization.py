from sklearn.feature_extraction.text import CountVectorizer

data = [
    "I love machine learning",
    "machine learning is fun",
    "I love coding in Python",
    "Python is great for machine learning",
]

cv = CountVectorizer()
X = cv.fit_transform(data)

print("Vocabulary", cv.vocabulary_)
print("matrix", X.shape)
print("Matrix:\n", X.toarray())