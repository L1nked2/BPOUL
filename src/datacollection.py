import numpy as np
import pandas as pd
import FinanceDataReader as fdr

def get_data(region='KR'):
  if region == 'KR':
    df_raw = fdr.StockListing('KRX-MARCAP')
    start_date = '2010-12-30'
    end_date = '2021-12-30'
    df_list = []
    num_stocks = 300
    for code in df_raw["Code"][:num_stocks]:
        series_close = fdr.DataReader(code, start_date, end_date, 'KRX')["Close"]
        df_list.append(series_close)
    df_close = pd.concat(df_list, axis=1)
    df_close.columns = df_raw["Name"][:num_stocks]
    df_close = df_close.dropna(axis=1)
    df_returns = df_close.pct_change()
    df_returns = df_returns.iloc[1:, :]
    correlation_matrix = df_returns.corr()
    pd.options.display.float_format = '{:.5f}'.format
  elif region == 'NA':
    df_raw = fdr.StockListing('NASDAQ')
    print(df_raw)
    start_date = '2010-12-30'
    end_date = '2021-12-30'
    df_list = []
    num_stocks = 300
    for code in df_raw["Symbol"][:num_stocks]:
      try:
        series_close = fdr.DataReader(code, start_date, end_date, 'NASDAQ')["Close"]
        df_list.append(series_close)
      except (KeyError, IndexError):
        print(code + " is not available")

    df_close = pd.concat(df_list, axis=1)
    print(df_raw)
    df_close.columns = df_raw["Name"][:len(df_list)]
    df_close = df_close.dropna(axis=1)
    df_returns = df_close.pct_change()
    df_returns = df_returns.iloc[1:, :]
    correlation_matrix = df_returns.corr()
    pd.options.display.float_format = '{:.5f}'.format
  return df_close, df_returns, correlation_matrix