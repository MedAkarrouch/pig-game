import random
def roll():
  return random.randint(1,6)

# Get nimber of players
num_players = None
while (not isinstance(num_players,int)) or num_players<2 or num_players>4:
  try:
    num_players = int(input("how many players (2-4) : "))
  except:
    print("Invalid number of players")


max_score= 30
players_scores = [0 for _ in range(num_players)];
reached_max= False

while(max(players_scores) < max_score):
  for player in range(num_players):
    if reached_max:
      break
    print(f"Player {player +1} 's trurn")
    wanna_roll = "y"
    while wanna_roll.lower() == "y":
      if reached_max:
        break
      wanna_roll = input("wanna roll (y) ? ")
      if wanna_roll.lower()!='y':
        break
      val = roll()
      if(val == 1):
        players_scores[player] = 0
        print("You got ",val) 
        print("score = ",players_scores[player])
        break
      else:
        players_scores[player]+=val
        print("You got ",val) 
        print("score = ",players_scores[player])
      if(players_scores[player]>=max_score):
        reached_max=True
      
print(f"Player {players_scores.index(max(players_scores))+1} has won 🔥🚀")