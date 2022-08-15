from ast import Global
import time
import csv
import pandas as pd

print("Welcome to today's election votes")
time.sleep(1) #delay of 1 second
print("Please fill in your credentials for verification ")
time.sleep(1)

def CheckName():
    global df #so i can use outside this function
    df = pd.read_csv('Sample Electoral Roll 2022.csv') #opens voting csv file

    global FirstName #so i can use outside this function
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
        time.sleep(1)

    print("Verifying your data...")
    time.sleep(1)

    verify = df.loc[df['First Name'].isin([FirstName])]['Surname'].iat[0] #returns the corresponding surname of the inputted firstname 
    if verify == Surname: #checks if the returned surname is same as the inputted surname
        time.sleep(1)
        print("OK")
        time.sleep(1)
    else:
        time.sleep(1)
        print("FAIL")
        time.sleep(1)
        print(FirstName + " does not correspond to " + Surname)
        exit()
CheckName()

def CheckAddress():


    HouseNum = int(input("What is your house number? "))
    StreetName = input("What is your street Name? ")
    Suburb = input("What is your Suburb?")
    Postcode = int(input('What is your Postcode? '))

    C1 = df.loc[df['First Name'].isin([FirstName])]['House Number'].iat[0]
    C2 = df.loc[df['First Name'].isin([FirstName])]['Street Name'].iat[0]
    C3 = df.loc[df['First Name'].isin([FirstName])]['Suburb'].iat[0]
    C4 = df.loc[df['First Name'].isin([FirstName])]['Postcode'].iat[0]

    if HouseNum == C1 and StreetName == C2 and Suburb == C3 and Postcode == C4:
        time.sleep(1)
        print("Address Verified...")
    else:
        print("Invalid Address")
        exit()
CheckAddress()

def eligibility():
    time.sleep(1)
    print("Checking Voting Eligibility...")
    time.sleep(1)
    pos = df.loc[df['First Name'].isin([FirstName])]['Has Voted?'].iat[0]
    if pos == "No":
        print("You are Eligible")
    else:
        print("You have already voted")
eligibility()
