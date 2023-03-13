import csv

# Read the CSV file and store the data in lists
with open('Resources/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # Skip the header row
    dates = []
    profits = []
    for row in csvreader:
        dates.append(row[0])
        profits.append(int(row[1]))

# Calculate the required values
total_months = len(dates)
total_profit = sum(profits)
changes = [profits[i+1]-profits[i] for i in range(len(profits)-1)]
average_change = sum(changes)/len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase)+1]
greatest_decrease_date = dates[changes.index(greatest_decrease)+1]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export a text file with the results
with open('financial_analysis.txt', 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_profit}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
