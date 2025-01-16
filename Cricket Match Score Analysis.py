import pandas as pd  

# Data for players' performance in the match (Runs, Wickets, Balls faced, Balls bowled)
data = {
    "Player": ['Rohit Sharma', 'KL Rahul', 'Virat Kohli', 'Suryakumar Yadav', 'Hardik Pandya', 
               'MS Dhoni', 'Ravindra Jadeja', 'Bhuvneshwar Kumar', 
               'Jasprit Bumrah', 'Yuzvendra Chahal', 'Mohammed Shami'],
    "Runs": [45, 62, 38, 75, 25, 50, 15, 10, 0, 5, 0],  # Runs scored by each player
    "Wickets": [0, 0, 0, 0, 1, 0, 2, 3, 1, 2, 4],  # Wickets taken by each player
    "Balls_Faced": [30, 50, 42, 55, 20, 45, 12, 8, 2, 4, 1],  # Balls faced by each player
    "Balls_Bowled": [0, 0, 0, 0, 4, 0, 10, 10, 10, 10, 10],  # Balls bowled by each player
}

# Convert the dictionary into a pandas DataFrame
match_data = pd.DataFrame(data)

# Calculate total runs scored by all players
total_runs = match_data["Runs"].sum()
print("Total Runs:", total_runs)

# Batting Average Calculation: This formula divides runs by the difference between balls faced and runs.
# This method is directly used here without any handling for invalid results (e.g., division by zero)
match_data['Batting Average'] = match_data['Runs'] / (match_data['Balls_Faced'] - match_data['Runs'])

# Display the dataset along with calculated batting averages for each player
print("\nBatting Average:\n", match_data[['Player', 'Batting Average']])

# Filter the players who have bowled at least one ball
bowlers = match_data[match_data['Balls_Bowled'] > 0]

# Bowling Strike Rate Calculation: Divides balls bowled by wickets taken. 
# This indicates how many balls a bowler takes to get one wicket.
bowlers['Bowling Strike Rate'] = bowlers['Balls_Bowled'] / bowlers['Wickets']

# Display the bowling strike rate of players who have bowled
print("\nBowling Strike Rate:\n", bowlers[['Player','Bowling Strike Rate']])

# Identify the top run scorer by finding the player with the maximum runs
top_scorer = match_data.loc[match_data['Runs'].idxmax(),'Player']
print("\nTop Run Scorer:", top_scorer)

# Identify the top wicket-taker by finding the player with the maximum wickets among the bowlers
top_wicket_taker = bowlers.loc[bowlers['Wickets'].idxmax(),'Player']
print("\nTop Wicket-Taker:", top_wicket_taker)

# Points Calculation for players:
# Points are calculated as: 
# - 1 point for every 10 runs scored 
# - 20 points for every wicket taken
match_data['Points'] = (match_data['Runs'] // 10) + (match_data['Wickets'] * 20)

# Display the dataset with player points
print("\nPlayer Points:\n", match_data[['Player','Points']])
