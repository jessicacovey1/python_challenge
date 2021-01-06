import os
import csv

csvpath = os.path.join(".","Resources", "election_data.csv")

votes = 0
winner = ""
candidates = ""
percentage = 0
new = True

candidates = {}
 
with open (csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        csvheader = next(csvreader)
        
        for row in csvreader:
           
           for name in candidates:

            if row[2] == name:
                new = False
                candidates[name] = candidates[name] + 1
            # * The total number of votes cast
            #print (votes)

        if new == True:
            candidates[row[2]] = 1
      
             

        for key, value in candidates.items():
            if value > # value is total votes for thtat candidate -not sure greater than other candidates total votes then
                    #winner = key

        #print (f"{key}: + {value}")

print ("Election Results")
print ('-------------------------')          
print (f"Total Votes: {votes}")
print ('-------------------------') 
print (f"{key}: + {percentage} + {value}")
print ('-------------------------')
print (f"Winner: {winner}")

output_path = os.path.join("Analysis", "new.txt")   

with open(output_path, 'w') as txt_file:
    txt_file.write ("Election Results")
    txt_file.write ('-------------------------')          
    txt_file.write (f"Total Votes: {votes}")
    txt_file.write ('-------------------------') 
    txt_file.write (f"{key}: + {percentage} + {value}")
    txt_file.write ('-------------------------')
    txt_file.write (f"Winner: {winner}")
  


    
#The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------