import logging
import os
# from douban_scrapy import settings
from logging.handlers import RotatingFileHandler
from logging import StreamHandler

# 直接继承logging.Logger 那么就是说这个类就是一个Logger， 有了Logger所有方法
# 只是在类里面添加一些内部方法，让logger 封装addhandler, setformatter等方法
class LogHandler(logging.Logger):
    # 单例模式
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # 一开始居然用了 cls()来实例化 导致无限次调用
            # cls._instance = cls(*args, **kwargs)
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, name, level=logging.DEBUG, to_stream=True, to_file=True):
        self.name = name
        self.level = level
        self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        # 错误的， 继承了logger 本身就是logger 不用再self.logger=xxx 这样变成了一个新的变量
        #self.logger = logging.Logger(name=name, level=level)
        super(LogHandler, self).__init__(name=name, level=level)

        # 写文件
        if to_file:
            self.__setFileHandler__()

        # 写标准输出
        if to_stream:
            self.__setSteamHandler__()

    def __setSteamHandler__(self):
        stream_handler = StreamHandler()
        stream_handler.setFormatter(self.formatter)
        self.addHandler(stream_handler)

    def __setFileHandler__(self):
        log_path = os.path.join(settings.LOG_DIR, self.name +'.log')
        handler = RotatingFileHandler(log_path, maxBytes=1024, backupCount=5)
        handler.setFormatter(self.formatter)
        self.addHandler(handler)
    def __call__(self, *args, **kwargs):
        return self


if __name__ == '__main__':
    logger = LogHandler('scrapy')
    logger2 = LogHandler('scrapy')
    print (logger)
    print((logger2))
    logger.info('haha')
