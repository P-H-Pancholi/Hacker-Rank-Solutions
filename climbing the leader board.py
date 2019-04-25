<<<<<<< HEAD
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
=======
n_all_scores = int(raw_input())
all_scores = raw_input()
all_scores = map(int,all_scores.split())
n_alice_scores = int(raw_input())
alice_scores = raw_input()
alice_scores = map(int,alice_scores.split())


set_all_scores = set(all_scores)


for score in alice_scores:
    alice_rank = 0
    position = 0
    for leader_board_score in set_all_scores:
        if score < leader_board_score:
            position +=1
        elif score == leader_board_score:
            alice_rank = position
    alice_rank = position
    print(alice_rank + 1)
>>>>>>> b6b99a9ada68b527e54dce8a7170e53754a264ac
