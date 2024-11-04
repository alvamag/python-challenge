import csv
import os

inputFile = os.path.join("Election_Data.csv")
outputFile = os.path.join("ElectionDataAnalysis.txt")

#variables
totalVotes = 0 #variable that holds the total votes
candidates = [] #list that holds candidates
candidateVotes = {} #dictionary that will hold the votes for each candidate
winningCount = 0 #variable to hold the winners
winningCandidate = "" #variable to hold the winning candidate

#read the csv file
with open(inputFile) as electionData:
    
    csvreader = csv.reader(electionData) 
    header = next(csvreader) #read the header

    for row in csvreader:
        totalVotes += 1 #add on to the total votes

        if row[2] not in candidates:
            candidates.append(row[2]) #if the candidate is not in the list add it

            candidateVotes[row[2]] = 1

        else:
            candidateVotes[row[2]] += 1

voteOutput = ""

for candidates in candidateVotes:
    votes = candidateVotes.get(candidates)
    votePct = (float(votes) / float(totalVotes)) *100.00
    voteOutput += f"{candidates}: {votePct:.2f}% \n"

    #compare the votes to the winning count
    if votes > winningCount:
        winningCount = votes
        winningCandidate = candidates
    

winningCandidateOutput = f"Winner: {winningCandidate}\n----------------------------"


#output
output = (
    f"\n\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {totalVotes:,}\n"
    f"----------------------------\n"
    f"{voteOutput}\n"
    f"----------------------------\n"
    f"{winningCandidateOutput}"
)

print(output) #displays to the console

#print the results and export the data to a text file
with open(outputFile, "w") as textFile:
    textFile.write(output)
