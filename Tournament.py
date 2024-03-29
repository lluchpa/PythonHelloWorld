
from player import Player
from match import Match
import csv
import os.path

class Tournament:

    matches = []

    """
        Given a filename of players resource, read data from it and create the tournament.
    """
    def createTournament(self, fileName):
        
        players = []


        print("Loading players from ", fileName, "\n")

        try:
            with open(fileName) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                idPlayer = 0
                for split in csv_reader:
                    player = Player()

                    player.ID(idPlayer)
                    player.setName(split[0])
                    player.setSurname(split[1])
                    player.setCategory(split[2])

                    players.append(player)

                    idPlayer += 1

            print("All players loaded.")

            print("ID | Name | Surnames | Category")
            for player in players:
                print(player.id, " ", 
                    player.name, " ", 
                    player.surname, " ", 
                    player.category)

            print("Creating tournament's matches")

            matches = self.createMatches(players)

            print("Tournament created!!")

            self.matches = matches
        except:
            print("An error ocurred loading players from resource ", fileName)

    """
        Given a list of players, creates the matches. Every player will play
        one time with the rest of players of the group.
    """
    def createMatches(self, players):

        matches_local = []

        for player in players:

            for _player in players:

                #create match
                if player.id < _player.id:
                    match = Match()

                    match.id1 = player.id
                    match.id2 = _player.id
                    match.category = player.category
                    match.sport = "tenis"
                    match.mod = "I"

                    matches_local.append(match)

        return matches_local
                
