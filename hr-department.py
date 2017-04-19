from department import Department

class HumanResources(Department):
    '''subclass of department
        
        properties:
        inherits from Department
        and augments with:
        is_hiring: (boolean)
    '''
    def __init__(self, name, supervisor, budget, meeting_place, is_hiring):
        Department.__init__(self, supervisor, budget, meeting_place, is_hiring)
        self.__is_hiring = is_hiring

    @property
    def is_hiring(self):
        return self.__is_hiring

    @is_hiring.setter
    def is_hiring_setter(self, val):
        self.__is_hiring = val

    def meeting_place(self, place):
        """ This overrides the base meeting_place() class completely """  
        self.meeting_place = place

    #returns a formatted string representation of the instances properties
    def __str__(self):
        return 'department name: {}\ndepartment supervisor: {}\ndepartment budget: {}\nmeets at: {}\ncurrently hiring: {}'.format(self.name, self.supervisor, self.budget, self.meeting_place, self.is_hiring)


this_hr_department = HumanResources('HumanResources', 'meg', 2000, 'library', True)
print(this_hr_department)

