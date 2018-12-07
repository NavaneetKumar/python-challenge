# Modules
import os
import csv

# Set path for file
csvpath = os.path.abspath("budget_data.csv")

# Set variables
# Month count
monthcnt = 0
# Total Profil/Loss Amount
plamt = 0
# Current Profit/Loss Amount
curplamt = 0
# Previous Profilt/Loss Amount
preplamt = 0
# Total change in Profit/Loss Amount
plamtchg = 0
# Greatest Increase
IncMonth = ""
IncAmt  = 0
# Greatest Decrease
DecMonth = ""
DecAmt = 0

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    csv_header = next(csvreader)    

    # Loop through data file
    for row in csvreader:
        monthcnt += 1
        curplamt = int(row[1])
        plamt += curplamt

        # Find the greatest Increase
        if IncAmt < curplamt - preplamt: 
            IncAmt = curplamt - preplamt
            IncMonth = row[0]

        # Find the greatest Decrease
        if DecAmt > curplamt - preplamt:
            DecAmt = curplamt - preplamt
            DecMonth = row[0]

        # Calculate the change
        if preplamt != 0:
            plamtchg += (preplamt - curplamt)

        # Save the Amount for next month
        preplamt = curplamt

text = f'''Financial Analysis
----------------------------------
Total Months: {monthcnt}
Total: ${plamt}
Average  Change: ${round(plamtchg/(monthcnt-1),2)}
Greatest Increase in Profits: {IncMonth} (${IncAmt})
Greatest Decrease in Profits: {DecMonth} (${DecAmt})
'''

print(text)

# Write in the file
f = open("PyBank_output.txt","w")
f.write(text)