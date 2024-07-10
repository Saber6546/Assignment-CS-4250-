# CS4250-Assignment1

## TF-IDF Document-Term Matrix Calculation

### Description
This program reads a collection of documents from a CSV file,
preprocesses the documents by removing stopwords and applying stemming,
computes the tf-idf matrix, and prints the tf-idf values for each term in each document.
### Files
- `indexing.py`: The Python script that reads the file and computes the TF-IDF matrix.
- `collection.csv`: The CSV file containing the documents.

### Usage
To run the program, execute the following command:
```bash
python indexing.py


###Output
Document 1:
love: 0.135
cat: 0.270

Document 2:
loves: 0.366
dog: 0.135

Document 3:
love: 0.101
their: 0.275
dog: 0.101
cat: 0.101
