from department import Department

class ITdepartment(Department):
    '''subclass of department
        
        properties:
        inherits from Department
        and augments with:
        is_hiring: (boolean)
    '''
    def __init__(self, name, supervisor, budget, meeting_place, is_awesome):
        Department.__init__(self, supervisor, budget, meeting_place, is_awesome)
        self.__is_awesome = is_awesome

    @property
    def is_awesome(self):
        return self.__is_awesome

    @is_awesome.setter
    def is_awesome_setter(self, val):
        self.__is_awesome = val

    def meeting_place(self, place):
        """ This overrides the base meeting_place() class completely """  
        self.meeting_place = place

    def get_budget(self):
      """Returns the budget for respective Department instance"""
      
      self.budget = Department.budget + 15000
      return self.budget 

    #returns a formatted string representation of the instances properties
    def __str__(self):
        return 'department name: {}\ndepartment supervisor: {}\ndepartment budget: {}\nmeets at: {}\nis awesome: {}'.format(self.name, self.supervisor, self.budget, self.meeting_place, self.is_awesome)


this_it_department = ITdepartment('IT Department', 'Dean', 20000, 'server room', True)
print(this_it_department)

