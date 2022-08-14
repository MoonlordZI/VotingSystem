import time
import csv
import pandas as pd

print("Welcome to today's election votes")
time.sleep(1) #delay of 1 second
print("Please fill in your credentials for verification ")
time.sleep(1)

def CheckName():
    df = pd.read_csv('Sample Electoral Roll 2022.csv') #opens voting csv file

    FirstName = input("What is your First Name? ")
    if FirstName not in df.values: #checking if inputted Firstname exsist in csv file
        time.sleep(1)
        print("Invalid First Name")
        exit()

    Surname = input("What is your Surname? ")
    if Surname not in df.values: #checking if inputted Surname exsist in csv file
        time.sleep(1)
        print("Invalid Surname")
        exit()

    questionMid = input("Do you have a Middle Name? [Type Y/N] ") 
    if questionMid == 'Y': 
        MiddleName = input("What is your Middle Name? ") #checking if inputted Middle Name exsist in csv file
        if MiddleName not in df.values:
            time.sleep(1)
            print("Invalid Middle Name")
            exit()
    else:
        time.sleep(1)
        print('OK')

    print("Virifying your data...")
    time.sleep(1)

    virify = df.loc[df['First Name'].isin([FirstName])]['Surname'].iat[0] #returns the corresponding surname of the inputted firstname 
    if virify == Surname: #checks if the returned surname is same as the inputted surname
        time.sleep(1)
        print("OK")
    else:
        time.sleep(1)
        print("FAIL")
        time.sleep(1)
        print(FirstName + " does not correspond to " + Surname)
        exit()
CheckName()

