
class InvalidSalaryError(Exception):
    """Raised when an employee salary is negative."""
    pass


def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)
    if "cap" in options:
        result = min(result, options["cap"])
    return result


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )


employees = [
    {"id": 1, "name": "Arun", "department": "Sales",
     "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR",
     "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT",
     "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT",
     "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance",
     "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales",
     "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT",
     "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR",
     "salary": 48000, "city": "Mumbai"},
]

# Function
print("Bonus:", bonus(10000, 0.1, 500, 300, cap=1500))

# List comprehension
high_names = [
    emp["name"] for emp in employees if emp["salary"] > 50000
]
print("Above 50000:", high_names)

raised_salaries = list(
    map(lambda emp: emp["salary"] * 1.10, employees)
)
print("Raised salaries:", raised_salaries)

# filtering
chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)
print("Chennai:", [emp["name"] for emp in chennai_employees])

# inheritance
employee = Employee("Rahul", 60000)
manager = Manager("Divya", 75000, 5)

print(employee.get_details())
print("Annual salary:", employee.annual_salary())
print(manager.get_details())

# exception and finally
try:
    invalid_employee = Employee("Test", -500)
except InvalidSalaryError as error:
    print(f"Error: {error}")
finally:
    print("Transaction finished")

for emp in employees:
    salary = emp["salary"]

    if salary == 0:
        continue

    print("Checking:", emp["name"], salary)

    if salary > 85000:
        print("Stopping at:", emp["name"])
        break
