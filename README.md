To solve the 1st problem, the following steps were followed:
Perform the same preprocessing steps as in Assignment 1 to clean and tokenise the data.
Create a TF-IDF matrix of size (no. of documents x vocab size) by following the below steps:
a. Compute the frequency count of each term in every document and store it as a nested dictionary for each document.
b. Determine the document frequency of each term by finding the postings list of each term and counting the number of documents in each posting list.
c. Calculate the IDF value of each term using the following formula with smoothing: IDF(term) = log(total number of documents/document frequency(term)+1).

Construct the query vector of size vocab by cleaning and tokenizing the query.
Compute the TF-IDF score for the query using the TF-IDF matrix by taking the dot product of the query vector and the TF-IDF matrix for each weighting scheme.
Report the top 5 relevant documents based on the TF-IDF score.
Present the TF-IDF score and results for each weighting scheme separately, and state the pros and cons of using each weighting scheme to determine the relevance of documents in the report.
To determine the Jaccard coefficient between a specified query and a document, the following steps need to be followed:
Preprocess the given dataset by cleaning and tokenizing the data.
Create sets of the document and query tokens.
Compute the intersection and union for each document and the query.
Calculate the Jaccard coefficient using the provided formula: Jaccard Coefficient = Intersection of (doc, query) / Union of (doc, query).
Rank the documents based on their Jaccard coefficient value and report the top 10 documents.
Pros and Cons of Weighting Schemes:
Binary: This scheme only considers the presence or absence of a term in a document and ignores the frequency of occurrence. It is simple to compute and works well for short documents. However, it may need to capture the importance of terms that occur frequently in long documents.
Raw Count: This scheme considers the frequency of occurrence of a term in a document. It works well for long documents and captures the importance of frequently occurring terms. However, it may be biased towards longer documents.
Term Frequency: This scheme normalizes the frequency of occurrence of a term by the total number of terms in the document. It works well for long documents and captures the importance of frequently occurring terms, while reducing the bias towards longer documents. However, it may need to capture the importance of rare terms.
Log Normalization: This scheme normalizes the frequency of occurrence of a term by taking the logarithm of the frequency count. It works well for long documents and captures the importance of terms that frequently occur, while reducing the impact of extremely frequent terms. However, it may not capture the importance of rare terms.
Double Normalization: This scheme normalises the frequency of occurrence of a term by the maximum frequency of any term in the document. It works well for long documents and captures the importance of frequent terms while reducing the impact of extremely frequent terms. It also normalises the document length. However, it may need to capture the importance of rare terms.
Overall, the best weighting scheme depends on the nature of the problem and the characteristics of the documents.

To solve the 2nd problem, the following steps were followed:

Implementing Naive Bayes classifier with TF-ICF weighting scheme for classifying news articles into predefined categories.
Preprocessing of the dataset includes removing unnecessary columns, cleaning text, tokenising text, stemming or lemmatising, and implementing the TF-ICF weighting scheme.
The dataset is split into a 70:30 ratio for training and testing, respectively.
The naive Bayes classifier is trained using the TF-ICF weighting scheme, and the probability of each category and feature gave each category is calculated.
The classifier's performance is evaluated using a testing set, and metrics such as accuracy, precision, recall, and F1 score are calculated.\
Classifier is improved through experimentation with different preprocessing techniques, parameters, and features.
Experiments include different splits and features like n-grams or TF-IDF weights.

To solve the 3rd problem, the following steps were followed:

Task: Rearrange query-url pairs in order of maximum DCG
Focus only on queries with qid:4 and use relevance judgement labels as relevance score
Create a file that rearranges query-url pairs in order of maximum DCG
Mention the number of such files that could be made
Task: Compute nDCG for the dataset
Calculate nDCG at position 50 and for the entire dataset
Use relevance judgement labels and DCG to compute nDCG
Explain the importance of nDCG as an evaluation metric for information retrieval systems
Task: Plot Precision-Recall curve for the query "qid:4"
Assume a model that ranks URLs based on the value of feature 75
Feature 75 represents the sum of TF-IDF on the whole document
URLs with higher feature 75 values are considered more relevant
Any non-zero relevance judgement value is considered relevant
Use the model to plot a Precision-Recall curve for the query "qid:4"

