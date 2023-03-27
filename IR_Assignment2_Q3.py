#!/usr/bin/env python
# coding: utf-8

# In[20]:


from collections import Counter 
import os
import numpy as np
import matplotlib.pyplot as plt
path = "C:\\Users\\91783\\Desktop\\IR 2023\\assignment2\\practice folder\\IR-assignment-2-data.txt"
path2 = "C:\\Users\\91783\\Desktop\\IR 2023\\assignment2\\practice folder\\"

with open(path, 'r') as data:
    data = data.readlines()
# Listing files
files = os.listdir(path2)
# calculating total files
total_files = len(files)
print(total_files)


# In[21]:


#print(data)
# Listing files
files = os.listdir(path2)
# calculating total files
total_files = len(files)
all_files_ids = set(list(range(total_files)))
print(total_files)


# In[22]:



i = 0
relevance = []
while i <= len(data) - 1:
    if data[i].split()[1] != "qid:4": 
        del data[i]
    else:
        relevance.append(int(data[i].split()[0]))
        i += 1
relevance_counter = dict(Counter(relevance))
dcg = {}
for line_idx, line in enumerate(data):
    dcg[line_idx] = {}
    line = line.split()
    dcg[line_idx]["rel"] = int(line[0])
    dcg[line_idx]["id"] = line[1]
    #dcg[line_idx]["query_url"] = {int(query_url.split(":")[0]): float(query_url.split(":")[1]) for query_url in line[2:]}
    query_url_parts = [query_url.split(":") for query_url in line[2:]]
    query_url_dict = {int(parts[0]): float(parts[1]) for parts in query_url_parts}
    dcg[line_idx]["query_url"] = query_url_dict


# In[23]:


# Set the number of items to consider
num_items = min(50, len(dcg))

# Get the top relevance scores
top_rel = np.array(relevance[:num_items])

# Compute the logs for the denominator
denominator = np.log2(range(2, num_items + 1))
denominator = np.insert(denominator, 0, 1)

# Compute the DCG and IDCG scores
dcg_score = np.sum(top_rel / denominator)
idcg_score = np.sum(np.sort(top_rel)[::-1] / denominator)

# Compute the nDCG score
ndcg_score = dcg_score / idcg_score


# In[37]:


# Read the data from a file
#filepath = "path/to/file.txt"
with open(path) as f:
    data = f.readlines()
while i <= len(data) - 1:
    if data[i].split()[1] != "qid:4": 
        del data[i]

# Define a function to parse the data and return relevant scores and labels
def parse_data(data):
    scores = []
    labels = []
    for line in data:
        # Split the line into its components
        parts = line.strip().split()
        # Extract the label, relevance score, and feature 75
        label = int(parts[0])
        score = int(parts[1].split(":")[1])
        feature_75 = float(parts[74].split(":")[1])
        # Keep track of the score and label if the relevance score is non-zero
        if score != 0:
            scores.append(feature_75)
            labels.append(label)
    return scores, labels

# Parse the data
scores, labels = parse_data(data)

# Define a function to compute precision and recall for a given threshold
def compute_precision_recall(scores, labels, threshold):
    # Determine which labels are considered relevant for the given threshold
    relevant_labels = set([label for label, score in zip(labels, scores) if score >= threshold])
    # Compute the true positives, false positives, and false negatives
    true_positives = len(relevant_labels)
    false_positives = len(scores) - true_positives
    false_negatives = len(set(labels)) - true_positives
    # Compute precision and recall
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    return precision, recall

# Compute the precision and recall for a range of thresholds
thresholds = sorted(scores, reverse=True)
precisions = []
recalls = []
print("step 1")
for threshold in thresholds:
    precision, recall = compute_precision_recall(scores, labels, threshold)
    precisions.append(precision)
    recalls.append(recall)
print("step 2")

# Plot the precision-recall curve
plt.plot(recalls, precisions)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()


# In[ ]:





# In[ ]:




