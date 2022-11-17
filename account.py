
class Account:
	
	def __init__(self, name) -> None:
		"""
		Inits account that set the default values

		:param name: person's name
		"""
		self.__name = name
		self.__balance = 0

	def get_balance(self) -> float:
		"""
		Function to get account balance

		:return: account balance
		"""
		return self.__balance

	def deposit(self, amount) -> bool:
		"""
		Function to increment the account balance
				
		:param amount: amount should be added to account
		
		:return: return True if deposit transaction is successful and False if deposit transaction is unsuccessful
		"""
		if amount < 0 or amount == 0:
			return False
		else:
			self.__balance += amount
			return True

	def withdraw(self, amount) -> bool:
		"""
		Function to decrement the account balance
		
		:param amount: amount should be subtracted to account
		
		:return: return True if withdraw transaction is successful and False if withdraw transaction is unsuccessfult
		"""
		if amount < 0 or amount == 0:
			return False
		elif amount > self.__balance:
			return False
		else:
			self.__balance -= amount
			return True

	def get_name(self) -> str:
		"""
		Function to get account name
		
		:return: account name
		"""
		return self.__name




