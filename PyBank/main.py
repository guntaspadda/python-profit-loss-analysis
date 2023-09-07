import os
import csv

# Open the file of interest and put it in read mode
csvpath = os.path.join('.','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    
    # TOTAL MONTHS: Create a counter for every row with data, and count the total number of rows in the dataset
    # TOTAL PROFIT: Create a list with all the values in the profit/loss column. Then sum the contents of the list
    # AVERAGE PROFIT: Create a new list that captures the change between subsequent values in the profit/loss list. Take an average of the contents of the new list
    # GREATEST INCREASE: Take the max of the list of changes
    # GREATEST DECREASE: Take the min of the list of changes
    # GREATEST INCREASE MONTH: Take the index of the greatest increase and match it to the month column
    # GREATEST DECREASE MONTH: Take the index of the greatest decrease and match it to the month column
    
    rowcount = 1
    profits_and_losses = [int(first_row[1])]
    previous_net = int(first_row[1])
    changes = []
    months = []
    for row in csvreader:
        rowcount +=1
        profits_and_losses.append(row[1])
        
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        changes.append(net_change)
        
        month = str(row[0])
        months.append(month)
        
    int_profits_and_losses = [float(value) for value in profits_and_losses]
    sumprofits = sum(int_profits_and_losses)
    int_changes = [float(value) for value in changes]
    sumchanges = sum(int_changes)
    lenchanges = len(int_changes)
    averagechange = sumchanges/lenchanges
    maxchange = max(int_changes)
    minchange = min(int_changes)
    maxchange_month = (months[int_changes.index(maxchange)])
    minchange_month = (months[int_changes.index(minchange)])
  


with open('Analysis/results.text','w') as f:
    
    f.write('Financial Analysis\n')
    f.write('-----------------\n')
    f.write('Total Months: ' + str(rowcount))
    f.write(' \n')
    f.write('Total: $' + str(sumprofits))
    f.write(' \n')
    f.write('Average Change: $' + str(averagechange))
    f.write(' \n')
    f.write('Greatest Increase in Profits: ' + (maxchange_month) + ' $' + str(maxchange))
    f.write(' \n')
    f.write('Greatest Decrease in Profits: ' + (minchange_month) + ' $' + str(minchange))
    f.write(' \n')