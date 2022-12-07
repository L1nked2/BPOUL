from src import model as md
from src import datacollection as dc
import os.path
import pandas as pd
import csv

data_path_kr = os.path.join('returns_kr.csv')
data_path_na = os.path.join('returns_na.csv')
asset_num = 10
data_kor_raw = [None, None, None]
data_na_raw = [None, None, None]
if os.path.isfile(data_path_kr):
  data_kor_raw[1] = pd.read_csv(data_path_kr)
  data_kor_raw[1].set_index('Date', inplace=True)
else:
  data_kor_raw = dc.get_data(region='KR')
  data_kor_raw[1].to_csv(data_path_kr)

if os.path.isfile(data_path_na):
  data_na_raw[1] = pd.read_csv(data_path_na)
  data_na_raw[1].set_index('Date', inplace=True)
else:
  data_na_raw = dc.get_data(region='NA')
  data_na_raw[1].to_csv(data_path_na)

stock_optimizer = md.StockOptimizer(data=data_na_raw, asset_num=asset_num, risk_rate=0, verbose=True)
result = stock_optimizer.run_optimization(method='kmeans', pca=False)
print(result)
if len(result) > 2:
  with open('sharpe_ratio.csv', 'w', newline='') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',')
      csvwriter.writerow(['sharpe_ratio'])
      for log in result[2]:
        csvwriter.writerow([log[1]])
  with open('risk_return.csv', 'w', newline='') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',')
      csvwriter.writerow(['return', 'risk'])
      for log in result[3]:
        csvwriter.writerow([log[0], log[1]])
