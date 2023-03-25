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
#print(total_files)

#print(data)
# Listing files
files = os.listdir(path2)
# calculating total files
total_files = len(files)
all_files_ids = set(list(range(total_files)))
#print(total_files)

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

ranking = []
for qry in dcg:
    rel = dcg[qry]["rel"]
    ranking.append(rel)

count_irr = ranking.count(0)
count_rel = ranking.count(1)

precsK = []
recallK = []
for k, _ in enumerate(ranking, start=1):
    precsK.append(sum(ranking[:k])/k)
    recallK.append(sum(ranking[:k])/count_rel)
    
plt.plot(recallK, precsK)
#print("done")