#!/usr/bin/env python 

import csv
import random

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


    load_players()
    experienced_players = players_who_have_experience('YES') 
    inexperienced_players = players_who_have_experience('NO') 

    put_players_on_team_randomly(experienced_players)
    put_players_on_team_randomly(inexperienced_players)

    print(teams)
