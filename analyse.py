from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

df= pd.read_csv('bank_transactions_data_2.csv')


X = df[['TransactionAmount', 'CustomerAge']]




scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# Add labels to the dataset
df['KMeans_Cluster'] = kmeans_labels


# Calculate distance of each point to its assigned cluster centroid
distances = np.linalg.norm(X_scaled - kmeans.cluster_centers_[kmeans_labels], axis=1)

# Define a threshold (e.g., top 5% farthest from centroids)
threshold = np.percentile(distances, 95)  # Change this value as needed

# Flag points above the threshold as potential frauds
df['Potential_Fraud'] = distances > threshold

# Separate fraudulent and non-fraudulent transactions
frauds = df[df['Potential_Fraud']]
non_frauds = df[~df['Potential_Fraud']]

print(frauds)
print(non_frauds)
#from sklearn.cluster import KMeans
#from sklearn.preprocessing import StandardScaler


#X = df [["AccountID", "CustomerAge" >= 60, "Occupation" = Retired, "TransactionAmount", "TransactionDate",  "TransactionType", "Location", "Channel", "AccountBalance",]]

#ageData = dataFrame.loc[dataFrame['CustomerAge'] >=60, 'AccountID']
#print(ageData)


#scaler = StandardScaler()
#X_scaled = scaler.fit_transform(X)

#kmeans = KMeans(n_clusters=3, random_state)
#kmeans_labels = kmeans