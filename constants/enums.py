# author: 测试蔡坨坨
# datetime: 2024/3/20 1:01
# function: 枚举类

from enum import Enum


class AccountEnum(Enum):
    ASSETS_CURRENT_BANK_CMB_Debit1234 = 'Assets:Current:Bank:CMB:Debit1234'
    ASSETS_CURRENT_WECHAT_MINIFUND = 'Assets:Current:Wechat:MiniFund'
    ASSETS_CURRENT_WECHAT_WALLET = 'Assets:Current:Wechat:Wallet'

    EXPENSES_FOOD = 'Expenses:Food'
    EXPENSES_TRANSPORT = 'Expenses:Transport'
    EXPENSES_CLOTHING = 'Expenses:Clothing'
    EXPENSES_OTHER = 'Expenses:Other'
    EXPENSES_COMMUNICATION = 'Expenses:Communication'
    EXPENSES_DAILY = 'Expenses:Daily'
    EXPENSES_HOUSING = 'Expenses:Housing'

    LIABILITIES_HUABEI = 'Liabilities:Huabei'

    INCOME_OTHER = 'Income:Other'
    INCOME_SIDELINE = 'Income:Sideline'

    def __str__(self):
        return self.value


class ProviderEnum(Enum):
    WECHAT = 'wechat'
    ALIPAY = 'alipay'

    def __str__(self):
        return self.value


class WechatColumnEnum(Enum):
    TRADE_TYPE = 1  # 交易类型
    TRADE_OBJECT = 2  # 交易对方
    PRODUCT = 3  # 商品
    INCOME_EXPENSE = 4  # 收/支
    PAY_METHOD = 6  # 交易方式
    PAY_STATUS = 7  # 交易状态


class AlipayColumnEnum(Enum):
    TRADE_TYPE = 1
    TRADE_OBJECT = 2
    PRODUCT = 4
    INCOME_EXPENSE = 5
    PAY_METHOD = 7
    PAY_STATUS = 8
