'''
INSTRUCTIONS:
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
•	The total number of votes cast
•	A complete list of candidates who received votes
•	The percentage of votes each candidate won
•	The total number of votes each candidate won
•	The winner of the election based on popular vote
Your analysis should align with the following results:
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

'''
#import dependencies module and files
import os
import csv

# Identifies file with poll data
pypollcsv = os.path.join("/Users/jessssamyn/Documents/PyPoll" , "Resources" , "election_data.csv")

#variables to store data
total_votes = 0
candidates = []
candidate_votes = {}
winning_candidate = ""
count_winner = 0

#gets data file
with open(pypollcsv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        #if candidate does not match an existing candidate...
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        #add a vote to candidates count
        candidate_votes[candidate] += 1

#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#candidates total unqique votes
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage: .3f}% ({votes})")
    
    #determine winner by looping through counts
    if votes > count_winner:
        count_winner = votes
        winning_candidate = candidate

print("-------------------------")
print(f"Winner: {winning_candidate}")

#Export analysis to text file
with open('election_reults.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage: .3f}% ({votes})\n")

        if votes > count_winner:
            count_winner = votes
            winning_candidate = candidate

    file.write("-------------------------\n")
    file.write(f"Winner: {winning_candidate}\n")
