import re
import os
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# Define the input file containing unparsed messages
input_file = "../Parser/unparsed_messages.txt"

# Read and preprocess the messages
messages = []
with open(input_file, 'r') as file:
    for line in file:
        message = line.strip()
        messages.append(message)

# Use TF-IDF Vectorization to transform the text data into numerical features
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(messages)

# Apply K-means clustering to categorize the messages into different groups
num_clusters = 20  # Adjust this based on the number of clusters you want
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
cluster_labels = kmeans.fit_predict(tfidf_matrix)

# Create output directories for each cluster
output_dir = "clustered_messages"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Store messages in separate files based on their clusters
for cluster_num in range(num_clusters):
    cluster_messages = [messages[i] for i, label in enumerate(cluster_labels) if label == cluster_num]
    cluster_output_file = os.path.join(output_dir, f"cluster_{cluster_num}.txt")
    
    with open(cluster_output_file, 'w') as output_file:
        for message in cluster_messages:
            output_file.write(message + "\n")

print("Messages have been clustered and stored in separate files based on their patterns.")
