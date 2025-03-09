#!/usr/local/bin/python3.9

import logging

'''
%(asctime)s    -> log time when the event occured
%(levelname)s  -> log level for this record
%(message)s    -> the text content of the log record
%(name)s       -> the name of te logger uesd, default is 'root'
%(pathname)s   -> the full path of the file from which the logger function was called
%(filename)s   -> the file from which the logging function wac called
%(funcName)s   -> the name of the function that calls the logging function
%(lineno)d     -> the line number of the code that calls the logging function
'''

LOG_FORMAT = "时间:%(asctime)s - 日志等级:%(levelname)s - 日志信息:%(message)s"
logging.basicConfig(level=logging.WARNING, format=LOG_FORMAT, filename='test0.log', filemode='w')

logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")


'''    LOGGER   '''
# 创建 Logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建 FileHandler，将日志写入文件
file_handler = logging.FileHandler('test1.log')
file_handler.setLevel(logging.DEBUG)

# 创建 Formatter，定义日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将 FileHandler 添加到 Logger
logger.addHandler(file_handler)

# 记录日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')


'''    LOGGER  将日志输出到控制台  '''
# 创建 Logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建 FileHandler，将日志写入文件
file_handler = logging.FileHandler('test2.log')
file_handler.setLevel(logging.DEBUG)

# 创建 Formatter，定义日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 创建 StreamHandler，将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# 将 Handler 添加到 Logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
