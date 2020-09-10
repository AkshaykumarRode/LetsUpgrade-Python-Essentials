class bankacc:
	def __init__(self,):
		self.balance=0
		print("Welcome to your bank account")

	def deposit(self):
		amount=float(input("Enter amount to be Deposite: "))
		self.balance += amount
		print("Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("You Withdrew:", amount)
		else:
			print("Insufficient balance ")

	def display(self):
		print("Net Available Balance is =",self.balance)

Account = bankacc()
Account.deposit()
Account.withdraw()
Account.display()
