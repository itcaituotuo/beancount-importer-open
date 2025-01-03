# author: 测试蔡坨坨
# datetime: 2024/1/14 15:51
# function: 账单解析规则

from constants.enums import (AccountEnum, ProviderEnum)


class Rules:
    # 对应微信账单字段&借贷账户：供应商, 交易类型, 交易对方, 商品, 收支, 支付方式, 当前状态, 借方, 贷方
    wechat_rules = [
        # 支出
        # 借：费用增加 贷：资产减少
        (ProviderEnum.WECHAT, '商户消费', '', '美团', '支出', '零钱通', '支付成功', AccountEnum.EXPENSES_FOOD, AccountEnum.ASSETS_CURRENT_WECHAT_MINIFUND),
        (ProviderEnum.WECHAT, '商户消费', '', '美团|叮咚买菜', '支出', '招商银行.*1234', '支付成功|已退款', AccountEnum.EXPENSES_FOOD, AccountEnum.ASSETS_CURRENT_BANK_CMB_Debit1234),
        
        # 收入
        # 借：资产增加 贷：收入增加
        (ProviderEnum.WECHAT, '红包|转账|二维码收款|其他', '', '', '收入', '', '已存入零钱|已到账|已收钱', AccountEnum.ASSETS_CURRENT_WECHAT_WALLET, AccountEnum.INCOME_OTHER),
        (ProviderEnum.WECHAT, '转账', '', '', '收入', '', '已转入零钱通', AccountEnum.ASSETS_CURRENT_WECHAT_MINIFUND, AccountEnum.INCOME_OTHER),
        
        # 内部转账
        # 借：资产增加 贷：资产减少
        (ProviderEnum.WECHAT, '转入零钱通-来自招商银行.*1234', '', '/', '/', '招商银行.*1234', '支付成功', AccountEnum.ASSETS_CURRENT_WECHAT_MINIFUND, AccountEnum.ASSETS_CURRENT_BANK_CMB_Debit1234),
        (ProviderEnum.WECHAT, '转入零钱通-来自零钱', '', '', '/', '零钱', '支付成功', AccountEnum.ASSETS_CURRENT_WECHAT_MINIFUND, AccountEnum.ASSETS_CURRENT_WECHAT_WALLET)
    ]

    # 对应支付宝账单字段&借贷账户：供应商, 交易分类, 交易对方, 商品说明, 收/支, 收/付款方式, 交易状态, 借方, 贷方
    alipay_rules = [
        # 支出
        # 借：费用增加 贷：资产减少
        (ProviderEnum.ALIPAY, '服饰装扮', '', '', '支出', '招商银行.*1234', '交易成功|等待确认收货', AccountEnum.EXPENSES_CLOTHING, AccountEnum.ASSETS_CURRENT_BANK_CMB_Debit1234),
        (ProviderEnum.ALIPAY, '餐饮美食', '', '', '支出', '招商银行.*1234', '交易成功|等待确认收货', AccountEnum.EXPENSES_FOOD, AccountEnum.ASSETS_CURRENT_BANK_CMB_Debit1234),
        (ProviderEnum.ALIPAY, '交通出行', '', '', '支出', '招商银行.*1234', '交易成功|等待确认收货', AccountEnum.EXPENSES_TRANSPORT, AccountEnum.ASSETS_CURRENT_BANK_CMB_Debit1234),

        # 支出
        # 借：费用增加 贷：负债增加
        (ProviderEnum.ALIPAY, '交通出行', '', '火车票', '支出', '花呗', '交易成功', AccountEnum.EXPENSES_TRANSPORT, AccountEnum.LIABILITIES_HUABEI),
        (ProviderEnum.ALIPAY, '家居家装', '', '', '支出', '花呗', '等待确认收货', AccountEnum.EXPENSES_DAILY, AccountEnum.LIABILITIES_HUABEI),

        # 借：负债减少 贷：资产减少
        (ProviderEnum.ALIPAY, '信用借还', '', '花呗', '不计收支', '招商银行.*1234', '还款成功', AccountEnum.LIABILITIES_HUABEI, AccountEnum.ASSETS_CURRENT_BANK_CMB_Debit1234),
    ]

