import logging

logger = logging.getLogger()  # 创建日志器
logger.setLevel(logging.DEBUG)  # 设置日志的打印级别
fh = logging.FileHandler(filename="kkk.log", mode='a', encoding="utf-8")  # 创建日志处理器，用文件存放日志
sh = logging.StreamHandler()  # 创建日志处理器，在控制台打印
# 创建格式器，指定日志的打印格式
fmt = logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[Line:%(lineno)d]-[Msg:%(message)s]")
# 给处理器设置格式
fh.setFormatter(fmt=fmt)
sh.setFormatter(fmt=fmt)
# 给日志器添加处理器
logger.addHandler(fh)
logger.addHandler(sh)
# 调用日志器
logger.debug("ajffasfdsas")
