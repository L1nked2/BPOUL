import numpy as np
import pandas as pd

# hyperparameters for the montecarlo simulation
MAX_LOOP_MONTE = 3000
# hyperparameters for the gradient descent
MAX_LOOP_GRAD = 1000
DELTA_DEFAULT = 0.1
MINIMUM_DELTA_RATIO = 0.1
DELTA_DECAY_RATIO = 0.5
IMPROVEMENT_THRESHOLD = 0.0001

# gets raw_data(closing price) and weights
# returns the mean_daily_return
def calc_mean_returns(raw_data: pd.DataFrame, weights: np.array):
  stock_returns = raw_data.mul(pd.Series(weights))
  mean_returns = stock_returns.sum(axis=1)
  return mean_returns

# gets the daily mean returns data
# calculate sharpe_ratio, sqrt(252) for annual sharpe ratio
# meaning 252 trading days in a year
def calc_sharpe_ratio(mean_returns: pd.DataFrame):
  assert len(mean_returns.columns) == 1
  sharpe_ratio = (252**0.5) * mean_returns.mean() / mean_returns.std()
  return sharpe_ratio

# optimize portfolio using sharpe ratio, method defines way to optimize
# raw_data includes only closing price, indexed by date and columns matches exactly with feature_stocks
def optimize_portfolio(raw_data: pd.DataFrame, feature_stocks: pd.Series, method='gradient'):
  # initialize values
  assert len(raw_data) == len(feature_stocks)
  assert len(raw_data.columns) == len(feature_stocks)
  num_stocks = len(raw_data.columns)
  current_weights = np.array(np.random.random(num_stocks))
  current_weights /= current_weights.sum()
  # optimization loops
  if method == 'montecarlo' or method == 'monte':
    # montecarlo optimization
    pass
  elif method == 'grad' or method == 'gradient':
    # gradient descent optimization
    current_delta = DELTA_DEFAULT
    for iter in range(MAX_LOOP_GRAD):
      current_mean_returns = calc_mean_returns(raw_data, current_weights)
      current_sharpe_ratio = calc_sharpe_ratio(current_mean_returns)
      best_sharpe_ratio = current_sharpe_ratio
      # grid search
      for target_stock_index in range(num_stocks):
        new_weights = current_weights.copy()
        new_weights[target_stock_index] += current_delta
        new_weights /= np.sum(new_weights)
        new_mean_returns = calc_mean_returns(raw_data, new_weights)
        new_sharpe_ratio = calc_sharpe_ratio(new_mean_returns)
        if new_sharpe_ratio > best_sharpe_ratio:
          best_sharpe_ratio = new_sharpe_ratio
          best_weights = new_weights
      improvement = best_sharpe_ratio - current_sharpe_ratio
      if improvement < IMPROVEMENT_THRESHOLD:
          # stop search if there's no improvement and delta is small enough
          # or decay delta and search again
          if current_delta < MINIMUM_DELTA_RATIO * DELTA_DEFAULT:
            break
          else:
            current_delta = current_delta * DELTA_DECAY_RATIO
      current_weights = best_weights
  return best_weights, best_sharpe_ratio

