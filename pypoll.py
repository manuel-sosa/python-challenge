import csv

file_to_load = "election_data.csv"
file_to_output = "pypoll-challenge.txt"

# Total Vote Counter
total_votes = 0

# Candidates Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read in the CSV and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        total_votes = total_votes + 1
        
        # Candidate name
        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print results and export data to pypoll-challenge.txt
with open(file_to_output, "w") as txt_file:

    # Print final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n"
    )

    print(election_results)

    # Save final vote count 
    txt_file.write(election_results)

    # Winner by looping through counts
    for candidate in candidate_votes:

        # Votes!
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        # Print candidates' voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes}\n)"
        print(voter_output)

        txt_file.write(voter_output)

        winning_candidate_summary = (
            f"---------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"---------------------------------\n"
            )
        
        print(winning_candidate_summary)

        # Save the winning candidate's name to pypoll-challenge.txt 
        txt_file.write(winning_candidate_summary)
