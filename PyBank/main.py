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
    print(header)

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
#--------------------------------------
#initialize total to 0
total = 0

#iterate over profit_loss_month list using for loop
for number in profit_loss_month:

#increment total value
    total += number

#return average by dividing the total by the length of the profit_loss_month list and round to 2 decimals
average = round(total/len(profit_loss_month),2)
#--------------------------------------

#use max function to store the maximum value of the profit_loss_month list
max_profit = max(profit_loss_month)

#use min function to store the minimum value of the profit_loss_month list
min_profit = min(profit_loss_month)

