'''
Instructions

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyzes the records to calculate each of the following values:
•	The total number of months included in the dataset
•	The net total amount of "Profit/Losses" over the entire period
•	The changes in "Profit/Losses" over the entire period, and then the average of those changes
•	The greatest increase in profits (date and amount) over the entire period
•	The greatest decrease in profits (date and amount) over the entire period
Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

'''
#Import dependencies
import os
import csv

#Set the path to collect data in CSV files
pybankcsv = os.path.join ("/Users/jessssamyn/Documents/PyBank" , "Resources" , "pybank_budget_data.csv")
print(pybankcsv)

#list of variables to store data
months = []
profit_losses = []

total_months = 0
net_total = 0
prev_total = 0
current_total = 0
total_change = 0

#read csv and each row
with open(pybankcsv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_months += 1
        profit_losses.append(int(row[1]))
        current_total += int(row[1])
        months.append(row[0])
    
    #track totals
    if total_months == 1:
        prev_total = current_total
    
    else:
        total_change = current_total - prev_total
        prev_total = current_total

#track revenue change    
total_prof_loss = sum(profit_losses)
avg_change = round(total_change / (total_months - 1), 2)
#calculate increase and decrease
increase_change = max(profit_losses)
decrease_change = min(profit_losses)

#Print analysis to terminal
print("Financial_Analysis")
print("-------------------------------")
print(f"Total Months:" + str(total_months))
print(f"Total: ${total_prof_loss}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {months[profit_losses.index(increase_change)]} (${increase_change})")
print(f"Greatest Decrease in Profits: {months[profit_losses.index(decrease_change)]} (${decrease_change})")

#export data to txt file
with open('budget_analysis.txt','w') as file:
    file.write("Financial_Analysis\n")
    file.write("-------------------------------\n")
    file.write(f"Total Months:\n" + str(total_months))
    file.write(f"Total: ${total_prof_loss}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {months[profit_losses.index(increase_change)]} (${increase_change})\n")
    file.write(f"Greatest Decrease in Profits: {months[profit_losses.index(decrease_change)]} (${decrease_change})\n")

    #Note: the script output does not match exact number shown in instruction example
