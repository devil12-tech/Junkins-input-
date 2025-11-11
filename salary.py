import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = sys.argv[1]
else:
     script_name = sys.argv[0]
     salary = 30000
     print("Input salary not provided. Using default salary")
bonus = 0.1*float(salary)
total_salary =float(salary)+bonus
print("Script Name:",script_name)
print("Salary:",salary)
print("Bonus:",bonus)
print("Total Salary:",total_salary)