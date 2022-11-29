import pandas as pd
import warnings
from . import optimization as op
from . import clustering as cl

class StockOptimizer(object):
  def __init__(self, data, asset_num, risk_rate, optional=False, verbose=False, **kwargs):
    self._load_stock_data(data)
    self.asset_num = asset_num
    self.risk_rate = risk_rate
    self.optional = optional
    self.verbose = verbose

  
  # load raw data and preprocess
  def _load_stock_data(self, data):
    self.data = data
    self.stock_close = self.data[0]
    self.stock_returns = self.data[1]
    self.correlation_matrix = self.data[2]
    return


  def gridsearch(self, method='KMeans', pca=False):
    self.feature_stocks = []
    for iter in range(self.asset_num):
      self.feature_stocks.append(None)
    if method == 'KMeans' or method == 'kmeans':
      result = cl.KMeansClustering(self.stock_returns, self.asset_num, pca)
    elif method == 'hierarchical':
      result = cl.HierarchicalClustering(self.stock_returns, self.asset_num)
    elif method == 'spectral':
      result = cl.SpectralClustering(self.stock_returns, self.asset_num)
    for label, content in result.iterrows():
      if self.feature_stocks[content[1]] is None:
        self.feature_stocks[content[1]] = content[0]
    return

  def run_optimization(self, method='KMeans', pca=False):
    self.gridsearch(method=method, pca=pca)
    data_selected = self.stock_returns[self.feature_stocks]
    # some steps? time window size?
    result = op.optimize_portfolio(data_selected, self.feature_stocks)
    if self.verbose:
      return result
    else:
      return result[:2]
