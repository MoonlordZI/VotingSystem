import pandas as pd
from ast import Global
import time

def CheckName():
    global df #so i can use outside this function
    df = pd.read_csv('Sample Electoral Roll 2022.csv') #opens voting csv file

    global FirstName #so i can use outside this function
    FirstName = input("What is your First Name? ")
    if FirstName not in df.values: #checking if inputted Firstname exsist in csv file
        print("Invalid First Name")
        exit()

    Surname = input("What is your Surname? ")
    if Surname not in df.values: #checking if inputted Surname exsist in csv file
        time.sleep(1)
        print("Invalid Surname")
        exit()

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

    Cm = df.loc[df['First Name'].isin([FirstName])]['House Number'].iat[0]
    print(Cm)
    if Cm == int(input("")):
        print("YAS")
    else:
        print("NO")
CheckAddress()
