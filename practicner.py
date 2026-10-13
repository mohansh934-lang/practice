#question 1st
# basic aggregate functions on a list of numbers
# numbers = [12, 45, 7, 23, 89, 34, 2, 56]

# b = {'Sum':sum(numbers), 'Max': max(numbers), 'Min': min(numbers), 'Count': len(numbers), 'Average':  sum(numbers) / len(numbers), 'Even': [num for num in numbers if num % 2 == 0], 'Odd': [num for num in numbers if num % 2 != 0]}
# print(numbers)
# print(b)

# count = 0
# maximum = numbers[0]
# minimum = numbers[0]

# for num in numbers:
#     count += 1
#     if num > maximum: 
#         maximum = num
#     if num < minimum:
#         minimum = num

# print(f"Count: {count}")
# print(f"Maximum: {maximum}")
# print(f"Minimum: {minimum}")

# --------------------------------------------------------------------------------------------------------------------------------------------------

#question 2nd
#remove None and 0 values from a list
# data = [10, None, 25, 0, None, 40, 15, None, 50]  

# cleaned_data = []    #cleaned_data = [x for x in data if x is not None and x != 0]  # Using list comprehension to filter out None and 0 values

# for x in data:
#     if x is not None and x !=0:
#         cleaned_data.append(x)

# print(cleaned_data)  # Output: [10, 25, 40, 15, 50]
# ---------------------------------------------------------------------------------------------------------------------------------------------------

#question 3rd
   # Program banao jo:
# extra spaces remove kare
# poora text lowercase kare
# words ki list banaye
# total words count kare
# "python" word present hai ya nahi check kare

# text = "  Data Engineering is FUN and Python is powerful  "

# lower_text = text.lower()  # Convert to lowercase
# cleaned_text = ' '.join(text.split())  # Remove extra spaces
# words = cleaned_text.split()  # Create a list of words
# total_words = len(words)  # Count the total number of words
# python_present = "python" in words  # Check if "python" is present

# print(f"Cleaned Text: '{words}'")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# question 4th
  #Har word kitni baar aaya uska dictionary banao.

# text = "python is easy and python is powerful and python is useful"

# word_count = {}
# for word in text.split():
#     word_count[word] = word_count.get(word, 0) + 1   #dictionary["key"] = dictionary.get("key", default_value) + 1
# print(word_count)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

#question 5th
    # Tasks:
# name print karo
# salary print karo
# skills mein "AWS" add karo
# salary ko 95000 update karo
# "city": "Bhopal" add karo
# check karo "Python" skills mein hai ya nahi


# employee = {
#     "name": "Rahul",
#     "department": "Data Engineering",
#     "salary": 85000,
#     "experience": 2,
#     "skills": ["Python", "SQL", "PySpark"]
# }

# emp_name = (f"name:{employee['name']}")
# print(emp_name)
# emp_salary = (f"salary:{employee['salary']}")
# print(emp_salary)
# skill_AWS = employee["skills"].append("AWS")   #append object ko modify karta hai return nahi karta hai 
# print(f"skill_+AWS : {employee['skills']}")
# update_salary = employee.update({"salary": 95000})
# print(f"salary_update: {employee['salary']}")   #update bhi object ko modify karta hai na ki return
# add_city= employee["city"] = "Bhopal"
# print(f"city_add:{employee['city']}")
# check_python = "python" in employee['skills']
# print(check_python)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#question 6th
    # Program banao jo:
# highest salary wala employee find kare
# average salary calculate kare
# salary > 75000 wale employees print kare.

# employees = {
#     101: {"name": "Rahul", "salary": 70000},
#     102: {"name": "Priya", "salary": 85000},
#     103: {"name": "Amit", "salary": 65000},
#     104: {"name": "Neha", "salary": 95000}
# }

# total_salary = 0
# highest_salary = 0

# for emp in employees.values():
#     salary = emp['salary']
#     total_salary += salary

#     if salary > highest_salary:
#         highest_salary = salary
        
#     if salary > 75000:
#         print(emp['name'],salary)

# average_salary = total_salary / len(emp)

# print(f"highest salary: {highest_salary}")
# print(f"average salary:{average_salary}")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#question 7
   # Tasks:
# total transaction amount
# highest transaction
# lowest transaction
# amount > 1000 wali transactions
# sirf transaction IDs ki list

# Ye DE-style data transformation hai.

# transactions = [
#     {"id": 1, "amount": 500},
#     {"id": 2, "amount": 1200},
#     {"id": 3, "amount": 300},
#     {"id": 4, "amount": 2000},
#     {"id": 5, "amount": 750}
# ]

# total_amount = 0
# highest_transaction = 0
# lowest_transaction= transactions[0]['amount']

# for tran in transactions:
#     total_amount += tran['amount']
#     if tran['amount'] > highest_transaction:
#         highest_transaction = tran["amount"]
#     if tran["amount"] < lowest_transaction :
#         lowest_transaction = tran['amount']
        
    
# print(total_amount)     
# print(highest_transaction)
# print(lowest_transaction)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 8

# i = 0

# for i in range(0,101):
#     if i % 3==0 and i%5==0:
#         print("fizzbuz")
#     elif i % 3==0:
#         print("fizz")
#     elif i % 5==0:
#         print("buzz")
#     else:
#         print(i)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 9
#use enumerate()

# skills = ["Python", "SQL", "PySpark", "AWS", "Airflow"]

# for i in range(len(skills)):
#     print(i + 1, skills[i])     #normaly loop se 


# for i, skills in enumerate(skills, start=1):
    # print(i,skills)   # by using enumerate 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# question 10

# names = ["Rahul", "Priya", "Amit", "Neha"]
# scores = [85, 92, 76, 89]

# result = {}
# for name, score in zip(names, scores):
#     result[name]= score

# print(result)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 11
#remove duplicate

# data = [10, 20, 10, 30, 40, 20, 50, 30, 60]

# unique_data = []

# for num in data:
#     if num not in unique_data:
#         unique_data.append(num)

# print(unique_data)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 12

# users = [
#     {"name": "Rahul", "age": 22, "city": "Bhopal"},
#     {"name": "Priya", "age": 25, "city": "Indore"},
#     {"name": "Amit", "age": 19, "city": "Bhopal"},
#     {"name": "Neha", "age": 28, "city": "Delhi"}
# ]


# condition_list = []

# for data in users:
#     if data['age'] >=22 and data['city'] != 'Bhopal':
#         condition_list.append(data)


# print(condition_list)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 13
#even ki list banani hai 

# numbers = [1,2,3,4,5,6,7,8,9,10]

# even_list = []

# for num in numbers:
#     if num % 2 ==0:
#         even_list.append(num)

# print(even_list)


# even_number = [num for num in numbers if num %2==0]
# print(even_number)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 14

# numbers = [1, 2, 3, 4, 5]

# dic_view = {}

# for i in numbers:
#     dic_view[i] = i*i

# print(dic_view)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#question 15

# records = [
#     {"name": "Rahul", "age": "22", "salary": "50000"},
#     {"name": "Priya", "age": "25", "salary": "65000"},
#     {"name": "Amit", "age": "19", "salary": "45000"},
#     {"name": "Neha", "age": "28", "salary": "80000"}
# ]


# cleaned_data = []

# for record in records:
#     record["age"] = int(record["age"])
#     record["salary"] = int(record["salary"])

#     if record["salary"] >= 50000:
#         cleaned_data.append(record)

# print(cleaned_data)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



















