# author: 测试蔡坨坨
# datetime: 2024/3/22 1:39
# function: 记账

import os
import re
from datetime import datetime

from constants.enums import ProviderEnum
from src.accounting.parsers import Parsers
from src.accounting.rules import Rules
from src.utils.csv_utils import CSVUtils
from src.utils.log_utils import LogUtils
from src.utils.path_utils import PathUtils


class Ledger(object):
    def __init__(self):
        self.logger = LogUtils().logger()
        self.rules_wechat = [Parsers.generator_rule(*pattern) for pattern in Rules.wechat_rules]
        self.rules_alipay = [Parsers.generator_rule(*pattern) for pattern in Rules.alipay_rules]

    def contains_keywords(self, text, keyword_pattern):
        """
        正则匹配
        :param text: 充值|会员
        :param keyword_pattern: 商户消费充值支出招商银行(1234)支付成功
        :return:
        """
        # 构建正则表达式
        regex = re.compile(keyword_pattern, flags=re.IGNORECASE)
        return bool(regex.search(text))

    def process_row(self, provider, row, outer_file_path):
        """
        记账
        :param provider:
        :param row:
        :param outer_file_path:
        :return:
        """

        matched = False  # 默认情况下，认为未匹配到规则

        # 解析规则
        match_rules = None
        if provider == ProviderEnum.WECHAT:
            match_rules = self.rules_wechat
        elif provider == ProviderEnum.ALIPAY:
            match_rules = self.rules_alipay

        for rule in match_rules:
            if all(self.contains_keywords(row[key], value) for key, value in rule['route'].items()):
                # 交易时间
                row[0] = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                # 金额
                amount = 0.00
                # 商品说明
                detail = ''

                # 微信账单
                if provider == ProviderEnum.WECHAT:
                    # amount = '{:.2f}'.format(float(row[5].replace('¥', '')))
                    amount = '{:.2f}'.format(float(row[5].replace('¥', '').replace(',', '')))
                    detail = row[1] if row[3] == '/' else row[3]
                # 支付宝账单
                if provider == ProviderEnum.ALIPAY:
                    amount = '{:.2f}'.format(float(row[6].replace('¥', '')))
                    detail = row[4]

                # 构建内容字符串
                content = (f"{row[0]} * \"{row[2]}\" \"{detail}\"\n"
                           f"{' ' * 4}{rule['account']['debit']} {amount} CNY\n"
                           f"{' ' * 4}{rule['account']['credit']} -{amount} CNY\n")

                # 将内容写入到文件
                with open(outer_file_path, 'a', encoding='utf-8') as file:
                    file.write(content)
                # mark matched
                matched = True
                # 如果匹配到一条规则，就退出循环，不再检查其他规则
                break
        return matched

    def parse_bill(self, provider, start_row, file_path):
        """
        解析账单
        :param provider: 供应商
        :param start_row: 开始行数
        :param file_path: 文件路径
        :return:
        """
        outer_file_path = PathUtils().get_project_path() + 'data/processed/' + f'{provider}_transaction.bean'
        # 判断文件是否存在
        if os.path.exists(outer_file_path):
            # 如果文件存在，删除文件
            os.remove(outer_file_path)

        csv_handler = CSVUtils(file_path)

        # Reading CSV from the N row, each field separated by commas
        data = csv_handler.read_csv(start_row)
        unmatched_data = []
        for row in data:
            matched = self.process_row(provider, row, outer_file_path)
            if not matched:
                unmatched_data.append(row)
        unmatched_data_num = len(unmatched_data)

        # 未匹配到规则的订单
        with open(outer_file_path, 'a', encoding='utf-8') as file:
            if unmatched_data_num > 0:
                file.write(f'\n未匹配到规则的订单共{unmatched_data_num}条：\n')
                self.logger.info(f'\n{provider}未匹配到规则的订单共{unmatched_data_num}条：\n{unmatched_data}')
                for row in unmatched_data:
                    file.write(f'{row}\n')
