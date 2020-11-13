from bhunters.information.plate_manager import *
from bhunters.information.plate_key import *

def main():
    plate_list = PlateManager.get_plate_list(Market.HK)
    print(plate_list[PlateKey.PLATE_NAME][0])    # 取第一条的板块名称
    print(plate_list[PlateKey.PLATE_NAME].values.tolist())   # 转为list

if __name__ == '__main__':
    main()