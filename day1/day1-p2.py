input = open("./input.txt", "r")

calories_by_elf = input.read().split("\n\n")
total_calories_by_elf = []

for elf in calories_by_elf:
    total_calories = 0
    calories = elf.split("\n")

    for calorie in calories:
        if calorie == '':
            continue
        total_calories += int(calorie)

    total_calories_by_elf.append(total_calories)


total_calories_by_elf.sort(reverse = True)
total_calories_by_top_3_elves = 0
for calorie in total_calories_by_elf[0:3]:
    total_calories_by_top_3_elves += calorie

print(total_calories_by_top_3_elves)
