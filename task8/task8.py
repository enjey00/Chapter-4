class MoneyFmt():
    def __init__(self, data):
        self.data = data

    def repr(self):
        print(self.data)

    def update(self, new_data):
        self.data = new_data

    def str_(self):
        dollarize = '${:,.2f}'.format(self.data)
        print(dollarize)

float_ = MoneyFmt(123654.216)
float_.repr()
float_.str_()
float_.update(31546549.12)
float_.repr()
float_.str_()