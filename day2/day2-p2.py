strat_guide = open("./input.txt", "r").read().split("\n")

results = {
        "DRAW": 3,
        "WIN": 6,
        "LOSE": 0,
}

opp_choices = {
        "ROCK": "A",
        "PAPER": "B",
        "SCISSORS": "C",
}

my_choices = {
        "ROCK": 1,
        "PAPER": 2,
        "SCISSORS": 3,
}

what_i_should_choose = {
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN",
}

total_score = 0

for rps_round in strat_guide:

    if rps_round == '':
        continue

    rps_round = rps_round.split(" ")


    desired_outcome = rps_round[1]
    total_score += results[what_i_should_choose[desired_outcome]]
    
    opp_choice = rps_round[0]

    if opp_choice == opp_choices["ROCK"]:
        if what_i_should_choose[desired_outcome] == "LOSE":
            total_score += my_choices["SCISSORS"]
            continue
        if what_i_should_choose[desired_outcome] == "WIN":
            total_score += my_choices["PAPER"]
            continue
        if what_i_should_choose[desired_outcome] == "DRAW":
            total_score += my_choices["ROCK"]
            continue

    if opp_choice == opp_choices["PAPER"]:
        if what_i_should_choose[desired_outcome] == "LOSE":
            total_score += my_choices["ROCK"]
            continue
        if what_i_should_choose[desired_outcome] == "WIN":
            total_score += my_choices["SCISSORS"]
            continue
        if what_i_should_choose[desired_outcome] == "DRAW":
            total_score += my_choices["PAPER"]
            continue

    if opp_choice == opp_choices["SCISSORS"]:
        if what_i_should_choose[desired_outcome] == "LOSE":
            total_score += my_choices["PAPER"]
            continue
        if what_i_should_choose[desired_outcome] == "WIN":
            total_score += my_choices["ROCK"]
            continue
        if what_i_should_choose[desired_outcome] == "DRAW":
            total_score += my_choices["SCISSORS"]
            continue

print(total_score)
