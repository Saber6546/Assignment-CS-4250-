#-------------------------------------------------------------------------
# AUTHOR: Ethan Ko
# FILENAME: indexing.py
# SPECIFICATION: This program reads a collection of documents from a CSV file,
# preprocesses the documents by removing stopwords and applying stemming,
# computes the tf-idf matrix, and prints the tf-idf values for each term in each document.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 4 hours 
#-----------------------------------------------------------*/

import csv
import math
from collections import defaultdict

# Reading data from CSV file
documents = []
with open('D:/Python/CS 4250/collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])

# Stopwords and stemming (simplified)
stopWords = {'i', 'you', 'he', 'she', 'it', 'we', 'they', 'and', 'or', 'but'}
stemming = {'cats': 'cat', 'dogs': 'dog'}  # Simplified stemming example

# Function to preprocess a document
def preprocess(document):
    words = document.lower().split()
    words = [stemming[word] if word in stemming else word for word in words if word not in stopWords]
    return words

# Identify index terms
terms = set()
for doc in documents:
    terms.update(preprocess(doc))

terms = sorted(terms)  # Sorting terms alphabetically

# Build document-term matrix
docTermMatrix = []
tf_matrix = []

# Compute term frequencies (tf) for each document
for doc in documents:
    words = preprocess(doc)
    tf_vector = defaultdict(float)
    for term in words:
        tf_vector[term] += 1 / len(words)
    tf_matrix.append(tf_vector)

# Compute inverse document frequency (idf)
idf_vector = {}
for term in terms:
    df = sum(1 for doc in documents if term in preprocess(doc))
    idf_vector[term] = math.log(len(documents) / df)

# Compute tf-idf matrix
for tf_vector in tf_matrix:
    tfidf_vector = {term: tf * idf_vector[term] for term, tf in tf_vector.items()}
    docTermMatrix.append(tfidf_vector)

# Print the document-term matrix
for i, vector in enumerate(docTermMatrix):
    print(f"Document {i + 1}:")
    for term, tfidf in vector.items():
        print(f"{term}: {tfidf:.3f}")
    print()
