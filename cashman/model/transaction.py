#Inside this model, we will create three class, Transaction, Income & Expense.

import datetime as dt

#Marshmallow to help in object serialization & deserialization.
from marshmallow import Schema, fields


#Creating a super class called Transaction from which sub classes of Income & Expense will inherit properties from
class Transaction():
	def __init__(self, description, amount, type):
		self.description = description
		self.amount = amount
		self.created_at = dt.datetime.now()
		self.type = type
		
	def __repr__(self):
		return '<Transaction(name={self.description!r})>'.format(self=self)
		
		
class TransactionSchema(Schema):
	description = fields.Str()
	amount = fields.Number()
	created_at = fields.Date()
	type = fields.Str()
	
