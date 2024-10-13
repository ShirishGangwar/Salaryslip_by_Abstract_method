

#                                        [ Employee salary slip ]


from abc import abstractmethod
class Emp:
    @abstractmethod
    def Daysalary(self,hr,r):
        pass
    @abstractmethod
    def Monthsalary(self,m):
        pass
    @abstractmethod
    def Absentsalary(self,x):
        pass
    @abstractmethod
    def Tax(self,t):
        pass
    @abstractmethod
    def Totalsalary(self):
        pass
class Engineer(Emp):
#         ↓      ↓
#     Drive     parent class
    def Daysalary(self,hr,r):
        global day                # Globel key words are use full to globelize any local variable
        day=hr*r
        print("DaySalary:",day)
    def Monthsalary(self,m):
        global month
        month=day*m
        print("MonthSalary:",month)
    def Absentsalary(self,x):
        global ab
        ab=day*x
        print("Absent:",ab)
    def Tax(self,t):
        global tax
        tax=month*t/100
        print("Tax:",tax)
    def totalsalary(self):
        total=month-ab-tax
        print("TotalSalary:",total)

k=Engineer()
k.Daysalary(8,200)
k.Monthsalary(31)
k.Absentsalary(5)
k.Tax(5)
k.totalsalary()


