employees = [
    {"id": 101, "name": "Rahim", "salary": 30000},
    {"id": 102, "name": "Karim", "salary": 35000},
    {"id": 103, "name": "Nila", "salary": 40000}
]

total_salary = 0

for employee in employees:
    print(employee["name"], employee["salary"])
    total_salary += employee["salary"]

print("Total salary:", total_salary)
