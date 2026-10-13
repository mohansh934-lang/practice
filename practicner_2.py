#question 1 

# numbers = [1,2,3,4,5,6,7,8,9]

# def data_summery(numbers):
#     result = {
#         "total": sum(numbers),
#         "minimum": min(numbers),
#         "maximum": max(numbers),
#         "average": sum(numbers)/len(numbers),
#         "count": len(numbers)
#     }
#     return result

# data = data_summery(numbers)

# print(data)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 2
# data = [10, None, 25, 0, 40, None, 15, 0, 50]

# def clean_data(data):
#     cleaned = []
#     for i in data:
#         if i is not None and i > 0:
#             cleaned.append(i)

#     return cleaned

# z= clean_data(data)
# print(z)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 3

# def data_ar(*args):      #*numbers, *args nam ki jagah kuch bhi aa sakte hai 
#     result = [
#         (args),
#         (sum(args)),
#         (sum(args)/len(args)),
#         (max(args)),
#         (min(args)) ]
#     return result

# f = data_ar(10,20,30)

# print(f)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 4

# def employee(**kwargs):
#     return kwargs


# result = employee(
#     name="Mohan",
#     department="Data Engineering",
#     salary=50000,
#     city="Bhopal",
#     experience=1
# )

# print(result)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 5
# def cleaner(data):
#     space_data = data.strip()
#     lower_data = space_data.lower()
#     comma_split = lower_data.split(',')

#     return comma_split


# f = cleaner("   MOHAN,DATA ENGINEER,INDIA   ")

# print(f)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 6


# def file_creat():
#     with open("employees_pytest.txt", "w") as file:
#         file.write("rahul\n")
#         file.write("neha\n")
#         file.write("ajay\n")
#         file.write("arun\n")

# file_creat()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 7

# def file_read():
#     names = []
#     with open("employees_pytest.txt", "r") as file:

#         for line in file:
#             name = line.strip()

#             if name:
#                 names.append(name)

#     print("Names", names)
#     print("Total_emps", len(names))

# file_read()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 8

# def file_creat():
#     with open("emp_data.txt","w") as file:
#         file.write("rahul,5000\n")
#         file.write("priya,65000\n")
#         file.write("amit,45000\n")
#         file.write("neha,80000\n")

# file_creat()

# def transform():
#         with open("emp_data.txt","r") as file:
#              with open("transformed_data.txt", "w") as output:

#                   for line in file:
#                        name, salary = line.strip().split(',')
#                        salary = int(salary)

#                        if salary >=50000:
#                             output.write(f"{name}, {salary}\n")

# transform()
