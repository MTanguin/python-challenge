# Dependencies
# Create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Module for statistics
import statistics

# Specify the file path
budget_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')

# Set initial values
total_months = 0
net_total = 0
greatest_increase = 0
peak_month = ""
greatest_decrease = 0
lowest_month= ""
change = []
monthly_changes = []

with open(budget_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_months += 1
        net_total += int(row[1])
        if int(row[1]) >= greatest_increase:
            peak_month = (row[0])
            greatest_increase = int(row[1])
        elif int(row[1]) <= greatest_decrease:
            lowest_month = (row[0])
            greatest_decrease = int(row[1])
        change.append(int(row[1]))

  
# track monthly changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthly_changes.append(monthlyChange)   

average_change = statistics.mean(monthly_changes)

print("Financial Analysis")
print("___________________________________")

print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change is: $ {round((average_change), 2)}")
print(f"Greatest Increase in Profits: {peak_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {lowest_month} ${greatest_decrease}")

# write this to an output file
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("___________________________________\n")

f.write(f"Total Months:   {total_months}\n")
f.write(f"Total: ${net_total}\n")
f.write(f"Average Change is: $ {round(average_change,2)}\n")
f.write(f"Greatest Increase in Profits: {peak_month}  ${greatest_increase} \n")
f.write(f"Greatest Decrease in Profits:  {lowest_month} ${greatest_decrease}\n")