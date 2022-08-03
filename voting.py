import time
import csv 


with open("Sample Electoral Roll 2022.csv") as file:
    reader = csv.DictReader(file)
    Sname = input("what is your Surname? ")
    for row in reader:
        if row['Surname'] != Sname:
            print("your ugly ass is missing baka")
            break
        if row['Surname'] == Sname:
            print("we found your ugly ass")
            break
print("Welcome to today's election votes")
time.sleep(1)
print("Please fill in your credentials for verification ")
time.sleep(1)
FirstName = input("what is your First name? ")
MiddleName = input("what is your Middle name? ")
LastName = input("what is your Last name? ")
