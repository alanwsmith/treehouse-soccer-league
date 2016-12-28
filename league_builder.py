#!/usr/bin/env python 

import csv
import random

# Files are written to the 'output' directory.

# Worth pointing out that this script expects there to 
# be a number of both experienced and inexperienced 
# players that can be split evenly across teams. 

# This script also relies on the fact that there are 18
# players in the input file and that there are three 
# teams. Because that works out to 6 players per team,
# no additional calculation is done to keep the 
# same number of players on each team.

# Also, this currently stores players in a player_dict
# with names for keys. If a new list with two players 
# who have the same name is used, one of them will 
# get overwritten. Because this script is written
# specifically for the test file I'm leaving it
# like that.

if __name__ == "__main__":
    
    player_dict = {}
    teams = {
    	'Sharks': { 
    		'players': [] 
    	}, 
    	'Dragons': {
    		'players': [] 
    	}, 
    	'Raptors': {
    		'players': [] 
    	} 
    }

    def load_players(): 
        with open('soccer_players.csv', 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)
            for row in csv_data:
                player_dict[row['Name']] = {
                    'height': row['Height (inches)'],
                    'experience': row['Soccer Experience'],
                    'guardian': row['Guardian Name(s)']
                }

    def players_who_have_experience(do_they_have_it):
        return_list = []
        for player_name, player_data in player_dict.items():
        	if player_data['experience'] == do_they_have_it:
        		return_list.append(player_name)
        return return_list 

    def put_players_on_team_randomly(player_list):
        while len(player_list):
        	for team_key, team_data in teams.items():
        		if len(player_list):
        		    team_data['players'].append(player_list.pop(random.randint(0,len(player_list) - 1))) 

    def output_team_file():
        with open('output/teams.txt', 'w') as teams_file:
            for team_key, team_data in teams.items():
                teams_file.write(team_key + '\n')
            	for player in team_data['players']:
            		teams_file.write('{}, {}'.format(player, player_dict[player]['experience']) + '\n')

    load_players()
    put_players_on_team_randomly(players_who_have_experience('YES'))
    put_players_on_team_randomly(players_who_have_experience('NO'))
    output_team_file()

