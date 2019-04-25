n_of_players = int(input())
scores_of_each_player = list(map(int,input().split()))
scores_of_each_player = sorted(list(set(scores_of_each_player)))
n_of_players = len(scores_of_each_player)

m_games_played_by_alice = int(input())
scores_of_alice = list(map(int,input().split()))


ranks = []
index = 0


for score1 in scores_of_alice:
	while(n_of_players > index and score1 >= scores_of_each_player[index]):
		index += 1
	ranks.append(n_of_players + 1 - index)

for i in range(m_games_played_by_alice):
	print(ranks[i])
