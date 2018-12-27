from webtool.Config import Global_Config
import logging.handlers

# 日志类
class Logger():
    LOG_FILE = Global_Config.LOGPATH
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
    fmt = '%y-%m-%d_%H.%M.%S'


    formatter = logging.Formatter(fmt)   # 实例化formatter
    handler.setFormatter(formatter)      # 为handler添加formatter

    logger = logging.getLogger('log')    # 获取名logger
    logger.addHandler(handler)           # 为logger添加handler
    logger.setLevel(logging.DEBUG)
    def loginfo(self, message):
        self.logger.info(message)

    def logdebug(self, message):
        self.logger.debug(message)