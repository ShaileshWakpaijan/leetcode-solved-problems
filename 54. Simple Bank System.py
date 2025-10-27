# LeetCode 2043

class Bank:
    def __init__(self, balance):
        print(balance)
        self.balanceList = balance
        self.accounts = len(balance)
    
    def valid(self, acc):
        return 1 <= acc <= self.accounts

    def transfer(self, account1, account2, money):
        if not self.valid(account1) or not self.valid(account2):
            return False
        if self.balanceList[account1 - 1] < money:
            return False

        self.balanceList[account1 - 1] -= money
        self.balanceList[account2 - 1] += money
        return True

    def deposit(self, account, money):
        if not self.valid(account):
            return False
        self.balanceList[account - 1] += money
        return True

    def withdraw(self, account, money):
        if not self.valid(account):
            return False
        if self.balanceList[account - 1] < money:
            return False
        self.balanceList[account - 1] -= money
        return True
        