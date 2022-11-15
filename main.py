from src import model as md
from src import datacollection as dc


asset_num = 10
data_kor_raw = dc.get_data(region='KR')
print(data_kor_raw[1].columns)
print(data_kor_raw[1]["삼성전자"])
stock_optimizer = md.StockOptimizer(data=data_kor_raw, asset_num=asset_num, risk_rate=0, verbose=True)
stock_optimizer.run_optimization()