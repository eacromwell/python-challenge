import csv

# Using with open to open the budget data csv
with open('Resources/budget_data.csv', 'r') as budget_data_csv:
    read_budget_data_csv = csv.reader(budget_data_csv, delimiter=',')
    
    # Stores the header row
    header = next(budget_data_csv) 
    
    # Make dates and profits empty lists that we will add to
    dates = []
    profits = []
    
    # Loop each row 
    for row in read_budget_data_csv:
        dates.append(row[0])
        profits.append(int(row[1]))

# Figure out all the data needed

# Total months is the length (or quantity) of items in the list "dates"
total_months = len(dates)

# Total profit is the sum of the profits list
total_profit = sum(profits)

# Figure changes as a list that is made using a for loop that compares the differences in the second row with the first and records it
changes = [profits[i+1]-profits[i] for i in range(len(profits)-1)]

# Then we just need to figure out the average of changes, so we just add changes and divide it by the quantity of datapoints (len)
average_change = sum(changes)/len(changes)

# Highest number is the max in the changes list
greatest_increase = max(changes)

# Lowest number is the min in the changes list
greatest_decrease = min(changes)

# This was really tricky, basically saying the greatest increase date is the dates list where the called index is the index of the greatest increase in the changes list but we have to add one because the changes list is one row shorter since the range was len(profits)-1. we reduced the range of changes by 1 because we technically skipped the first row since we only calculate the changes between two numbers so inevitably the list is shorter by 1.
greatest_increase_date = dates[changes.index(greatest_increase)+1]

# Same thing but for decrease
greatest_decrease_date = dates[changes.index(greatest_decrease)+1]

# Print the analysis to the terminal, make it match the assignment layout
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Print the header for fun just as proof that the header was successfully stored
print(f"The header rows were: {header}")

# Export a text file with the results
with open('PyBank_Summary.txt', 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_profit}\n")
    
    # Need to use .2f to format the decimals in Average Change
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    
    # Need to make sure to use $ to display the currency format
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
    
    # Write the header for fun just as proof that the header was successfully stored
    outfile.write(f"The header rows were: {header}\n")
