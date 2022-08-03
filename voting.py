
import csv 


with open("Sample Electoral Roll 2022.csv") as file:
    reader = csv.DictReader(file)
    Sname = input("what is your Surname?")
    for row in reader:
        if row['Surname'] != Sname:
            print("your ugly ass is missing baka")
            break
        if row['Surname'] == Sname:
            print("we found your ugly ass")
            break