import logging
import threading
import os
from OOP.GzTimedRotatingFileHandler import GzTimedRotatingFileHandler

"""
自定义Logger类
"""
class Logger:

    def __init__(self, loggerName):
        self.__logger = logging.getLogger(loggerName)

        # log_path是存放日志的路径
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/vhallapp/logs/pythonTest'))
        # 如果不存在这个logs文件夹，就自动创建一个
        if not os.path.exists(lib_path):
            os.mkdir(lib_path)
        # 日志文件的地址
        info_logname = "%s/%s_info.log" % (lib_path, loggerName)
        warn_logname = "%s/%s_warn.log" % (lib_path, loggerName)
        error_logname = "%s/%s_error.log" % (lib_path, loggerName)

        # 日志输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(filename)s] [%(levelname)s]: %(message)s')

        # 创建一个FileHandler， 向文件logname输出日志信息
        self.fh_info = GzTimedRotatingFileHandler(filename=info_logname, when="MIDNIGHT", interval=1)
        # 设置日志等级
        self.fh_info.setLevel(logging.INFO)
        # 设置handler的格式对象
        self.fh_info.setFormatter(formatter)
        # 将handler增加到logger中
        self.__logger.addHandler(self.fh_info)

        # 创建一个FileHandler， 向文件logname输出日志信息
        self.fh_warn = GzTimedRotatingFileHandler(filename=warn_logname, when="MIDNIGHT", interval=1)
        # 设置日志等级
        self.fh_warn.setLevel(logging.WARNING)
        # 设置handler的格式对象
        self.fh_warn.setFormatter(formatter)
        # 将handler增加到logger中
        self.__logger.addHandler(self.fh_warn)

        # 创建一个FileHandler， 向文件logname输出日志信息
        self.fh_error = GzTimedRotatingFileHandler(filename=error_logname, when="MIDNIGHT", interval=1)
        # 设置日志等级
        self.fh_error.setLevel(logging.ERROR)
        # 设置handler的格式对象
        self.fh_error.setFormatter(formatter)
        # 将handler增加到logger中
        self.__logger.addHandler(self.fh_error)


    def __del__(self):
        # 关闭打开的文件
        self.fh_info.close()
        self.fh_warn.close()
        self.fh_error.close()

    def info(self, message):
        self.__logger.info(message)

    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)


if __name__ == "__main__":

    logger = Logger("loggertest")

    logger.info("hello it's me")

    logger.error("hello it's me")

    logger.warning("hello it's me")