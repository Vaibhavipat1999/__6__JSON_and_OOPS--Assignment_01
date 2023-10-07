# 👉 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of 
# Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a 
# list of objects of Employee class. Finally print the list of the Employee objects

import json

f = open('F:\PYTHON WORK\__6__JSON_and_OOPS_Assignment\_1_ Assignment_01\_1_Question_01\_1_Sample_employees.json',)
data = json.load(f)

for i in data['Employees']:
	print(i)

f.close()

