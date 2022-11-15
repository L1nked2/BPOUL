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


  def gridsearch(self, method='KMeans'):
    self.feature_stocks = []
    if method == 'KMeans':
      result = cl.KMeansClustering(self.stock_returns, self.asset_num)
    
    return

  def run_optimization(self, method='KMeans'):
    self.gridsearch(method=method)
    data_selected = self.stock_returns[self.feature_stocks]
    # some steps? time window size?

    result = op.optimize_portfolio(data_selected, self.feature_stocks)
    return result