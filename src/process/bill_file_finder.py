# @datetime：2024/11/10 23:25
# @author：by caituotuo.top
# @function：账单文件查找

import re
from pathlib import Path

from src.utils.path_utils import PathUtils


class BillFileFinder:
    def __init__(self, directory: str):
        self.dir_path = Path(PathUtils().get_project_path() + directory)

    def find_files_with_keyword(self, keyword="微信"):
        """
        Find CSV files in the directory that contain the specified keyword
        :param keyword: Keyword to search for in the files
        :return: List of CSV files containing the keyword
        """
        keyword_pattern = re.compile(keyword)  # Compile regex pattern

        # Search for matching CSV files
        matching_files = [
            file for file in self.dir_path.glob("*.csv")
            if keyword in file.stem  # Check if keyword is in the file name
        ]
        return matching_files


# Usage example
if __name__ == "__main__":
    finder = BillFileFinder('data/bank_statements')
    matching_files = finder.find_files_with_keyword('alipay')

    for file in matching_files:
        print(file)
