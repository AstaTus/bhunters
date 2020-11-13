from ..futu_context import *
from futu import * 
import pandas as pd
class StockManager():
    REQUEST_MAX_COUNT = 1000
    @classmethod
    def get_stock_list_by_plate_code(cls, plate_code, sort_field=SortField.CODE, ascend=True):
        ret, data = FutuContext.instance().get_plate_stock(plate_code, sort_field, ascend)
        if ret == RET_OK:
            return data
        else:
            return None

    @classmethod
    def get_stock_history_kline(cls, code, start=None, end=None, ktype=KLType.K_DAY, autype=AuType.QFQ, fields=[KL_FIELD.ALL], extended_time=False):
        page_req_key = None
        is_frist = True
        total_data = None
        while page_req_key != None or is_frist:
            is_frist = False
            ret, data, page_req_key = FutuContext.instance().request_history_kline(code, start, end, ktype, autype, fields, StockManager.REQUEST_MAX_COUNT, page_req_key, extended_time) # 请求翻页后的数据
            if ret != RET_OK:
                print('error:', data)
            else:
                if total_data == None:
                    total_data = data
                else:
                    total_data.append(data)

        return total_data

                
