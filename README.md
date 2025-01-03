## 微信&支付宝账单 -> beancount账单

### 使用说明
1. 下载微信&支付宝账单，并解压到data/bank_statements目录下（微信&支付宝每次只能放一份文件）
2. 配置账户枚举（对应beancount里的账户），constants/enums.py文件AccountEnum
3. 配置账单解析规则，src/accounting/rules.py
4. 运行main.py，生成beancount账单，data/processed目录下
