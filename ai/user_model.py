from decimal import Decimal, ROUND_HALF_UP
class User:
    amount = Decimal('0')

    # 初始化
    def __init__(self, amount):
        self.amount = Decimal(str(amount))



    # 资金变动
    def change_amount(self, start_index, end_index):
        # print(start_index, end_index, amount)


        s = Decimal(str(start_index))
        e = Decimal(str(end_index))
        # p = Decimal(str(proportion))
        # print(s, e)



        result = e * self.amount / s




        # 保留两位小数（0.00），使用“四舍五入”
        r = result.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

        self.amount = r
        return r

