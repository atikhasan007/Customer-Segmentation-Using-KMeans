Workflow Summary
Data Preprocessing:
Load customer data and select relevant features such as age, spending, visits, and promotion interest.

Standard Scaling:
Normalize the feature values using StandardScaler to ensure fair contribution of all features.

Dimensionality Reduction with PCA:
Apply PCA to reduce feature dimensions from many to 2 for better clustering and visualization.

KMeans Clustering (k=4):
Initialize and fit the KMeans algorithm with n_clusters=4 to segment customers into 4 groups.

Cluster Prediction:
Assign each customer to one of the 4 clusters based on proximity to the cluster centroids.

Silhouette Score Evaluation:
Calculate silhouette score to measure how well-separated and meaningful the clusters are.

Model Saving with Pickle:
Save the trained KMeans model using Python’s pickle for future prediction in a Streamlit web app.

Web Interface with Streamlit:
Build an interactive web app to input customer data and predict their cluster group in real-time.

✅ Tools & Libraries Used
pandas, numpy – for data handling and numerical operations

scikit-learn – for scaling, PCA, clustering, and evaluation

pickle – to save and load the trained KMeans model

streamlit – for building a user-friendly web interface

