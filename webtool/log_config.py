# -*- coding: UTF-8 -*-
#！usr/bin/python
from webtool.Config import Global_Config
import logging.handlers
# 日志类
class Logger(object):
    LOG_FILE = Global_Config.LOGPATH
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt)   # 实例化formatter
    handler.setFormatter(formatter)      # 为handler添加formatter

    logger = logging.getLogger('log')    # 获取名为tst的logger
    logger.addHandler(handler)           # 为logger添加handler
    logger.setLevel(logging.DEBUG)
    def loginfo(self, message):
        self.logger.info(message)

    def logdebug(self, message):
        self.logger.debug(message)
LOGER=Logger()