# import logging


# class Gali:

#     def __init__(self):
#         logging.basicConfig(level=logging.INFO)
#         print("teri bhen chod dunga")
#         logging.warning("are nahi mat do hali")
#         self.next()
#     def next(self):
#         print("nahi yar majak tha soory")

# if __name__=="__main__":
#     obj = Gali()

# if __name__=="__main__":
#     print(__name__)

   
# retries = 3

# for i in range(retries):
#     print(i)
#     if i < retries-1:
#         print("True")
#     else:
#         print(False)

# total_sent = 0
# total_failed = 0

# for i in range(1,101):
#     if i % 2 ==0:
#         total_sent+=1
#     else:
#         total_failed+=1

# print(total_failed)
# print(total_sent)

# address = "Mohan"

# try:
#     print(name)
# except Exception as e:
#     print(e)


a = int(input("enter your 1st number: "))
b = int(input("enter your 2nd numbers: "))


try:
    if a == 0 and b == 0:
        raise ValueError("Both numbers cannot be zero")

    result = a + b
    print("Result:", result)

except Exception as e:
    print("Error:", e)

