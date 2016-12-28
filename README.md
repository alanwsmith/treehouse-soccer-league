Treehouse Soccer League
=======================

My run through the Treehouse Soccer League project in Python. 

Notes
-----

Files are written to the 'output' directory.

Theres an empty line between each of the teams. The instructions didn't specify this one way or the other. It looks better with it, so I went that way.

Worth pointing out that this script expects there to be a number of both experienced and inexperienced players that can be split evenly across teams. 

This script also relies on the fact that there are 18 players in the input file and that there are three teams. Because that works out to 6 players per team, no additional calculation is done to keep the same number of players on each team.

Also, this currently stores players in a player_dict with names for keys. If a new list with two players who have the same name is used, one of them will get overwritten. Because this script is written specifically for the test file I'm leaving it like that.
