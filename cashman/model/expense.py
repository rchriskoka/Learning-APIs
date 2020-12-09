#Creating a class to represent expenses.
from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

#Class Expense to inherit from Transaction.
class Expense(Transaction):
	def __init__(self, description, amount):
		super(Expense,self).__init__(description, -abs(amount), TransactionType.EXPENSE)
		
	def __repr__(self):
		return '<Expense(name={self.description!r})>'.format(self=self)
		
class ExpenseSchema(TransactionSchema):
	@post_load
	def make_expense(self, data, **kwargs):
		return Expense(**data)

#Similar to Income Class, this class hardcodes the type of the transaction but now passes Expense to the super class.
#What makes it different is that it forces the amount passed to be negative. 
#Therefore, no matter if the user sends a positive or negative value, it will always be stored as negative to faciliate calculations.


