from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.cluster import SpectralClustering as SPC
from sklearn.decomposition import PCA
import pandas as pd
import warnings



def KMeansClustering(stock_returns: pd.DataFrame, n_clusters=10, pca=False):
  dataset_array = stock_returns.T.values
  if pca:
    pca_instance = PCA()
    dataset_array = pca_instance.fit_transform(dataset_array)
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

def HierarchicalClustering(stock_returns: pd.DataFrame, n_clusters=10, pca=False):
  dataset_array = stock_returns.T.values
  if pca:
    pca_instance = PCA()
    dataset_array = pca_instance.fit_transform(dataset_array)
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

def SpectralClustering(stock_returns: pd.DataFrame, n_clusters=10, pca=False):
  dataset_array = stock_returns.T.values
  if pca:
    pca_instance = PCA()
    dataset_array = pca_instance.fit_transform(dataset_array)
  print(dataset_array)
  km = SPC(n_clusters=n_clusters)
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
