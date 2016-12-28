Treehouse Soccer League
=======================

My run through the Treehouse Soccer League project in Python. 

Notes
-----

The `teams.txt` file is written in the `output` directory. The extra credit individual player letters are output to the `letters` directory. These directories are in the GitHub repo. The script currently doesn't try to make those directories (since we haven't gotten to that yet). If the repo is cloned, there shouldn't be a problem. If the 

Theres an empty line between each of the teams. The instructions didn't specify this one way or the other. It looks better with it, so I went that way.

Worth pointing out that this script expects there to be a number of both experienced and inexperienced players that can be split evenly across teams. 

This script also relies on the fact that there are 18 players in the input file and that there are three teams. Because that works out to 6 players per team, no additional calculation is done to keep the same number of players on each team.

Also, this currently stores players in a player_dict with names for keys. If a new list with two players who have the same name is used, one of them will get overwritten. Because this script is written specifically for the test file I'm leaving it like that.

For the Extra Credit, I can't remember if the course covered how to replace spaces with underscores. I used the `.replace()` for that. Another possible way would have been to split on spaces and then join back with underscores, but I'm don't remember that being covered either. 

I didn't add a lot of comments to the code. Instead, I tried to make it obvious what the code was doing.


