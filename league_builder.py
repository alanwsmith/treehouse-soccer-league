#!/usr/bin/env python 

import csv


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


    load_players()
    experienced_players = players_who_have_experience('YES') 
    inexperienced_players = players_who_have_experience('NO') 

    print(experienced_players)
    print(inexperienced_players)
