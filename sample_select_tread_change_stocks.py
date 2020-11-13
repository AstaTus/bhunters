from bhunters.information.plate_manager import *
from bhunters.information.plate_key import *
from bhunters.information.stock_manager import *
from bhunters.table.table_manager import *
from bhunters.visualization.visualization_tool import *

import numpy as np
import talib


def main():
    TableManager.set_show_all_rows_and_columns()
    plate_list = PlateManager.get_plate_list(Market.HK)
    print(plate_list[PlateKey.PLATE_NAME][0])    # 取第一条的板块名称
    print(plate_list[PlateKey.PLATE_NAME].values.tolist())   # 转为list
    stock_kline = StockManager.get_stock_history_kline('HK.01302')
    print(stock_kline)
    # VisualizationTool.plot_kline_candlestick(stock_kline)
    close =np.random.random(100)
    output = talib.SMA(close)
    #kdj
    # talib.STOCH()
    print(output)
if __name__ == '__main__':
    main()