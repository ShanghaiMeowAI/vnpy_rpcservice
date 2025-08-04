import multiprocessing
import sys
from time import sleep
from datetime import datetime, time
from logging import INFO

from vnpy.event import EventEngine
from vnpy.trader.setting import SETTINGS
from vnpy.trader.engine import MainEngine

# from vnpy_ctp import CtpGateway
# from vnpy_ctastrategy import CtaStrategyApp
from vnpy_rpcservice import RpcGateway
# from vnpy_ctastrategy.base import EVENT_CTA_LOG


SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True



# Chinese futures market trading period (day/night)
# DAY_START = time(8, 45)
# DAY_END = time(15, 0)

# NIGHT_START = time(20, 45)
# NIGHT_END = time(2, 45)



def run():
    """
    Running in the child process.
    """
    SETTINGS["log.file"] = True

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(RpcGateway)

    setting = RpcGateway.default_setting


    try:
        main_engine.connect(setting, "RPC")
        
        print("RPC 连接成功！")
    except Exception as e:
        print(f"RPC 连接异常: {e}")
    
    sleep(5)


if __name__ == '__main__':
    run()
    print('end')