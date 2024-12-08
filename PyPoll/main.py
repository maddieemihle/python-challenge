# PyPoll Data Analysis

# Import modules for reading CSV files
import csv
import os

# Files to load and output
csvpath = os.path.join('.', 'PyPoll/Resources', 'election_data.csv')  # Input file path
output_file = os.path.join('PyPoll/analysis', 'election_analysis.txt')  # Output file path

# Initialize variables to track the election data, winning candidate, and winning count tacker
total_votes = 0  # Track the total number of votes cast
winning_candidate = ""  
winning_count = 0
winning_percentage = 0

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}  # Track the candidate vote counts
candidate_names = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]  # Track the candidate names

# Open the CSV file and process it
with open(csvpath, newline='', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Loop through each row of the dataset and process it
    for row in csvreader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them to the list
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output file
with open(output_file, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        # Retrieve the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        # Print and write each candidate's vote count and percentage
        candidate_results = (f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        print(candidate_results, end="")

        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)
