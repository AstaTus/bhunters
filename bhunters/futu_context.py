import threading
from atexit import register
from futu import *

@register
def _exit_callback():
    FutuContext.instance().close()

class FutuContext():
    '''
    todo move to config file
    '''
    FUTU_CONTEXT_HOST = '127.0.0.1'
    FUTU_CONTEXT_POST = 11111

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if not hasattr(FutuContext, "_instance"):
            with FutuContext._instance_lock:
                if not hasattr(FutuContext, "_instance"):
                    FutuContext._instance = OpenQuoteContext(host=FutuContext.FUTU_CONTEXT_HOST, port=FutuContext.FUTU_CONTEXT_POST) 
        return FutuContext._instance
    
    def reset(self):
        '''
        当 context 总是调用失败时，提供重连机制
        '''
        