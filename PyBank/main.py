import csv
import os

#source to read budget data
fileLoad = os.path.join("budget_data.csv")

# file to hold the output of the budget analysis
outputFile = os.path.join("budgetAnalysis.txt")

# variables for months
totalMonths = 0 # initialize the total months to 0
totalPL = 0 #initialize the total budget to 0
monthlyChanges = [] #initialize the list of monthly changes
months = [] #initialize the list of months


# read the csv file
with open(fileLoad) as budgetData:
    csvreader = csv.reader(budgetData)

    header = next(csvreader) #read the header row

    firstRow = next(csvreader)

    totalMonths += 1 #increment the total months

    totalPL += float(firstRow[1]) #add on to the total profits and losses
    
    previousPL= float(firstRow[1]) #previous profits & losses

    
    for row in csvreader:

        totalMonths += 1 #increment the total months

        totalPL += float(row[1]) #add on to the profits and losses

        netChange = float(row[1]) - previousPL #calculate the net change

        monthlyChanges.append(netChange) #add on to the list of monthly changes

        months.append(row[0]) #add the first month that a change occurred

        previousPL = float(row[1])

averageChangePerMonth = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]] # holds the month and the greatest increase
greatestDecrease = [months[0], monthlyChanges[0]] #holds the month and the greatest decrease


# loop to caculate the greatest and least monthly change
for m in range(len(monthlyChanges)):

    if (monthlyChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChanges[m]
        greatestIncrease[0] = months[m]

    if (monthlyChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChanges[m]
        greatestDecrease[0] = months[m]


#start generating the output
output = (
    f"\nBudget Data Analysis \n"
    f"---------------------\n"
    f"Total Months = {totalMonths}\n"
    f"Total Profits & Losses = ${totalPL: ,.2f}\n"
    f"Average Change per Month = ${averageChangePerMonth:,.2f}\n" 
    f"Greatest Increase = {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n"
    f"Greatest Decrease = {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f} \n"
    )


print(output) #print to console

with open(outputFile, "w") as textFile:
    textFile.write(output)