#!/usr/bin/env python 

import csv


if __name__ == "__main__":
    
    players = []

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
        count = 0
        for player in players:
        	if player['experience'] == 'YES':
        		count += 1
        return count


    load_players()
    print(players_with_experience())
    print(players)

