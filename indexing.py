#-------------------------------------------------------------------------
# AUTHOR: Ethan Ko
# FILENAME: indexing.py
# SPECIFICATION: This program reads a collection of documents from a CSV file,
# preprocesses the documents by removing stopwords and applying stemming,
# computes the tf-idf matrix, and prints the tf-idf values for each term in each document.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 8 hours 
#-----------------------------------------------------------*/

import csv
import math
from collections import defaultdict

# Reading data from CSV file
documents = []
with open('D:/Python/CS 4250/collection.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])

# Stopwords and stemming
stopWords = {'i', 'you', 'he', 'she', 'it', 'we', 'they', 'and', 'or', 'but', 'her'}
stemming = {'cats': 'cat', 'dogs': 'dog', 'loves': 'love'}  # Simplified stemming example

# Function to preprocess a document
def preprocess(document):
    words = document.lower().split()
    words = [stemming[word] if word in stemming else word for word in words if word not in stopWords]
    return words

# Identify index terms
terms = sorted(set().union(*[preprocess(doc) for doc in documents]))  # Sorting terms alphabetically

# Build document-term matrix
docTermMatrix = []

# Compute term frequencies (tf) for each document
tf_matrix = []
for doc in documents:
    words = preprocess(doc)
    tf_vector = defaultdict(float)
    total_words = len(words)
    for term in terms:
        tf_vector[term] = words.count(term) / total_words
    tf_matrix.append(tf_vector)

# Compute inverse document frequency (idf)
idf_vector = {}
N = len(documents)
for term in terms:
    df = sum(1 for doc in documents if term in preprocess(doc))
    idf_vector[term] = math.log(N / (df + 1))  # Using (df + 1) to avoid division by zero

# Compute tf-idf matrix
docTermMatrix = []
for tf_vector in tf_matrix:
    tfidf_vector = {term: tf * idf_vector[term] for term, tf in tf_vector.items()}
    docTermMatrix.append(tfidf_vector)

# Print the document-term matrix in the desired format
# Print header with extended border line
print('-' * 67)
print(f"| {'Document':<12} | {'cat':<10} | {'dog':<10} | {'love':<10} | {'loves':<10} |")
print('-' * 67)

# Print each document row with extended border line
for i, vector in enumerate(docTermMatrix):
    row = [f"Document {i + 1}"]
    row += [f"{vector.get(term, 0):.4f}" for term in terms]
    print(f"| {row[0]:<12} | {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10} |")
    print('-' * 67)


