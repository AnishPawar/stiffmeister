import datetime
class Employee:
    raise_amount = 1.1
    num_empls = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_empls += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    @classmethod
    def set_raise_amount(cls,amount):
        Employee.raise_amount = amount
    @classmethod                      #alternative constructor
    def from_string(cls,emp_str):
        first,last,pay  = emp_str.split(' ')
        return cls(first,last,pay)
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True    
class Developer(Employee):
    def __init__(self,first,last,pay,language):
        # super().__init__(first,last,pay)
        Employee.__init__(self,first,last,pay)
        self.language = language    

emp_1 = Developer('Anish','Pawar',1000,'Python')
emp_2 = Developer('Kiran','Pawar',1000,'CPP')


date = datetime.date(2020,7,11)
print(Developer.is_weekday(date))
# print(help(Developer))
print(emp_1.language)
