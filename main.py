import os
import csv

#Set path for files
election_csv = os.path.join("..", "Resources", "election_data.csv")
output = os.path.join("..", "Pypoll", "elections.txt")

#Variables
total_votes = 0
count_candidates = []
candidate_a = 0
candidate_b = 0
candidate_c = 0
single_candidates = []

with open(election_csv) as csvfile:
    election_vote = csv.reader(csvfile, delimiter=',')
    header = next(election_vote)
    
    for row in election_vote:
        column_data = row[2]
        total_votes +=1

        #Now find the single candidates 
        if column_data not in single_candidates:
            single_candidates.append(column_data)

        #Porcentage for each candidate (won votes)
        if column_data == single_candidates[0]:
            candidate_a +=1

        elif column_data == single_candidates[1]:
            candidate_b +=1
        
        elif column_data == single_candidates[2]:
            candidate_c +=1

        # Finding the winner truogh graders
        if candidate_a > candidate_b and candidate_c:
            winner = single_candidates[0]
        
        elif candidate_b > candidate_a and candidate_c:
            winner = single_candidates[1]

        elif candidate_c > candidate_a and candidate_b:
            winner = single_candidates[2]
        
#Finding porcentage for each candidate
percentage_candidate_a = (candidate_a / total_votes) * 100
percentage_candidate_b = (candidate_b / total_votes) * 100
percentage_candidate_c = (candidate_c / total_votes) * 100



text=f"""
Election Results
----------------------------

Total Votes: {total_votes}

----------------------------

{single_candidates[0]}: {percentage_candidate_a:.3f}% ({candidate_a})
{single_candidates[1]}: {percentage_candidate_b:.3f}% ({candidate_b})
{single_candidates[2]}: {percentage_candidate_c:.3f}% ({candidate_c})

----------------------------

Winner: {winner}

----------------------------

"""
print(text)

# Write results to the output file
with open(output , 'w') as file:
    file.write(text)