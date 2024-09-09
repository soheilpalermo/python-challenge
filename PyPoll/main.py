import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Dictionary to hold candidate names and their corresponding votes
candidate_votes = {}

# Total vote counter
total_votes = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    header = next(csvreader)

    # Process each vote
    for row in csvreader:
        # Increment total votes
        total_votes += 1

        # Candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        
        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the results and export the data to a text file
output_path = os.path.join("analysis", "election_results.txt")

with open(output_path, "w") as txtfile:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    txtfile.write(election_results)

    # Determine the winner by looping through the counts
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print each candidate's voter count and percentage
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        print(candidate_results, end="")
        txtfile.write(candidate_results)
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txtfile.write(winning_candidate_summary)
