# Make sure to change environment to conda (Command Palette)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
preamble = pd.read_csv('/Users/vaibhavjha/DS4002projects/preambles_data.csv')
print(preamble.head())
# Uploaded successfully

# Install necessary packages for feature selection
# pip install sentence-transformers scikit-learn numpy
# pip install transformers torch sentencepiece

# Extracting features from the text
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
texts = preamble['P reamble'].tolist()
embeddings = model.encode(texts, convert_to_numpy=True)
print(embeddings.shape)
# Embeddings produced successfully

# Get cosine-similarity measure on embeddings
# Install: pip install sentence-transformers scikit-learn numpy
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim_matrix = cosine_similarity(embeddings)
print("Cosine Similarity Matrix:\n", cosine_sim_matrix)
# Cosine Similarity Matrix produced successfully

## Dendogram for cut-off
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
# Compute linkage matrix
linkage_matrix = sch.linkage(embeddings, method='ward')  # Try 'average' or 'complete' instead of 'ward'
# Plot dendrogram
plt.figure(figsize=(10, 6))
dendrogram = sch.dendrogram(linkage_matrix)
plt.axhline(y=1, color='r', linestyle='--')  # Example threshold
plt.show()
# Dendogram produced successfully. Chose cut-off at y = 1.

# Perform hierarchical clustering to group preambles
from sklearn.cluster import AgglomerativeClustering
clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0.4, metric='precomputed', linkage='complete')
clusters = clustering.fit_predict(1 - cosine_sim_matrix)  # Convert similarity to distance
# Assign clusters
preamble["Cluster"] = clusters
print(preamble.head(15))
# Clustering performed successfully

# Export clusters to a CSV file
preamble.to_csv("preambles_clusters.csv")

# Evaluation of clusters
"""
from wordcloud import WordCloud

preamble['Cluster'] = clusters  

for cluster_id in np.unique(clusters):
    texts = " ".join(preamble[preamble['Cluster'] == cluster_id]['P reamble'])

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(texts)
    
    plt.figure(figsize=(12, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.xticks(rotation=90, fontsize=8)  
    plt.yticks(rotation=0, fontsize=8)  
    plt.title(f"Cluster {cluster_id}")
    plt.show()

# Getting error for Cluster 1 word cloud: "float found"

"""

# Silhouette Score
# Ranges from -1 to 1, with 1 being well-clustered, 0 being overlapping clusters, and -1 being misclustered
from sklearn.metrics import silhouette_score
silhouette_avg = silhouette_score(embeddings, clusters)
print(f"Silhouette Score: {silhouette_avg:.3f}")