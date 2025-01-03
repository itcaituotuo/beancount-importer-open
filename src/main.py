# author: 测试蔡坨坨
# datetime: 2024/3/22 0:45
# function: 主入口


from constants.enums import ProviderEnum
from src.accounting.ledger import Ledger
from src.process.bill_file_finder import BillFileFinder


class Main:
    def __init__(self, bill_dir='data/bank_statements'):
        self.bill_dir = bill_dir

    def main(self):
        file_path = BillFileFinder(self.bill_dir).find_files_with_keyword('微信')[0]
        Ledger().parse_bill(ProviderEnum.WECHAT, 18, file_path)

        file_path = BillFileFinder(self.bill_dir).find_files_with_keyword('alipay')[0]
        Ledger().parse_bill(ProviderEnum.ALIPAY, 26, file_path)


if __name__ == '__main__':
    Main().main()
