# PROXIMO PASSO METODO _repr_ PARA DEFINIR PRINT
# IMPRIMIR DESCRIÇÃO
class Category:

    def __init__(self, cat_name):
        self.name = cat_name
        self.ledger = list()

    def __repr__(self) -> str:
        asterisks = 30 - len(self.name)
        l_asterisks = asterisks // 2
        r_asterisks = asterisks - l_asterisks
        output = '{}{}{}'.format(l_asterisks*'*', self.name, r_asterisks*'*')
        for i in range(0, len(self.ledger)):


    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for i in range(0, len(self.ledger)):
            balance = balance + self.ledger[i]['amount']
        return balance

    def check_funds(self, check_amount):
        if check_amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def transfer(self, amount, budget_cat):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, 'Transfer to ' + budget_cat.name)
            budget_cat.deposit(amount, 'Transfer from ' + self.name)
            return True


food = Category('food')
food.deposit(1000, 'day 1 deposit')
food.deposit(1000, 'day 2 deposit')
food.withdraw(500, 'day 1 spending')
water = Category('water')
water.deposit(1000, 'month 1 deposit')
print(food)
