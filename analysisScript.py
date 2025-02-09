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

# Perform hierarchical clustering to group preambles
from sklearn.cluster import AgglomerativeClustering
clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=1.0, metric='precomputed', linkage='complete')
clusters = clustering.fit_predict(1 - cosine_sim_matrix)  # Convert similarity to distance
# Assign clusters
preamble["Cluster"] = clusters
print(preamble.head(15))
# Clustering performed successfully

# Visualize the clusters
sns.heatmap(cosine_sim_matrix, xticklabels=preamble["C ountry"], yticklabels=preamble["C ountry"], cmap="coolwarm")
plt.title("Constitutional Preamble Similarity")
plt.show()
# Very poor visualization produced