class perent:
    companyName="Infosys" 
    
    def __init__(self,id,name,salary):
        self.id = id
        self.Name = name
        self.salary = salary

    @classmethod
    def changecompany(cls,name):
        cls.companyName=name

    def bonus(self):
        print("Bonus : ",self.salary*0.2)

    def display(self):
       print("ID : ",self.id)
       print("Name : ",self.Name)
       print("Salary : ",self.salary)
       print("Company Name : ",self.companyName)

class devloper(perent):
    def __init__(self,id,name,salary,lang):
        super().__init__(id,name,salary)
        self.languge=lang

    def display(self):
        super().display()
        print("Languge : ",self.languge)
 
class manager(perent):

    def __init__(self,id,name,salary,team_size):
        super().__init__(id,name,salary)
        self.team_size=team_size

    def display(self):
        super().display()
        print("Team Size : ",self.team_size)

emp1=devloper(101,"kalpesh",20000,"python")
emp1.display()
emp1.bonus()

print("---------------------------------------------------")

emp2=manager(102,"om",20000,5)
emp2.changecompany("TCS")
emp2.display()

print("---------------------------------------------------")

emp3=perent(103,"sachin",20000)
emp3.display()