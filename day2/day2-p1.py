strat_guide = open("./input.txt", "r").read().split("\n")

results = {
        "DRAW": 3,
        "WIN": 6
}

my_choices = {
        "X": 1,
        "Y": 2,
        "Z": 3
}

total_score = 0

for rps_round in strat_guide:

    if rps_round == '':
        continue

    rps_round = rps_round.split(" ")

    opp_choice = rps_round[0]
    my_choice = rps_round[1]

    total_score += my_choices[my_choice]

    if opp_choice == 'A':
        if my_choice == 'X':
            total_score += results["DRAW"]
            continue

        if my_choice == 'Y':
            total_score += results["WIN"]
            continue

    if opp_choice == 'B':
        if my_choice == 'Y':
            total_score += results["DRAW"]
            continue

        if my_choice == 'Z':
            total_score += results["WIN"]
            continue
    
    if opp_choice == 'C':
        if my_choice == 'Z':
            total_score += results["DRAW"]
            continue

        if my_choice == 'X':
            total_score += results["WIN"]
            continue

print(total_score)
