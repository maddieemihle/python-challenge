# PyBank Data Analysis

# Import modules for reading CSV files
import csv
import os

# File path for load and output for PyBank
csvpath = os.path.join('.', 'PyBank/Resources', 'budget_data.csv')  # Input file path
txt_output = os.path.join('PyBank/analysis', 'budget_analysis.txt')  # Output file path

# Define variables to track the financial data 
total_months = 0
total_net = 0

# Define variables for profit changes, average of changes, greatest increase, greatest decrease.
profit_changes =[]
average_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", float('inf')]

# Open and read the csv
with open(csvpath, newline='', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Extract first row to initalize the variables to avoid appending "net change list" and track the total and net changes
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])  # The net total amount of "Profit/Losses" over the entire period
    prev_net = int(first_row[1])

    # Process each row of data
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])

        # Calculate the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        profit_changes.append(net_change)

        # Calculate the greatest increase and decrease in profits 
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
average_change = sum(profit_changes) / len(profit_changes)

# Open a text file to save the output
with open(txt_output, "w") as txt_file:

    # Print the total and net changes (to terminal)
    txt_output = (
        f"\n\nFinancial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average  Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )
    print(txt_output, end="")

    # Write the total and net changes to the text file
    txt_file.write(txt_output)
