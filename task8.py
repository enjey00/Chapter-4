class MoneyFmt():
    def __init__(self, data):
        self.data = data

    def repr(self):
        print(self.data)

    def update(self, new_data):
        self.data = new_data

    def __str__(self):
        dollarize = '${:,.2f}'.format(self.data)
        return dollarize

float_ = MoneyFmt(123654.2160000)
float_.repr()
print(float_)
float_.update(31546549.12464)
float_.repr()
print(float_)