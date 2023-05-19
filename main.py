import os
import csv

#Set path for files
budget_csv = os.path.join("..", "Resources", "budget_data.csv")
output = os.path.join("..", "Analysis", "budget.txt")


#Variables
total_months = []
total_profits = []
increase_profit = ["", 0]
decrease_profit = ["", 99999999999]
month_count = 0
net_profit = 0


#open file
with open(budget_csv, "r") as csvfile:
    csvfile = csv.reader(csvfile)
    header = next(csvfile)
    first_row = next(csvfile)

    month_count+=1
    net_profit+=int(first_row[1])
    previous_net=int(first_row[1])


#Dates and profits

    for row in csvfile:
        month_count+=1
        net_profit+=int(row[1])


        net_change=int(row[1])-previous_net
        previous_net=int(row[1])


        total_months.append(row[0])
        total_profits.append(net_change)

        if net_change > increase_profit[1]:
            increase_profit[1]=net_change
            increase_profit[0]=row[0]

        if net_change < decrease_profit[1]:
            decrease_profit[1]=net_change
            decrease_profit[0]=row[0]
            

monthly_average=sum(total_profits)/len(total_profits)

text=f"""
Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${net_profit}
Average Change: ${monthly_average:.2f}
Greatest Increase in Profits: {increase_profit[0]} (${increase_profit[1]})
Greatest Decrease in Profits: {decrease_profit[0]} (${decrease_profit[1]})

"""
print(text)
with open(output, "w") as file:
    file.write(text)

    

