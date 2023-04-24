team_1 = ["Mia", "Lisa"]
team_2 = ["James", "Ty", "Ava"]

size_1 = len(team_1)
size_2 = len(team_2)

def game(b):
    if size_1 != size_2:
        print("Teams must have the same size!")
    else:
        print("Game on!")

print(game(b = size_1))

team_1 = ["Mia", "Lisa", "Liam"]
size_1 = len(team_1)

print(game(b = size_1))

def rounds(a):
    if size_1 != 1:
        print(f"Rounds left: {size_1}")
    else:
        print("Final round")

while size_1 != 0:
    print(rounds(a = size_1))
    lost = team_1.pop()
    size_1 = len(team_1)

## test
print("second try")

team_3 = ["Mia", "Lisa"]
team_4 = ["James", "Ty", "Ava"]

size_3 = len(team_3)
size_4 = len(team_4)

def game2(b):
    size_3 = len(team_3)
    size_4 = len(team_4)
    if size_3 != size_4:
        print("Teams must have the same size!")
    else:
        print("Game on!")

print(game2(b = size_3))

team_3 = ["Mia", "Lisa", "Liam"]

print(game2(b = size_3))

def rounds2(a):
    size_3 = len(team_3)
    if size_3 != 1:
        print(f"Rounds left: {size_3}")
    else:
        print("Final round")

while size_3 != 0:
    print(rounds2(a = size_3))
    lost = team_3.pop()