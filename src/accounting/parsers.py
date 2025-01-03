# author: 测试蔡坨坨
# datetime: 2024/2/20 1:14
# function: 账单解析

from constants.enums import AlipayColumnEnum, ProviderEnum, WechatColumnEnum


class Parsers(object):
    @staticmethod
    def generator_rule(provider, trade_type, trade_object, product, income_expense,
                       pay_method, pay_status, debit_account, credit_account):
        column = WechatColumnEnum if provider == ProviderEnum.WECHAT else AlipayColumnEnum
        rule = {
            'route': {
                column.value: value
                for column, value in
                zip(column, [trade_type, trade_object, product, income_expense, pay_method, pay_status])
            },
            'account': {
                'debit': debit_account,
                'credit': credit_account
            }
        }
        return rule
