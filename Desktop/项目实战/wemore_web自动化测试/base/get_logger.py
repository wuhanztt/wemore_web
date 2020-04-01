import logging.handlers


class GetLogger:
    logger = None
    @classmethod
    def get_logger(cls):
        #  如果logger为空
        if cls.logger is None:
            #  获取日志器
            cls.logger = logging.getLogger()
            #  设置日志器级别
            cls.logger.setLevel(logging.INFO)
            #  获取处理器控制台
            sh = logging.StreamHandler()
            #  获取处理器文件——以时间分隔
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/wemore.log", when="midnight", interval=1, backupCount=30, encoding="utf_8")
            #  设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            #  将格式器添加到处理器控制台
            sh.setFormatter(fm)
            #  将格式器添加到处理器文件
            th.setFormatter(fm)
            #  将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        #  返回日志器
        return cls.logger


# if __name__ == "__main__":
#     logger = GetLogger().get_logger()
#     logger.info("info信息被执行")
#     logger.error("error信息被执行")