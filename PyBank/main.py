import os
import csv

csvpath = os.path.join(".","Resources", "budget_data.csv")

months = 0
total = 0
sum_change = 0
maximum = 0
maximum_date = ''
minimum = 9999999999999
minimum_date = ''
index = 0

change_values = []
dates = []
 
with open (csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        csvheader = next(csvreader)
        for row in csvreader:
            months = months + 1
            total = total + float(row[1])
            change_values.append(row[1])
            dates.append(row[0])
        #print (change_values)

        for row in change_values:
                if index >= 1:
                    #print (change_values[temp])
                    calc = float(change_values[index]) - float(change_values[index-1])
                    #print (calc)
                    sum_change = calc + sum_change
                    if calc > maximum:
                        maximum = calc
                        maximum_date = dates[index]
                    if calc < minimum:
                        minimum = calc
                        minimum_date = dates[index]
                index = index + 1
average = sum_change / (months-1)
#print (average)

print ("Financial Analysis")
print ('-------------------------')          
print (f"Total Months: {months}")
print (f"Total: ${total}")
print (f"Average Change: ${average}")
print (f"Greatest Increase in Profits: {maximum_date}, ${maximum}")
print (f"Greatest Decrease in Profits: {minimum_date}, ${minimum}")

output_path = os.path.join("Analysis", "new.txt")   

with open(output_path, 'w') as txt_file:
    txt_file.write (f"Financial Analysis")
    txt_file.write (f"---------------------")
    txt_file.write (f"Total Months: {months}")
    txt_file.write (f"Total: ${total}")
    txt_file.write (f"Average Change: ${average}")
    txt_file.write (f"Greatest Increase in Profits: {maximum_date}, ${maximum}")
    txt_file.write (f"Greatest Decrease in Profits: {minimum_date}, {minimum}")