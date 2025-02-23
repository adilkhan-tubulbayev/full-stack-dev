class Employee():
	def __init__(self, name, salary, department):
		self.name = name
		self.__salary = salary
		self.department = department

	@property
	def salary(self):
			return self.__salary
	
	@salary.setter
	def salary(self, value):
		if value < 0:
			print("Error. Salary must be greater than 0.")
		else:
			self.__salary = value


person = Employee("Abibos", 10000, "Abibos Department")
print(person.salary)
person.salary = 20000
print(person.salary)
