# author: 测试蔡坨坨
# datetime: 2024/1/14 13:02
# function: CSV文件工具类

import csv

import chardet

from src.utils.log_utils import LogUtils


class CSVUtils(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = LogUtils().logger()

    def detect_encoding(self):
        """
        获取文件编码
        :return: encoding
        """
        with open(self.file_path, 'rb') as f:
            result = chardet.detect(f.read())
        file_encoding = result['encoding']
        # self.logger.info(f'文件编码格式: {file_encoding}')
        return file_encoding

    def convert_to_utf8(self):
        """
        编码格式统一utf8
        :return:
        """
        try:
            detected_encoding = self.detect_encoding()
            if (detected_encoding is not None) and (detected_encoding.lower() != 'utf-8'):
                # 源文件
                with open(self.file_path, 'r', encoding=detected_encoding, errors='ignore') as raw_file:
                    csv_content = raw_file.read()
                # 转成utf-8
                with open(self.file_path, 'w', encoding='utf-8') as utf8_file:
                    utf8_file.write(csv_content)
                self.logger.info(f'原文件编码格式：{detected_encoding}，新文件编码格式：utf-8')
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.file_path}")
        except Exception as e:
            self.logger.error(f"Error converting file: {e}")

    def read_csv(self, start_row=1):
        """
        读取csv文件并转换成列表
        :param start_row: 从第N行读起
        :return:
        """
        self.convert_to_utf8()
        data = []
        try:
            with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                # Skip rows until reaching the specified start_row
                for _ in range(start_row - 1):
                    next(csv_reader)
                # Read data from the specified start_row
                for row in csv_reader:
                    # Remove '\t' from each element in the row
                    row = [element.replace('\t', '') for element in row]
                    data.append(row)
        except FileNotFoundError:
            self.logger.error(f'File not found: {self.file_path}')
        except Exception as e:
            self.logger.error(f'Error reading CSV file: {e}')
        return data
