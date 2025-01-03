# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨
# 时间：2022/3/12 20:50
# 功能：路径相关

import os


class PathUtils:
    def get_project_path(self):
        """
        获取项目根路径 F:\Desktop\Heson_Files\beancount\beancount-importer\
        @return:
        """
        # 获取当前文件的绝对路径
        current_file = os.path.abspath(__file__)
        # 返回当前文件所在的目录的父目录的父目录，即src目录外层的目录
        return os.path.dirname(os.path.dirname(os.path.dirname(current_file))) + '/'


if __name__ == '__main__':
    print(PathUtils().get_project_path())
