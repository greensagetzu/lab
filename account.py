
class Account:
	
	def __init__(self, name) -> None:
		"""[Inits account ]

		Args:
			name ([string]): [person's name]
		"""
		self.__name = name
		self.__balance = 0

	def get_balance(self) -> int:
		"""[Function to get account balance]

		Returns:
			[int]: [account balance]
		"""
		return self.__balance

	def deposit(self, amount) -> boolean:
		"""[Function to increment the account balance]
				
		Args:
			amount ([int]): [amount should be added to account]
		
		Returns:
			bool: [if deposit transaction is successful or not]
		"""
		if amount < 0 or amount == 0:
			return False
		else:
			self.__balance += amount
			return True

	def withdraw(self, amount) -> boolean:
		"""[Function to decrement the account balance]
		
		Args:
			amount ([int]): [amount should be subtracted to account]
		
		Returns:
			bool: [if withdraw transaction is successful or not]
		"""
		if amount < 0 or amount == 0:
			return False
		elif amount > self.__balance:
			return False
		else:
			self.__balance -= amount
			return True

	def get_name(self) -> string:
		"""[Function to get account name]
		
		Returns:
			[string]: [account name]
		"""
		return self.__name

	def __str__(self) -> string:
		"""[Function to print]
		
		Returns:
			[string]: [print]
		"""
		return f'account_name = {self.__name} and account_balance = {self.__balance}'


def main() -> none:
	account_one = Account('001-John')
	
	account_one.deposit(100)
	account_one.deposit(200)
	account_one.withdraw(400)
	account_one.withdraw(50)

	print(account_one)

	name = input('Enter the name: ')
	account_two = Account(name)

	deposit_num = int(input('Enter amount to be desposited: '))
	account_two.deposit(deposit_num)
	print(account_two)

	withdraw_num = int(input('Enter amount to be withdrawn: '))
	account_two.withdraw(withdraw_num)
	print(account_two)


if __name__ == '__main__':
	main()