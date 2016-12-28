#!/usr/bin/env python 

import csv
import random

# Checkout the README.md file for some other notes.

if __name__ == "__main__":

    # Dictionary to hold players loaded from the JSON file
    players = {}

    # The three teams with lists that will hold the
    # players assigned to each.
    teams = {
        'Sharks': { 'players': [] }, 
        'Dragons': { 'players': [] }, 
        'Raptors': { 'players': [] } 
    }

    def load_players(): 
        with open('soccer_players.csv', 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)
            for row in csv_data:
            	# Make the name of each player the main key
                # and assign the rest of the data cleaner names. 
                players[row['Name']] = {
                    'height': row['Height (inches)'],
                    'experience': row['Soccer Experience'],
                    'guardian': row['Guardian Name(s)']
                }

    def players_who_have_experience(do_they_have_it):
        return_list = []
        for player_name, player_data in players.items():
            if player_data['experience'] == do_they_have_it:
                return_list.append(player_name)
        return return_list 

    def put_players_on_team_randomly(player_list):
        while len(player_list):
            for team_key, team_data in teams.items():
                if len(player_list):
                    team_data['players'].append(player_list.pop(random.randint(0,len(player_list) - 1))) 

    def output_team_file():
        with open('teams.txt', 'w') as teams_file:
            for team_key, team_data in teams.items():
                teams_file.write(team_key + '\n')
                for player in team_data['players']:
                    teams_file.write('{}, {}, {}'.format(player, players[player]['experience'], players[player]['guardian']) + '\n')
                teams_file.write('\n')

    def output_welcome_letters():
        for team_name, team_data in teams.items():
        	for player_name in team_data['players']:
        		file_name = player_name.lower().replace(' ', '_') + '.txt'
        		with open(file_name, 'w') as letter:
        		    letter.write('Dear {},\n\n'.format(players[player_name]['guardian']))
        		    letter.write('Welcome to the new season!\n\n')
        		    letter.write('This letter provides soccer seasons details for your player:\n\n    {}\n\n'.format(player_name))
        		    letter.write('This season, they will play for:\n\n    The {}\n\n'.format(team_name))
        		    letter.write('The first practice is:\n\n    4:45pm on Jan. 10 at Community Field 7\n\n'.format(team_name))
        		    letter.write('Looking forward to seeing you then!\n\n')
        		    letter.write('-- Alan "The Commish" Smith\n')
        		    
    load_players()
    put_players_on_team_randomly(players_who_have_experience('YES'))
    put_players_on_team_randomly(players_who_have_experience('NO'))
    output_team_file()
    output_welcome_letters()

