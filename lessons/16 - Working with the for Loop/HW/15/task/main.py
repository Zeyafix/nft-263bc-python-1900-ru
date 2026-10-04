groups = int(input("Group count: "))
rounds = int(input("Rounds per group: "))
for group in range(1, groups + 1):
    for round_number in range(rounds, 0, -1):
        print(f"Group {group}, round {round_number}")
