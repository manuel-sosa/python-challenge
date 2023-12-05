import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")

with open(filepath) as filedata:
    reader = csv.reader(filedata)
    header = next(reader)

    # initialize variables
    total_months = 0
    total_pl = 0
    change_pl_list = []
    previous_pl = 0
    change_pl = 0
    average_change = 0
    greatest_incrase = ["", 0]
    greatest_decrease = ["", 999999999999999999]

    for row in reader:
        
        if total_months == 0:        
            previous_pl = int(row[1])

        total_pl = total_pl + int(row[1])
        total_months = total_months + 1

        change_pl = int(row[1]) - previous_pl
        change_pl_list.append(change_pl)
        previous_pl = int(row[1])

    change_pl_list.pop(0)
    average_change = sum(change_pl_list) / len(change_pl_list)
    
    greatest_increase = df.loc(change_pl).idxmax
    greatest_decrease = df.loc(change_pl).idxmin

    print("\n")
    print("------------------")
    print("Financial Analysis")
    print("------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_pl}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: ${greatest_increase[0]} (${greatest_increase[1]})')
    print(f'Greatest Decrease in Profits: ${greatest_decrease[0]} (${greatest_decrease[1]}')
    
# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

