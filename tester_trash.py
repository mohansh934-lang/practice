import time
import random


bimari = ["fever", "cough", "cold", "headache", "nausea", "cancer"]

# Scan the patient's 
while True:
    try:
      print("Welcome to the shri girdhari hospital")
      time.sleep(2)
      print("thanks for waiting, please provide patient details")
      x = input("Enter patient name :")
      if x == "":
          raise NameError("Name cannot be empty")
      elif x == "exit":
        break
      else:
        print("Scanning patient", x)
        time.sleep(5)
        i = random.choice(bimari)
        print("Patient", x, "has", i)
        if i == "fever":
                print("Prescribing paracetamol for", i)
        elif i == "cough":
                print("Prescribing cough syrup for", i)
        elif i == "cold":
                print("Prescribing decongestant for", i)
        elif i == "headache":
                print("Prescribing ibuprofen for", i)
        elif i == "nausea":
                print("Prescribing anti-nausea medication for", i)      
        else:
                print("Bhajan karo or dua karo bhagwan se", i)
        print("Get well soon", x)
        print("-------------------------------")
        break
    except NameError as ne:
        print(ne)
        
               