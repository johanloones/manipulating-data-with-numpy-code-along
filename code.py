# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.

# This exercise will help you deal with other file formats and how toa read it.
data_ipl=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=str)
data_ipl

# Number of unique matches 
len(set(data_ipl[:,0]))

# How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.

# Number of unique teams
team1=set(data_ipl[:,3])
team2=set(data_ipl[:,4])
team1.union(team2)

# this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras
extras=data_ipl[:,17]
extras_int=extras.astype(np.int16)
print(sum(extras_int))

# An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out
batsman='SR Tendulkar'
player_out_mask=data_ipl[:,20] == batsman
wickets_arr=data_ipl[player_out_mask]
wickets_arr[:,11]
wickets_arr[:,21]

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.

# Number of times Mumbai Indians won the toss

toss_winner='Mumbai Indians'
toss_winner_mask=data_ipl[:,5]== toss_winner
print(np.unique(data_ipl[:,0][toss_winner_mask]))
np.unique(data_ipl[:,0][toss_winner_mask]).size

# this exercise will help you get the statistics on one particular team
team='Mumbai Indians'
team_mask= np.logical_or(data_ipl[:,3]==team,data_ipl[:,4]==team)
total_matches=np.unique(data_ipl[:,0][team_mask]).size
print(total_matches)

# Filter record where batsman scored six and player with most number of sixex
scored_six='6'
player_scored_six=data_ipl[:,16]==scored_six
print(player_scored_six)
from collections import Counter
print(data_ipl[:,13][player_scored_six])
player_most_six_dict=Counter(data_ipl[:,13][player_scored_six])
print(player_most_six_dict)
player_most_six=[key for key, value in player_most_six_dict.items() if value == max(player_most_six_dict.values())]
print(player_most_six)

# An exercise to know who is the most aggresive player or maybe the scoring player






