import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

votes = 0
winner = ""
winner_votes=0
candidates = ""

candidates = {}
 
with open (csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        csvheader = next(csvreader)
        
        for row in csvreader:
           votes = votes + 1      #for every new row add 1 to the count variable 'votes' to get total votes
           
           if row[2] in candidates:   #if the key name in column 3 is in candidate dictionary
                candidates[row[2]] = candidates[row[2]] + 1  #add one to the key value count

           else: 
               candidates[row[2]] = 1         #else the candidate key in dictionary is one
           #for name in candidates:

            #list of candidates that received votes   loop through dictionary and print out 


print ("Election Results")
print ('-------------------------')          
print (f"Total Votes: {votes}")
print ('-------------------------') 
for key, value in candidates.items():  #pulls out key and value and returns them
    print (f"{key}: {100*value/votes} {value}")
    if value > winner_votes:
        winner = key 
        winner_votes = value    
print ('-------------------------')
print (f"Winner: {winner}")

output_path = os.path.join("Analysis", "new.txt")   

with open(output_path, 'w') as txt_file:
    txt_file.write ("Election Results")
    txt_file.write ('-------------------------')          
    txt_file.write (f"Total Votes: {votes}")
    txt_file.write ('-------------------------')
    for key, value in candidates.items():  
        txt_file.write (f"{key}: {100*value/votes} {value}")
        if value > winner_votes:
            winner = key 
            winner_votes = value 
    txt_file.write ('-------------------------')
    txt_file.write (f"Winner: {winner}")
  
