class Category:
    id = 0
    def __init__(self, budget_name):
        self.budget_name = budget_name
        self.ledger = list()
        self.funds = 0
        self.total_deposit = 0
        self.total_withdraw = 0
        self.column = list()
        Category.id += 1

    def __str__(self):
        budget_string = [self.budget_name.center(30, "*")]
        for line in self.ledger:
            line_desc = line["description"][:23].ljust(23)
            line_amount = str("{:.2f}".format(line["amount"])).rjust(7)
            budget_string.append(line_desc + line_amount)

        budget_string.append(str("Total: {:.2f}".format(self.funds)))
        return "\n".join(budget_string)

    def deposit(self, dep_amount, dep_desc=""):
        self.ledger.append({"amount": (dep_amount), "description": dep_desc})
        self.funds = self.funds + dep_amount
        self.total_deposit += + dep_amount
    
    def withdraw(self, withdraw_amount, withdraw_desc=""):
        if self.check_funds(withdraw_amount) is True:
            self.funds -= withdraw_amount
            self.total_withdraw += withdraw_amount
            self.ledger.append({"amount": withdraw_amount*(-1), "description": withdraw_desc})
            return True
        else:
            return False
    
    def get_balance(self):
        return self.funds

    def transfer(self, transfer_amount, destination):
        if self.check_funds(transfer_amount) is True:
            self.funds -= transfer_amount
            self.total_withdraw += transfer_amount
            destination.funds += transfer_amount
            destination.total_deposit = destination.total_deposit + transfer_amount
            self.ledger.append({"amount": transfer_amount*(-1), "description":  "Transfer to " + destination.budget_name} )
            destination.ledger.append({"amount": transfer_amount, "description": "Transfer from " + self.budget_name})
            return True
        else:
            return False
    def check_funds(self, amount):
        if self.funds < amount:
            return False
        else:
            return True
def get_withdraw_percentage(categories, final_withdraw):
    rounded = int(round((categories.total_withdraw*100/final_withdraw)/10)*10)
    return rounded

def create_spend_chart(categories):
    count , percent, max_len, final_withdraw =  0, 0, 0, 0
    categories_qty = Category.id
    spend_chart = "Percentage spent by category\n"
    for category in categories:
        if len(category.budget_name) >= max_len:
            max_len = (len(category.budget_name))
        else:
            continue

    for category in categories:
        final_withdraw += category.total_withdraw

    for i in range(10):
        percent = 100 - count
        percent_str = (str(percent)+"|").rjust(4)
        spend_chart += percent_str
        count += 10
        for category in categories:
            rounded = get_withdraw_percentage(category, final_withdraw)
            if percent <= rounded:
                spend_chart += "o".center(3)
            else:
                spend_chart += "".center(3)
        spend_chart += "\n"
    spend_chart += "    -"+"---"*categories_qty+"\n"
    names = []
    for category in categories:
        names.append(category.budget_name)

    index = 0
    while index < max_len:
        spend_chart += "".center(5)
        for name in names:
            if index >= len(name):
                spend_chart += "".center(2)
            else:
                spend_chart += str(name[index]) + "".center(2)
        spend_chart += "\n"
        index += 1

    return spend_chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
#food.get_balance()
print(create_spend_chart([clothing, food, auto]))

#print(food)
#print(clothing)