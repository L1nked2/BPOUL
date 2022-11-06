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

  
  # load raw data and translate to pd.DataFrame()
  def _load_stock_data(self, data):
    self.data = pd.DataFrame(data)
    self.stock_returns = self.data["close"].pct_change()
    return


  def gridsearch(self, method='KMeans'):
    self.feature_stocks = []
    if method == 'KMeans':
      result = cl.KMeansClustering(self.data)
    
    return

  def run_optimization(self):
    self.gridsearch()
    data_selected = self.data[self.feature_stocks]
    # some steps?

    result = op.optimize_portfolio(data_selected, self.feature_stocks)
    return result