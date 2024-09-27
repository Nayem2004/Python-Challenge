#PyBank

import csv
import os

# Defines the main function.
def main():
    # File path for the CSV file (update as needed)
    file_path = os.path.join(os.getcwd(), 'budget_data.csv')

    # Initializes variables.
    total_months = 0
    net_total = 0
    previous_profit_loss = None
    changes = []
    dates = []

    # Variables for tracking the greatest increase and decrease in profits.
    greatest_increase = {'date': '', 'amount': float('-inf')}
    greatest_decrease = {'date': '', 'amount': float('inf')}

    # Try to open and read the CSV file.
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Skips the header row.
            header = next(csv_reader)
            
            # Loops through each row in the CSV.
            for row in csv_reader:
                date = row[0]
                profit_loss = int(row[1])
                
                # Counts the total months and calculates the net total amount.
                total_months += 1
                net_total += profit_loss
                
                # Tracks changes in profit/loss from the previous month.
                if previous_profit_loss is not None:
                    change = profit_loss - previous_profit_loss
                    changes.append(change)
                    dates.append(date)
                    
                    # Checks for greatest increase in profits.
                    if change > greatest_increase['amount']:
                        greatest_increase = {'date': date, 'amount': change}
                    
                    # Checks for greatest decrease in profits.
                    if change < greatest_decrease['amount']:
                        greatest_decrease = {'date': date, 'amount': change}
                
                # Updates the previous profit/loss value.
                previous_profit_loss = profit_loss

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found. Please check the file path and try again.")
        return

    # Calculates the average change in "Profit/Losses".
    average_change = sum(changes) / len(changes)

    # Generates the financial analysis report.
    report = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
        f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

    # Prints the analysis to the terminal.
    print(report)

    # Exports the analysis to a text file.
    output_file = 'financial_analysis.txt'
    with open(output_file, mode='w') as file:
        file.write(report)

    print(f"\nThe financial analysis has been saved to '{output_file}'.")

# Calls the main function when the script is executed.
if __name__ == "__main__":
    main()

