import os

import csv

BudgetDataCSV = os.path.join("..", "Resources", "budget_data.csv")

# Create lists to store data
TotalMonths = []
NetProfit = []
AverageMonthlyProfitChange = []
LargestProfitIncrease = []
LargestLossDecrease = []

# Open and read the csv file
with open(BudgetDataCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        TotalMonths.append(row[1])
        NetProfit.append(row[2])
        AverageMonthlyProfitChange.append(row[3])
        LargestProfitIncrease.append(row[4])
        LargestLossDecrease.append(row[5])
        





    



# Convert integer months into string and print
