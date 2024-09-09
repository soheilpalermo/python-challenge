import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
months = []
profit_losses = []
monthly_changes = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read the first row (so we can calculate the changes properly)
    first_row = next(csvreader)
    previous_profit = int(first_row[1])
    months.append(first_row[0])
    profit_losses.append(previous_profit)
    
    # Loop through each row of data after the first row
    for row in csvreader:
        # Track the month and profit/loss
        months.append(row[0])
        profit_losses.append(int(row[1]))
        
        # Calculate the monthly change and add it to the list
        monthly_change = int(row[1]) - previous_profit
        monthly_changes.append(monthly_change)
        previous_profit = int(row[1])

# Calculate the total number of months
total_months = len(months)

# Calculate the total net amount of Profit/Losses
total_profit = sum(profit_losses)

# Calculate the average of the changes in Profit/Losses
average_change = sum(monthly_changes) / len(monthly_changes)

# Find the greatest increase in profits (max of monthly_changes)
greatest_increase = max(monthly_changes)
greatest_increase_month = months[monthly_changes.index(greatest_increase) + 1]

# Find the greatest decrease in profits (min of monthly_changes)
greatest_decrease = min(monthly_changes)
greatest_decrease_month = months[monthly_changes.index(greatest_decrease) + 1]

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Output the results to a text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
