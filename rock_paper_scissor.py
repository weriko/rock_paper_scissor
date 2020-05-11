import random
lista = ["paper","rock","scissor"]

player1= random.choice(lista)

player3= random.choice(lista)
class Player:
    def __init__(self, playerno=None):
        self.wins = []
        self.playerno=playerno
        self.choice = "paper"
def vs(player1, player2):
    print(player1.choice)
    print(player2.choice)
    if player1.choice == "paper" and player2.choice =="rock":
        player1.wins.append("win")
        player2.wins.append("lose")
    elif player1.choice == "rock" and player2.choice== "scissors":
        player1.wins.append("win")
        player2.wins.append("lose")
    elif player1.choice =="scissors" and player2.choice == "paper":
        player1.wins.append("win")
        player2.wins.append("lose")
    elif player1.choice==player2.choice:
        player1.wins.append("draw")
        player2.wins.append("draw")
    else:
        player2.wins.append("win")
        player1.wins.append("lose")

def game(players):
    pos = ["rock","paper","scissors"]
    for i in range(len(players)-1):
        
        players[i].choice = random.choice(pos)
        players[i+1].choice = random.choice(pos)
        vs(players[i],players[i+1])
        print(players[0].wins)
    for player in players:
        if "lose" in player.wins:
            players.remove(player)
    if len(players) ==1:
        print("wins > ",players[0].playerno)
    else:
        game(players)
        
game([Player(playerno = 1),Player(playerno =2),Player(playerno=3),Player(playerno=4)])
