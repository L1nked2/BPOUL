from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering
import pandas as pd
import warnings

def KMeansClustering(stock_returns: pd.DataFrame, n_clusters=10):
  # PCA
  
  dataset_array = stock_returns.T.values
  print(dataset_array)
  km = KMeans(n_clusters=n_clusters)
  km.fit(dataset_array)
  # Get cluster assignment labels
  labels = km.labels_
  # Format results as a DataFrame
  result = pd.DataFrame([stock_returns.columns,labels]).T
  print(labels)
  print(result)
  return result

def HierarchicalClustering(stock_returns: pd.DataFrame, n_clusters=10):
  dataset_array = stock_returns.T.values
  print(dataset_array)
  km = AgglomerativeClustering(n_clusters=n_clusters)
  km.fit(dataset_array)
  # Get cluster assignment labels
  labels = km.labels_
  # Format results as a DataFrame
  result = pd.DataFrame([stock_returns.columns,labels]).T
  print(labels)
  print(result)
  return result

def SpectralClustering(stock_returns: pd.DataFrame, n_clusters=10):
  dataset_array = stock_returns.T.values
  print(dataset_array)
  km = SpectralClustering(n_clusters=n_clusters)
  km.fit(dataset_array)
  # Get cluster assignment labels
  labels = km.labels_
  # Format results as a DataFrame
  result = pd.DataFrame([stock_returns.columns,labels]).T
  print(labels)
  print(result)
  return result

# DBSCAN?
# OPTICS?
