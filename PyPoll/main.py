#import csv library
import csv

#assign filepath to a variable
filepath = 'election_data.csv'

#initialize total_votes (integer) and candidate_votes (list) variables
total_votes = 0
candidate_votes = []

#read in csv file, store header, increment total_votes by 1 for each row, and append the value of the the 3rd column from each row to the candidate_votes list
with open(filepath) as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_votes.append(row[2])

        
#-----------------------------------------------------------------------------------------------------------------------------------------------
#for loop to total up number of votes for each candidate

#initialize an empty dictionary
candidate_dict = {}

#create a set from candidate_votes list to identify unique values and loop through each name
for name in set(candidate_votes):
    
    #initialize candidate vote total to 0
    candidate_dict[name] = 0
    
    #loop through each item in the candidate_votes list
    for item in candidate_votes:
        
        #if the name in candidate_votes list matches current name in loop pulled from the set then increment that candidate's vote total by 1
        if item == name:
            candidate_dict[name] += 1            
#-----------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------
#for loop to calculate the percentage of votes won by each candidate

#initialize an empty dictionary
percent_won = {}

#loop over the key/value pairs of the candidate_dict dictionary
for key, value in candidate_dict.items():
    
    #for each candidate (key), divide their number of votes (value) by the total number of votes
    percent_won[key] = round(value/total_votes*100,2)
#------------------------------------------------------------------------------------------------

#save the winner to a variable by selecting the max value from candidate_dict, using the 'key' argument to tell the function to search based on the value from each key/value pair
winner = max(candidate_dict, key=lambda key: candidate_dict[key])

#print out results
print('Election Results')
print('------------------------')
print(f"Total Votes: {total_votes}")
print('------------------------')
print(f"Khan: {percent_won['Khan']}% ({candidate_dict['Khan']})")
print(f"Correy: {percent_won['Correy']}% ({candidate_dict['Correy']})")
print(f"Li: {percent_won['Li']}% ({candidate_dict['Li']})")
print(f'''O'Tooley: {percent_won["O'Tooley"]}% ({candidate_dict["O'Tooley"]})''')
print('------------------------')
print(f"Winner: {winner}")
print('------------------------')

#export the results to a text file
with open('Election_Results.txt', 'w') as f:
    f.write('Election Results\n')
    f.write('------------------------\n')
    f.write(f"Total Votes: {total_votes}\n")
    f.write('------------------------\n')
    f.write(f"Khan: {percent_won['Khan']}% ({candidate_dict['Khan']})\n")
    f.write(f"Correy: {percent_won['Correy']}% ({candidate_dict['Correy']})\n")
    f.write(f"Li: {percent_won['Li']}% ({candidate_dict['Li']})\n")
    f.write(f'''O'Tooley: {percent_won["O'Tooley"]}% ({candidate_dict["O'Tooley"]})\n''')
    f.write('------------------------\n')
    f.write(f"Winner: {winner}\n")
    f.write('------------------------')
