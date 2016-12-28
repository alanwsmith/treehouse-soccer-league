#!/usr/bin/env python 

import csv
import random

# Files are written to the 'output' directory.

# Worth pointing out that this script expects there to 
# be a number of both experienced and inexperienced 
# players that can be split evenly across teams. 

if __name__ == "__main__":
    
    players = []
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
                players.append({
                    'name': row['Name'],
                    'height': row['Height (inches)'],
                    'experience': row['Soccer Experience'],
                    'guardian': row['Guardian Name(s)']
                })

    def players_who_have_experience(do_they_have_it):
        return_list = []
        for player in players:
        	if player['experience'] == do_they_have_it:
        		return_list.append(player['name'])
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
            		teams_file.write('{}, '.format(player) + '\n')



    load_players()
    experienced_players = players_who_have_experience('YES') 
    inexperienced_players = players_who_have_experience('NO') 

    put_players_on_team_randomly(experienced_players)
    put_players_on_team_randomly(inexperienced_players)

    print(teams)
    output_team_file()
