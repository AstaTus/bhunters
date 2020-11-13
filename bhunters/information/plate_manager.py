from ..futu_context import *
from futu import * 
class PlateManager():

    @classmethod
    def get_plate_list(cls, market):
        ret, data = FutuContext.instance().get_plate_list(market, Plate.ALL)
        if ret == RET_OK:
            return data
        else:
            return None

