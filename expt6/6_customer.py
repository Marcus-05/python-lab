class customer:
    def __init__(self, bill_amount, name):
        self.bill_amount = bill_amount
        self.customername = name

    def purchase(self):
        self.discount_price = 5 * self.bill_amount / 100
        self.pay_bill = self.bill_amount - self.discount_price

    def pays_bill(self):
        self.purchase()
        print(f"The customer name is {self.customername}")
        print(f"The discount price is {self.discount_price}")
        print(f"The pay bill is {self.pay_bill}")


if __name__ == '__main__':
    musheer = customer(400, "musheer")
    musheer.pays_bill()
