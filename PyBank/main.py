#*******************************************************************************
# Application Name: PyBank
# Author: Rod Skoglund
# Description: Reads in a file with financial data (Date and Profit/Loss), 
#     determines/calculates the summary data which includes Number of Months, 
#     Net Profit/Loss, Average Profit/Loss change and th Greatest Increase (with 
#     associated Date) and the Greatest Decrease (with associated Date). The 
#     Summary Data is output in a file and displayed on the terminal.
#*******************************************************************************

#*******************************************************************************
# Modules
#*******************************************************************************
import os
import csv

#*******************************************************************************
# Initialize variables
#*******************************************************************************
dateCol = 0
profitLossCol = 1
monthCount = 0
netProfitLoss = 0
aveProfitLossChange = 0
maxIncrease = 0
maxIncreaseDate = ""
maxDecrease = 0
maxDecreaseDate = ""

#*******************************************************************************
# Set path for file
#*******************************************************************************
csvpath = os.path.join("Resources", "budget_data.csv")

#*******************************************************************************
# Open input file and process all the lines in the file
#*******************************************************************************
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #***************************************************************************
    # Read the header row so it won't be processed with the rest of the data in 
    # the file.
    #***************************************************************************
    csv_header = next(csvreader)

    #***************************************************************************
    # Read and process each row of data after the header
    #***************************************************************************
    for row in csvreader:
        #***********************************************************************
        # Update variables
        #***********************************************************************
        monthCount = monthCount + 1
        netProfitLoss = netProfitLoss + int(row[profitLossCol])

        #***********************************************************************
        # If current Profit/Loss value is greater than the current max, 
        # update max value and date with current Profit/Loss value.
        #***********************************************************************
        if int(row[profitLossCol]) >= maxIncrease:
          maxIncrease = int(row[profitLossCol])
          maxIncreaseDate = row[dateCol]

        #***********************************************************************
        # If current Profit/Loss value is less than the current mininum, 
        # update mininum value and date with current Profit/Loss value.
        #***********************************************************************
        if int(row[profitLossCol]) <= maxDecrease:
          maxDecrease = int(row[profitLossCol])
          maxDecreaseDate = row[dateCol]
    
    #***************************************************************************
    # Calculate average Profit/Loss
    aveProfitLossChange = netProfitLoss / monthCount
    #***************************************************************************

#*******************************************************************************
# Output results/summary to a file and the terminal
#*******************************************************************************
output_path = os.path.join("output", "PyBankOutput.txt")

#*******************************************************************************
# Open the file using "write" mode. Specify the variable to hold the contents
#*******************************************************************************
with open(output_path, 'w') as text_file:

    #***************************************************************************
    # Define/Initialize Output lines
    #***************************************************************************
    line1 = "Financial Analysis"
    line2 = "----------------------------"
    line3 = "Total Months: " + str(monthCount)
    line4 = "Total: $" + str(netProfitLoss)
    line5 = "Average Change: $" + str(int(aveProfitLossChange))
    line6 = "Greatest Increase in Profits: " + maxIncreaseDate + " ($" + str(maxIncrease) + ")"
    line7 = "Greatest Decrease in Profits: " + maxDecreaseDate + " ($" + str(maxDecrease) + ")"
    line8 = "----------------------------"

    #***************************************************************************
    # Write output lines to the output file
    #***************************************************************************
    text_file.write(line1 + "\n")
    text_file.write(line2 + "\n")
    text_file.write(line3 + "\n")
    text_file.write(line4 + "\n")
    text_file.write(line5 + "\n")
    text_file.write(line6 + "\n")
    text_file.write(line7 + "\n")
    text_file.write(line8 + "\n")

    #***************************************************************************
    # Write output lines to the terminal
    #***************************************************************************
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)
