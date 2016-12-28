#!/usr/bin/env python 

import csv


if __name__ == "__main__":
    
    players = []
    TEAMS = ['Sharks', 'Dragons', 'Raptors']

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

    def players_with_experience():
        return_list = []
        for player in players:
        	if player['experience'] == 'YES':
        		return_list.append(player['name'])
        return return_list 


    load_players()
    print(players_with_experience())
    print(players)

