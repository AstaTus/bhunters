
class IndicatorsConfig():
    #MA_Type: 0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, 5=TRIMA, 6=KAMA, 7=MAMA, 8=T3 (Default=SMA)
    #TODO 每种均线的解释
    MA_TYPE_SMA     = 0
    MA_TYPE_=EMA    = 1
    MA_TYPE_WMA     = 2
    MA_TYPE_DEMA    = 3
    MA_TYPE_TEMA    = 4
    MA_TYPE_TRIMA   = 5
    MA_TYPE_KAMA    = 6
    MA_TYPE_MAMA    = 7
    MA_TYPE_T3      = 8

    #MACD
    """
    短期
    DIF:快线-快速（一般选12日）移动平均值 - 慢速（一般选26日）移动平均值
    DEA:慢线：DIF的(一般是9)N日EMA
    柱子:计算出的DIF和DEA的数值均为正值或负值。用（DIF-DEA）×2即为MACD柱状图
    """
    MACD_FAST_PERIOD = 12
    MACD_SLOW_PERIOD = 26
    MACD_SIGNAL_PERIOD = 9

    #KDJ

    #Boollinger
    """
    中轨线=N日的移动平均线
    上轨线=中轨线+K倍的标准差
    下轨线=中轨线－K倍的标准差（K为参数，可根据股票的特性来做相应的调整，一般默认为2）
    """
    BOOLLINGER_UP_NBDEV     = 2
    BOOLLINGER_DOWN_NBDEV   = 2





