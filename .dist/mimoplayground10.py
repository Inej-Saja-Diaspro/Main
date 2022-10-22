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
