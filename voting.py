from random import randint
import string
import random
import pandas as pd
from ast import Global
import time

print("Today is election day")
time.sleep(1) #delay of 1 second
print("Glory to Arstotzka!")
time.sleep(1)
print("Papers please...")
time.sleep(1)

def CheckName():
    global df #so i can use outside this function
    df = pd.read_csv('Sample Electoral Roll 2022.csv') #opens voting csv file

    global FirstName #so i can use outside this function
    FirstName = input("What is your First Name? ")
    if FirstName not in df.values: #checking if inputted Firstname dosent exsist in csv file
        time.sleep(1)
        print("Invalid First Name")
        exit()

    Surname = input("What is your Surname? ")
    if Surname not in df.values: #checking if inputted Surname dosent exsist in csv file
        time.sleep(1)
        print("Invalid Surname")
        exit()

    questionMid = input("Do you have a Middle Name? [Type Y/N] ") 
    if questionMid == 'Y': 
        MiddleName = input("What is your Middle Name? ")
        if MiddleName not in df.values: #checking if inputted Middle Name dosent exsist in csv file
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

def eligibility():

    time.sleep(1)
    print("Checking Voting Eligibility...")
    time.sleep(1)
    pos = df.loc[df['First Name'].isin([FirstName])]['Has Voted?'].iat[0] #retrieves value of 'Has Voted' collumn corresponding to the First Name
    if pos == "No": #Checks if the 'Has Voted' collumn says No 
        print("You are Eligible")
    else:
        print("You have already voted")
        exit()
eligibility()

def CheckAddress():
#asks input of addresses 
    HouseNum = int(input("What is your house number? "))
    StreetName = input("What is your street Name? ")
    Suburb = input("What is your Suburb? ")
    Postcode = int(input('What is your Postcode? '))
#retreives the addresses corresponding to the first name and stores it in varable
    C1 = df.loc[df['First Name'].isin([FirstName])]['House Number'].iat[0]
    C2 = df.loc[df['First Name'].isin([FirstName])]['Street Name'].iat[0]
    C3 = df.loc[df['First Name'].isin([FirstName])]['Suburb'].iat[0]
    C4 = df.loc[df['First Name'].isin([FirstName])]['Postcode'].iat[0]
#checks if retrieved addresses matches with inputted addresses
    if HouseNum == C1 and StreetName == C2 and Suburb == C3 and Postcode == C4:
        time.sleep(1)
        print("Address Verified...")
    else:
        print("Invalid Address")
        exit()
CheckAddress()

def ID():
    LOne = random.choice(string.ascii_letters) #LOne is assigned a random letter 
    LTwo = random.choice(string.ascii_letters) #LTwo is assigned a random letter
    LThree = random.choice(string.ascii_letters) #LThree is assigned a random letter
    global UniqueID
    UniqueID = "ID" + " " + LOne+LTwo+LThree #UniqueID is assigned the word ID followed by the random letters from LOne, Two and Three

ID()

def Voting():
    global vb
    vb = pd.read_csv('Voting bal.csv') #assignes the Voting Bal.csv to the word vb 
    time.sleep(1)
    print("Please order from 1 to 4 your preferences (1 being the highest, 4 being the lowest)")
    time.sleep(2)
    print("Here are the Candidates")
    time.sleep(1)
    print('--------')
    print(vb['Candidates']) #displays the voting bal csv
    print('--------')

    print('Starting numbering candidates')
    time.sleep(1)
    VOne = input("HUNNERUP, DAVID ") #Vone is assigned a value
    time.sleep(1)
    VTwo = input("SMITH, Silvia ") #VTwo is assigned a value
    time.sleep(1)
    VThree = input("SMITH, Warwick ") #Vthree is assigned a value 
    time.sleep(1)
    VFour = input("AUSTEN, Brain ") #VFour is assigned a value

  
    vb[UniqueID] = VOne, VTwo, VThree, VFour #creates a collumn with the header from UnqiueID and the assigned values from Vone to four
    vb.to_csv('Voting bal.csv', index = False) #updates the voting bal csv file, index false means it wont add the collumnn that lables the rows

Voting()

def UpdateVote():
    position = df.loc[df['First Name'].isin([FirstName])]['IDNum'].iat[0] #positions is allocated the IDNum corresponding to the First Name
    positionUpdate = position - 1 #ID Num begins with a 1 however the program starts the csv with 0 
    df.loc[int(positionUpdate), 'Has Voted?'] = "Yes" #updates the Has Vote collumn to Yes corresponding to the user
    df.to_csv("Sample Electoral Roll 2022.csv", index = False) #updates the csv file
UpdateVote()