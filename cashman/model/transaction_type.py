#A file to define the type of transaction using python's enumerator.

from enum import Enum

class TransactionType(Enum):
	INCOME = "INCOME"
	EXPENSE = "EXPENSE"
	
	
#The code of the enumerator defines a class called TransactionType that inherits from Enum
#and defines two types, Income & Expense.
