import csv

# Source the file from election_data.csv
file_path = "Resources/election_data.csv"

# To start, set total votes to 0, candidates as a dictionary, winner votes to 0 and winner name to blank
total_votes = 0
candidates = {}
winner_votes = 0
winner_name = ""

# Open the CSV file and read the data
with open(file_path, newline="") as election_data_csv:
    read_election_data_csv = csv.reader(election_data_csv, delimiter=",")
    
    # Stores the header row
    header = next(election_data_csv) 
    
    # Loop the data in the csv
    for row in read_election_data_csv:
        
        # Keep a tally of the total votes, I discovered that += will loop and increment so I'll use that instead of total_votes + 1
        total_votes += 1
        
        # Keep the vote count using a similar methodology
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop the candidates and display their data
for candidate in candidates:
    # Calculate the percentage of votes each candidate won
    vote_percentage = (candidates[candidate] / total_votes) * 100
    
    # Print the candidate's name, percentage of votes, and vote count
    print(f"{candidate}: {vote_percentage:.3f}% ({candidates[candidate]})")
    
    # Return the winner based on the loop data
    if candidates[candidate] > winner_votes:
        winner_votes = candidates[candidate]
        winner_name = candidate

print("-------------------------")

# Print the winner name
print(f"Winner: {winner_name}")
print("-------------------------")

# Print the header for fun just as proof that the header was successfully stored
print(f"The header rows were: {header}")

# Make a .txt with the data formatted to the way the module assignment showed
with open("PyPoll_Summary.txt", "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    
    # Loop all the candidates and figure out what the vote percentage is using total_votes
    for candidate in candidates:
        vote_percentage = (candidates[candidate] / total_votes) * 100
        outfile.write(f"{candidate}: {vote_percentage:.3f}% ({candidates[candidate]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner_name}\n")
    outfile.write("-------------------------\n")
    
    # Write the header for fun just as proof that the header was successfully stored
    outfile.write(f"The header rows were: {header}\n")