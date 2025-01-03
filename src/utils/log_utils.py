# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨
# 时间：2022/3/16 20:10
# 功能：日志模块封装

import logging
import os
import time
from logging import handlers

from src.utils.path_utils import PathUtils


class LogUtils(object):
    @classmethod
    def logger(cls):
        # 不会打印 HTTP General 信息
        log = logging.getLogger(__name__)
        # log = logging.getLogger()
        # 日志级别关系映射
        level_relations = {
            'NOTSET': logging.NOTSET,
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }

        # 日志存储目录
        reports_dir = PathUtils().get_project_path() + 'reports'
        if not os.path.exists(reports_dir):
            os.mkdir(reports_dir)
        logs_dir = PathUtils().get_project_path() + "reports/logs"
        if not os.path.exists(logs_dir):
            os.mkdir(logs_dir)
        # 日志文件根据日期命名
        log_file_name = "%s.log" % time.strftime("%Y-%m-%d", time.localtime())
        log_file_path = os.path.join(logs_dir, log_file_name)

        rotating_file_handler = handlers.TimedRotatingFileHandler(filename=log_file_path,
                                                                  when='D',  # 按天分隔，一天一个文件
                                                                  interval=30,
                                                                  encoding='utf-8')

        # 日志输出格式
        fmt = "%(asctime)s %(levelname)s %(pathname)s %(lineno)d %(message)s"
        # fmt = "%(name)s %(asctime)s %(created)f %(relativeCreated)d %(msecs)d %(levelname)s %(levelno)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d %(process)d %(thread)d %(threadName)s %(message)s"
        formatter = logging.Formatter(fmt)
        rotating_file_handler.setFormatter(formatter)

        # 加上判断，避免重复打印日志
        if not log.handlers:
            # 控制台输出
            console = logging.StreamHandler()
            console.setLevel(level_relations["NOTSET"])
            console.setFormatter(formatter)
            # 写入日志文件
            log.addHandler(rotating_file_handler)
            log.addHandler(console)
            log.setLevel(level_relations['DEBUG'])
        return log
