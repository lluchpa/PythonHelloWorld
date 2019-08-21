print("Welcome to my first code in Python")

from player import Player
from match import Match
from Tournament import Tournament
import csv
import os.path


#read data from file
fileName = str(input("Input file name of resource players"))

if not os.path.isfile(fileName):
    print("Please, create the file players.csv and writte formatted data!!")
    quit()

#players list
players = []
tournament = Tournament()

matches = tournament.createTournament(fileName, players)

for match in matches:
    print(match.id1, " ", match.id2, " ", match.category, " ", match.mod, " ", match.sport)

print("This seems to be a good first code.")

