#import csv module for reading/writing csv files
import csv

#store path to csv file
file = 'budget_data.csv'

#initialize variables
months = []
profit_loss = []
profit_loss_total = 0

#open file and store header
with open(file) as f:
    csvreader = csv.reader(f)
    header = next(csvreader)

    #iterate over each row in file
    for row in csvreader:
        
        #append the 1st column value to months list
        months.append(row[0])
        
        #append the 2nd column value to the profit_loss list
        profit_loss.append(int(row[1]))
        
        #increment the value of profit_loss_total
        profit_loss_total += int(row[1])
        
#use the len function to retrieve the number of items in 'months' list and store as a variable
number_of_months = len(months)

#list comprehension to create a list of changes in profit/loss for each month
profit_loss_month = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]


#find average of profit_loss_month list
#---------------------------------------------------
#initialize total to 0
total = 0

#iterate over profit_loss_month list using for loop
for number in profit_loss_month:

#increment total value
    total += number

#return average by dividing the total by the length of the profit_loss_month list and round to 2 decimals
average = round(total/len(profit_loss_month),2)
#---------------------------------------------------

#remove first item from 'months' list so we can correctly align the 'months' and 'profit_loss_month' lists for zipping
months.remove('Jan-2010')

#zip 'months' list and 'profit_loss_month', turn into a list, and then find the respective max/min profits by passing a lambda function to the key argument of the 'max'/'min' function that tells the function to search the 2nd values of the zipped list
#return the max/min values and associated months by indexing to the desired item and save as variable
max_month = max(list(zip(months, profit_loss_month)),key = lambda x: x[1])[0]
max_profit = max(list(zip(months, profit_loss_month)),key = lambda x: x[1])[1]
min_month = min(list(zip(months, profit_loss_month)),key = lambda x: x[1])[0]
min_profit = min(list(zip(months, profit_loss_month)),key = lambda x: x[1])[1]

#print the results of the prior analysis, using f-strings to assign respective variables
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${profit_loss_total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_month} (${min_profit})")

#save results of analysis to a txt file
with open ('Financial Analysis.txt', 'w') as f:
    f.write(f"Financial Analysis\n")
    f.write(f"----------------------\n")
    f.write(f"Total Months: {number_of_months}\n")
    f.write(f"Total: ${profit_loss_total}\n")
    f.write(f"Average Change: ${average}\n")
    f.write(f"Greatest Increase in Profits: {max_month} (${max_profit})\n")
    f.write(f"Greatest Decrease in Profits: {min_month} (${min_profit})\n")