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
