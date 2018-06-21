#importing stuff that you later need

import pandas
import xlrd
import random

#1.
#importing table from Excel
df = pandas.read_excel('C:\\Users\\johny\\Desktop\\vaja4\\Zvezek1.xlsx').iloc[:28]

#Extracting data from a row
Home = (df["Home"].values)
Away = (df["Away"].values)
HomeScore = (df["HS"].values)
AwayScore = (df["AS"].values)

#Determening variables
clHome = 0
clAway = 0
gSHome = 0
gSAway = 0
clAvg = 0
gSAvg = 0
trendgS = 0
trendcl = 0

#2.
#Calculates total score and adds values to Avg variables(not actually avarage but when avarage is needed it is corrected with the right equation
#Calculates the trend(I basically calculated it based on how many games each team won)
for i in range(len(Home)):
    if Home[i] == "Warriors" and HomeScore[i] > AwayScore[i]:
        gSHome +=1
        gSAvg +=HomeScore[i]
    elif Home[i] == "Warriors" and HomeScore[i] < AwayScore[i]:
        clAway +=1
        clAvg +=AwayScore[i]
    elif Home[i] == "Cavaliers" and HomeScore[i] > AwayScore[i]:
        clHome +=1
        clAvg +=HomeScore[i]
    else:
        gSAway +=1
        gSAvg +=AwayScore[i]

    if i > 18 and i <= 28:
        if Home[i] == "Warriors" and HomeScore[i] > AwayScore[i]:
            trendgS +=1
        elif Home[i] == "Warriors" and HomeScore[i] < AwayScore[i]:
            trendcl +=1
        elif Home[i] == "Cavaliers" and HomeScore[i] > AwayScore[i]:
             trendcl +=1
        else:
            trendgS +=1
if trendcl > trendgS:
    print("Cavs are da best")
else:
    print("Curry wins again")

#Prints how many times each team won and average points scored
print("Golden State wins:", gSAway+gSHome,"\nCavaliers wins:", clHome+clAway,"\nGolden State home wins:",gSHome,"\nGolden State away wins:",gSAway,"\nCavaliers home wins:",clHome,"\nCavaliers away wins:",clAway)
print("Average points Cavaliers:",clAvg/(clAway+clHome),"\nAverage points Golden State:", gSAvg/(gSAway+gSHome))

#3.
#Random generator which gives the teams different weights
#Calculates the next game based on the weights adding or subtracting from the average
#While loop for eliminating that the teams draw
rng = random.randint(0,100)
a = 0
b = 0
if rng <=65:
    while a == b:
        a = int(round(gSAvg/(gSAway+gSHome) +random.randint(-2,6)))
        b = int(round(clAvg/(clAway+clHome) +random.randint(-6,2)))
    print("Next game prediction:", "Golden State", int(round(a)),"Cavaliers", int(round(b)))
else:
    while a == b:
        a = int(round(gSAvg/(gSAway+gSHome) +random.randint(-6,2)))
        b = int(round(clAvg/(clAway+clHome) +random.randint(-2,6)))
    print("Next game score:", "Golden State", int(round(a)),"Cavaliers", int(round(b)))
#3. 2nd indent: I didn't do. I only know that I had to put the generated predicted game back into the sample with a Fuction

#4. Missing because of missing 3. 2nd indent

#5.Creates the betting sistem which compares the user's and the program algorithems score
#Prints out the outcomes if you correctly predicted the winner,score,..

gSvnos = int(input("Golden State score: "))
cvvnos = int(input("Cavaliers score: "))
cash = 0

if gSvnos > cvvnos and a > b:
    print("Winner winner chicken dinner.")
    cash += 10
    if gSvnos == a and cvvnos == b:
        cash += 500
    elif gSvnos == a or cvvnos == b:
        cash += 100
    elif ((abs(gSvnos-a)) < a*0.08) and ((abs(cvvnos-b)) < b*0.08):
        cash += 40
    elif ((abs(gSvnos-a)) < a*0.08) or ((abs(cvvnos-b)) < b*0.08):
        cash += 15

elif gSvnos < cvvnos and a < b:
    print("Winner winner chicken dinner.")
    cash += 10
    if gSvnos == a and cvvnos == b:
        cash += 500
    elif gSvnos == a or cvvnos == b:
        cash += 100
    elif ((abs(gSvnos-a)) < a*0.08) and ((abs(cvvnos-b)) < b*0.08):
        cash += 40
    elif ((abs(gSvnos-a)) < a*0.08) or ((abs(cvvnos-b)) < b*0.08):
        cash += 15
else:
    print("Wrong call")
print ("You won:",cash,"€")

