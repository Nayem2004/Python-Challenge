import csv
import os

# Defines the main function.
def main():
    # File path for the CSV file.
    file_path = os.path.join(os.getcwd(), 'election_data.csv')

    # Initializes the variables.
    total_votes = 0
    candidate_votes = {}

    # Try to open and read the CSV file.
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Skips the header row.
            header = next(csv_reader)
            
            # Loops through each row in the CSV.
            for row in csv_reader:
                total_votes += 1
                candidate = row[2]
                
                # If the candidate is already in the dictionary, this increments their vote count.
                if candidate in candidate_votes:
                    candidate_votes[candidate] += 1
                else:
                    candidate_votes[candidate] = 1

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found. Please check the file path and try again.")
        return

    # Calculates the winner and the percentage of votes each candidate won
    winner = None
    max_votes = 0
    results = []
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        results.append(f"{candidate}: {percentage:.3f}% ({votes})")
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    # Generates the election results report.
    report = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
        + "\n".join(results) +
        "\n-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    )

    # Prints the analysis to the terminal.
    print(report)

    # Exports the analysis to a text file.
    output_file = 'election_results.txt'
    with open(output_file, mode='w') as file:
        file.write(report)

    print(f"\nThe election results have been saved to '{output_file}'.")

# Calls the main function when the script is executed
if __name__ == "__main__":
    main()

