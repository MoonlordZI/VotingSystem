import time
import csv

print("Welcome to today's election votes")
time.sleep(1)
print("Please fill in your credentials for verification ")
time.sleep(1)

with open("Sample Electoral Roll 2022.csv") as file:
    reader = csv.DictReader(file)
    Fname = input("what is your First Name? ")
    Sname = input("What is your Surname? ")
    Mname = input("What is your Middle Name? ")

    for row in reader:
        if row['First Name'] != Fname:
            print("your cridentials isnt reistered or you've inputting your First Name incorrectly")
            break
