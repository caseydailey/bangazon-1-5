import employee
import department


class ITdepartmentEmployee(Employee, FullTime):
	'''describes IT employees'''

	
	def __init__(self, first_name, last_name):
		Employee.__init__(first_name, last_name)
		FullTime.__init__(self)


class HRdepartmentEmployee(Employee, PartTime):
	'''describes HR employees'''

	def __init__(self, first_name, last_name):
		Employee.__init__(first_name, last_name):
		PartTime.__init__(self)