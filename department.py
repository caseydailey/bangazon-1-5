class Department():
    '''Parent class for all Departments

        properties: 
        name: (string)
        supervisor: (string)
        employees: (set)
        budget: (integer)
        meeting_place: (string)

        methods:
        setters and getters for the above prperties
    '''

    def __init__(self, name, supervisor, budget, meeting_place):
        self.__name = name
        self.__supervisor = supervisor
        self.employees = set()
        self.__budget = budget
        self.meeting_place = meeting_place

    def meeting_place():
        """ Provides instructions regarding meetings for employees """
        print("Everyone meet in {}".format(self.meeting_place))  

    #name getter
    @property
    def name(self):
        '''returns name if there is one'''
        try: 
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, name):
        '''sets name if given value'''
        try:
            self.__name = name
        except ValueError:
            raise ValueError("Please provide a department name")

    #supervisor getter
    @property
    def supervisor(self):
        '''returns supervisor name if there is one'''
        try:
            return self.__supervisor
        except AttributeError:
            return ""

    #supervisor setter
    @supervisor.setter
    def supervisor_setter(self, supervisor_name):
        '''sets supervisor if one is given'''
        try:
            self.__supervisor = supervisor_name
        except ValueError:
            raise ValueError("Please provide a supervisor name")

    #budget getter
    @property
    def budget(self):
        '''returns budget if there is one'''
        try: 
            return self.__budget
        except AttributeError:
            return ""

    def add_employee(self, employee):
        '''adds an employee to the employee set'''
        self.employees.add(employee)

    def remove_employee(self, employee):
        '''removes an employee'''
        self.employees.remove(employee)

    def get_employees(self):
      """Returns the set of employees for the department instance"""  
      print("Department:", self.name)
      for employee in self.employees:
        print("   ", employee.first_name, employee.last_name)

    #returns a formatted string representation of the instances properties
    def __str__(self):
        return 'department name: {}\ndepartment supervisor: {}\ndepartment budget: {} bucks\nmeets at: {}\n'.format(self.name, self.supervisor, self.budget, self.meeting_place)

this_department = Department('whatever', 'casey', 20, 'hackery')
print(this_department)

