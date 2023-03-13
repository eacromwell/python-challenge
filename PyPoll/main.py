import csv

# Set file path for the data
file_path = "Resources/election_data.csv"

# Initialize variables to store data
total_votes = 0
candidates = {}
winner_votes = 0
winner_name = ""

# Open the CSV file and read the data
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header row
    next(csvreader)
    
    # Iterate through each row of data
    for row in csvreader:
        # Count the total number of votes cast
        total_votes += 1
        
        # Keep track of the vote count for each candidate
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    # Calculate the percentage of votes each candidate won
    vote_percentage = (candidates[candidate] / total_votes) * 100
    
    # Print the candidate's name, percentage of votes, and vote count
    print(f"{candidate}: {vote_percentage:.3f}% ({candidates[candidate]})")
    
    # Check if this candidate has more votes than the current winner
    if candidates[candidate] > winner_votes:
        winner_votes = candidates[candidate]
        winner_name = candidate

print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Export the results to a text file
with open("election_results.txt", "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate in candidates:
        vote_percentage = (candidates[candidate] / total_votes) * 100
        outfile.write(f"{candidate}: {vote_percentage:.3f}% ({candidates[candidate]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner_name}\n")
    outfile.write("-------------------------\n")