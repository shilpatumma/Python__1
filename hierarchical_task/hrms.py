# (2). Human Resources Management System (HRMS)
# Employee Hierarchy:
# Base class Employee with attributes like employee_id, name, salary.
# Subclasses: Manager, Developer, Salesperson, HR, etc., with specific attributes 
# (e.g., department, role, commission) and methods (e.g., calculate_bonus, generate_payslip).
# Leave Management:
# Base class Leave with attributes like employee, start_date, end_date.
# Subclasses: SickLeave, CasualLeave, PaternityLeave, etc., with specific attributes 
# (e.g., medical_certificate, reason) and methods (e.g., approve_leave).

# Ans...


# class Employee:
#     def __init__(self, employee_id, name, salary):
#         self.employee_id = employee_id
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         return self.salary * 0.2

#     def generate_payslip(self):
#         return f"\nEmployee Name : {self.name} \nID : {self.employee_id} \nSalary : {self.salary} \nBonus : {self.calculate_bonus()}" 


# class Manager(Employee):
#     def __init__(self, employee_id, name, salary, department):
#         super().__init__(employee_id, name, salary)
#         self.department = department

#     def calculate_bonus(self):
#         return self.salary * 0.25

# class Developer(Employee):
#     def __init__(self, employee_id, name, salary, programming_language):
#         super().__init__(employee_id, name, salary)
#         self.programming_language = programming_language

#     def calculate_bonus(self):
#         return self.salary * 0.3


# class Salesperson(Employee):
#     def __init__(self, employee_id, name, salary, commision):
#         super().__init__(employee_id, name, salary)
#         self.commision = commision

#     def calculate_bonus(self):
#         return self.salary * 0.2 + self.commision

# class HR(Employee):
#     def __init__(self, employee_id, name, salary, role):
#         super().__init__(employee_id, name, salary)
#         self.role = role

#     def calculate_bonus(self):
#         return self.salary * 0.2 
    

# class Leave:
#     def __init__(self, employee, start_date, end_date):
#         self.employee = employee
#         self.start_date = start_date
#         self.end_date = end_date

#     def approval_leave(self):
#         return f"Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"


# class SickLeave(Leave):
#     def __init__(self, employee, start_date, end_date, medical_certificate):
#         super().__init__(employee, start_date, end_date)
#         self.medical_certificate = medical_certificate

#     def approval_leave(self):
#         if self.medical_certificate:
#             return f"\nSick Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"
#         else:
#             return f"\nSick leave denied for {self.employee.name} due to missing medical certificate."


# class CasualLeave(Leave):
#     def __init__(self, employee, start_date, end_date, reason):
#         super().__init__(employee, start_date, end_date)
#         self.reason = reason

#     def approval_leave(self):
#         return f"\nCasual Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"


# class PaternityLeave(Leave):
#     def __init__(self, employee, start_date, end_date, child_certificte):
#         super().__init__(employee, start_date, end_date) 
#         self.child_certificte = child_certificte

#     def approval_leave(self):
#         if self.child_certificte:
#             return f"\nPaternity Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"
#         else:
#             return f"\nPaternity leave denied for {self.employee.name} due to missing certificate."


# manager = Manager(1, "Manish Shukla", 90000, "IT")
# developer = Developer(2, "Shivani Mehra", 85000, "Python")
# salesperson = Salesperson(3, "Jyoti Mehta", 80000, 2000)
# hr = HR(4, "Sundar Verma", 75000, "Hiring Employees")


# print(manager.generate_payslip())
# print(developer.generate_payslip())
# print(salesperson.generate_payslip())
# print(hr.generate_payslip())


# sickleave = SickLeave(developer, "14-08-2024", "20-08-2024", medical_certificate = True)
# casualleave = CasualLeave(manager, "16-08-2024", "20-08-2024", reason = "Family events")
# paternityleave = PaternityLeave(salesperson, "17-08-2024", "26-08-2024", child_certificte=True)


# print(sickleave.approval_leave())
# print(casualleave.approval_leave())
# print(paternityleave.approval_leave())

