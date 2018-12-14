import os

import csv

ElectionDataCSV = os.path.join("..", "Resources", "election_data.csv")

# Create lists to store data
TotalVotesCast = []
PercentofVotesbyCandidate = []
TotalVotesbyCandidate = []
PopularVoteWinner = []

# Open and read the csv file
with open(ElectionDataCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        TotalVotesCast.append(row[1])
        PercentofVotesbyCandidate.append(row[2])
        TotalVotesbyCandidate.append(row[3])
        PopularVoteWinner.append(row[4])
