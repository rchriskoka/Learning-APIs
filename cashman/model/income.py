#A file to represent income

from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

#Inheriting from Transaction
class Income(Transaction):
	def __init__(self, description, amount):
		super(Income,self).__init__(description,amount,TransactionType.INCOME)
		
	def __repr__(self):
		return '<Income(name={self.description!r})>'.format(self=self)
		

#Inheriting from TransactionSchema
class IncomeSchema(TransactionSchema):
	@post_load
	def make_income(self,data, **kwargs):
		return Income(**data)
