input = open("./input.txt", "r")

calories_by_elf = input.read().split("\n\n")

index_elf_with_most_calories = 1
elf_with_most_calories = (index_elf_with_most_calories - 1, 0)

for elf in calories_by_elf:
    total_calories = 0
    calories = elf.split("\n")

    for calorie in calories:
        if calorie == '':
            continue
        total_calories += int(calorie)

    if total_calories > elf_with_most_calories[1]:
        elf_with_most_calories = (index_elf_with_most_calories, total_calories)

    index_elf_with_most_calories += 1  

print(elf_with_most_calories[1])
