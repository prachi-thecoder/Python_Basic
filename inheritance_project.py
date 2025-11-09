class employee:
    def __init__(self):
        self.emp_name="prachi"
        self.emp_id=emp123342
        self.emp_salary=100000
    def display_info(self):
        print(self.emp_name)
        print(self.emp_id)
        print(self.emp_salary)
    def calculate_bonus(self):
        bonus=1000 + self.emp_salary
    def promote(self):
        print(f"{self.emp_name}promoted new salary:{self.emp_salary}")
class manager(employee):
    def __init__(self):
        super.__init__(self.emp_name,self.emp_id,self.emp_salary)
        self.department="fullstack"
        self.project_handled=0
    def project_assign(self):
        self.project_handled +=1
    def display_managerinfo(self):
        print(self.department)
        print(self.project_handled)
class senior_manager(manager):
    def __init__(self):
        super.__init__(self.emp_name,self.emp_id,self.emp_salary)
        self.team_size=10
        self.initialbudget=10000
    # def approve_budget(self):
    def display_seniormanager_info(self):
        print(self.team_size)
        print(self.initialbudget)

obj = senior_manager()
obj.display_info()
obj.calculate_bonus()
obj.promote()
obj.display_managerinfo()
obj.display_seniormanager_info()
