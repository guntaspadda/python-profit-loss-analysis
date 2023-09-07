import os
import csv

# Open the file of interest and put it in read mode
csvpath = os.path.join('.','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    rowcount = 0
    candidates = []
    candidate_votecount = {}
    candidate_percentage = {}
    candidate_results = {}
    for row in csvreader:
        # Total Votes: Count the number of rows in the file
        rowcount += 1 
        
        # Candidate List: Create a list of unique values from the candidate column (source:https://www.geeksforgeeks.org/python-get-unique-values-list/)
        # Total Votes Per Candidate: Store the total votes for each candidate in a dictionary
        candidate = str(row[2])
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votecount[candidate] = 1
        else:
            candidate_votecount[candidate] += 1
            
    # Percentage of Votes Per Candidate: Create a dictionary to store the % votes for each candidate (% format source: https://www.askpython.com/python/examples/print-a-percentage-value-in-python#:~:text=format()%20function.,printed%20in%20the%20next%20line.)
    for candidate in candidates:
        percent_votes_int = int(candidate_votecount[candidate])/rowcount
        percentage_votes = "{:.0%}".format(percent_votes_int)
        candidate_percentage[candidate] = percentage_votes
    for candidate in candidates:
        candidate_results[candidate] = (candidate_percentage[candidate], candidate_votecount[candidate])
        
    # Election Winner: Return the candidate with the max votecount (source: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-80.php#:~:text=Use%20max()%20with%20the,value%20in%20the%20given%20dictionary.)    
    def winner(d):
        return max(d, key = d.get)
   

# Results
with open('Analysis/results.text','w') as f:
    f.write('Election Results\n')
    f.write('--------\n')
    f.write('Total Votes: ' + str(rowcount))
    f.write(' \n')
    f.write('--------\n')
    f.write(str(candidate_results))
    f.write(' \n')
    f.write('--------')
    f.write(' \n')
    f.write('Winner: ' + str(winner(candidate_votecount)))
    f.write(' \n')
    f.write('--------')