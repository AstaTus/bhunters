import plotly.graph_objects as go

class VisualizationTool():

    @classmethod
    def plot_kline_candlestick(cls, kline, macd ,):
        """
        蜡烛图
        成交量
        成交额
        MACD
        MA
        筹码分布
        """
        candlestick_trace = {
            'x': kline.time_key,
            'open': kline.open,
            'close': kline.close,
            'high': kline.high,
            'low': kline.low,
            'type': 'candlestick',
            'name': 'MSFT',
            'showlegend': False
        }

        figure = go.Figure(data=[candlestick_trace])
        figure.show()
