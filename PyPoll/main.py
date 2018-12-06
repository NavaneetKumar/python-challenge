# Modules
import os
import csv

Pollresult = {}

def CountVote(name,vote=1):
    # Check if the Candidate already exists
    if name in Pollresult:
        # if yes then update it's vote count
        Pollresult[name] += vote
    else:
        # if not them add him first
        Pollresult[name] = vote



# Set path for file
csvpath = os.path.abspath("C:/BootCamp/PREWORK_NK/Python Home work/election_data.csv")

# Set variables
totvote = 0
winner = ""
winnervote = 0

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    csv_header = next(csvreader)    

    # Loop through the data file
    for row in csvreader:
        totvote += 1
        # Add the Candidates and update their vote counts
        CountVote(row[2])


text = f'''Election Results
-------------------------
Total Votes: {totvote}
-------------------------'''

# Loop through the dictionary
for name, vote in Pollresult.items():
    text += f'''\n{name}: {"{:.3%}".format(vote/totvote)} ({vote})'''
    # Find the winner
    if winnervote < vote:
        winnervote = vote
        winner = name

text += f'''
-------------------------
Winner: {winner}
-------------------------
'''

print(text)

# Write in the file
f = open("PyPoll_output.txt","w")
f.write(text)