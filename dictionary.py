#student info store
'''
student = {}
student['roll_no'] = int(input("Enter roll number: "))
student['name'] = input("Enter name: ")
student['course'] = input("Enter course: ")
student['marks'] = float(input("Enter marks: "))2
print("\nStudent Information:")
print("Roll No:", student['roll_no'])
print("Name:", student['name'])
print("Course:", student['course'])
print("Marks:", student['marks'])
'''

# employee info store
'''
employee = {}

employee['emp_id'] = int(input("Enter employee ID: "))
employee['name'] = input("Enter employee name: ")
employee['department'] = input("Enter department: ")
employee['salary'] = float(input("Enter salary: "))

print("\nEmployee Information:")
print("Employee ID:", employee['emp_id'])
print("Name:", employee['name'])
print("Department:", employee['department'])
print("Salary:", employee['salary'])'''
# count character in a string in dictionary
'''
s = input("Enter a string: ")

d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print("Character count:")
print(d)

'''
