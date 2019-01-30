#*******************************************************************************
# Application Name: PyPoll
# Author: Rod Skoglund
# Description: Reads in a file with election data (Voter ID, County, and 
#    Candidate), analyzes the votes and calculates each of the following:
#      * The total number of votes cast
#      * A complete list of candidates who received votes
#      * The percentage of votes each candidate won
#      * The total number of votes each candidate won
#      * The winner of the election based on popular vote.
#
#    The Summary Data is output in a file and displayed on the terminal.
#
#*******************************************************************************

#*******************************************************************************
# Modules
#*******************************************************************************
import os
import csv

#*******************************************************************************
# Initialize variables
#*******************************************************************************
voterIDCol = 0
countyCol = 1
candidateCol = 2
voteCount = 0
winner = ""
winnerTotal = 0

candidateInfoList = []

#*******************************************************************************
# Functions
#*******************************************************************************
def nameInList(name):
  candidateInList = False
  for c in candidateInfoList:
    if c['candidate'] == name:
      candidateInList = True
  return candidateInList

#*******************************************************************************
# Set path for file
#*******************************************************************************
csvpath = os.path.join("Resources", "election_data.csv")

#*******************************************************************************
# Open input file and process all the lines in the file
#*******************************************************************************
with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  #*****************************************************************************
  # Read the header row so it won't be processed with the rest of the data in 
  # the file.
  #*****************************************************************************
  csv_header = next(csvreader)

  #*****************************************************************************
  # Read and process each row of data after the header. calculate total votes 
  # for each candidate
  #*****************************************************************************
  for row in csvreader:
    voteCount += 1
    if nameInList(row[candidateCol]):
      for d in candidateInfoList:
        if d['candidate'] == row[candidateCol]:
          d['voteCount'] += 1
    else:
      candidateInfoList.append({"candidate": row[candidateCol], "voteCount": 1})

  #*****************************************************************************
  # Write results to the terminal
  #*****************************************************************************
  print("Election Results")
  print("----------------------------------------")
  print(f"Total Votes: {voteCount}")
  print("----------------------------------------")

  #*****************************************************************************
  # Write results for each candidate to the terminal. Determine winneer which 
  # will be printed later.
  #*****************************************************************************
  for c in candidateInfoList:
    percentOfVotes = float(c['voteCount']/voteCount  * 100)
    if c['voteCount'] > winnerTotal:
      winner = c['candidate']
      winnerTotal = c['voteCount']

    print(f"{c['candidate']}: {'%.3f' % percentOfVotes}% ({c['voteCount']})")

  #*****************************************************************************
  # Write winner to the terminal
  #*****************************************************************************
  print("----------------------------------------")
  print(f"Winner: {winner}")
  print("----------------------------------------")

#*******************************************************************************
# Output results/summary to a file
#*******************************************************************************
output_path = os.path.join("output", "PyPollOutput.txt")

#*******************************************************************************
# Open the file using "write" mode. Specify the variable to hold the contents
#*******************************************************************************
with open(output_path, 'w') as text_file:
  #*****************************************************************************
  # Write results to the file
  #*****************************************************************************
  text_file.write("Election Results" + "\n")
  text_file.write("----------------------------------------" + "\n")
  text_file.write(f"Total Votes: {voteCount}" + "\n")
  text_file.write("----------------------------------------" + "\n")

  #*****************************************************************************
  # Write results for each candidate to the file
  #*****************************************************************************
  for can in candidateInfoList:
    percentOfVotes = float(can['voteCount']/voteCount  * 100)
    text_file.write(f"{can['candidate']}: {'%.3f' % percentOfVotes}% ({can['voteCount']})" + "\n")

  #*****************************************************************************
  # Write winner to the file
  #*****************************************************************************
  text_file.write("----------------------------------------" + "\n")
  text_file.write(f"Winner: {winner}" + "\n")
  text_file.write("----------------------------------------" + "\n")
