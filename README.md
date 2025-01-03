# beancount-importer-open

> 功能：自动将`微信`、`支付宝`账单转换成 beancount 账单。



### 使用指南

详细说明：[自动记账：Python+Beancount](https://mp.weixin.qq.com/s/G_oJR__hKfEmB4tMQ8Po-w?token=227064824&lang=zh_CN)

1. **下载账单并解压**

   下载 **微信** 和 **支付宝** 的账单文件，并将其解压到 data/bank_statements 目录中（每次仅支持处理一份微信账单和一份支付宝账单文件）。

2. **配置账户映射**

   打开 constants/enums.py 文件，设置 AccountEnum 枚举，以确保账单中的账户与 **beancount** 配置中的账户相对应。

3. **自定义账单解析规则**

   在 src/accounting/rules.py 文件中，根据需要调整账单解析规则。

4. **生成 beancount 格式账单**

   运行 main.py，生成的 beancount 格式账单文件将保存到 data/processed 目录中。



通过以上步骤，即可快速将微信和支付宝账单转换为 beancount 记账格式！
