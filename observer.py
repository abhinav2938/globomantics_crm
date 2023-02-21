#!/usr/bin/env python

"""
Author: Abhinav Kumar
Simple implementation of observer design pattern
where business and consumer customer are observer
"""

class BusinessCustomer:
	def __init__(self,accnt_id,mney_owd):
		"""
		constructor to store account Id and money owed
		"""
		#changes from online
		self.accnt_id = accnt_id
		self.mney_owd = mney_owd

	
	def update(self):
		"""
		When the subject wants to update the subscriber like eom we use this method
		"""
		if self.money_owd > 0:
			print(f"{self.accnt_id}: call the company's finance dept")
		else:
			print(f"{self.accnt_id}: corporate balance paid")

class ConsumerCustomer:
	def __init__(self,accnt_id,money_owd):
		self.accnt_id = accnt_id
		self.money_owd = money_owd

	def update(self):
		if self.money_owd > 0:
			print(f"{self.accnt_id}:send a reminder email")
		else:
			print(f"{self.accnt_id}:Individual balance paid")
	
class AccountingSystem:
	"""
	This is the subject/publisher that maintains list of observer and notify them
	"""

	def __init__(self):
		self.customers = set()

	def register(self,customer):
		self.customers.add(customer)

	def remove(self,customer):
		self.customers.remove(customer)

	
	def notify(self):
		for customer in self.customers:
			customer.update()

def main():
	
	"""
	Execution starts here
	"""


	cust1 = BusinessCustomer("ACT100", 10)
	cust2 = BusinessCustomer("ACT2", -19)
	cust3 = ConsumerCustomer("ACT$", -8)

	#create account system or the subject

	account_sys = AccountingSystem()
	account_sys.register(cust1)
	account_sys.register(cust2)
	account_sys.register(cust3)

	#notify of some event

	account_sys.notify()

	#cust2 unregister
	account_sys.remove(cust2)

	account_sys.notify()

if __name__ == "__main__":
	main()

