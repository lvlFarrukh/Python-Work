import random
moves = ["se","st","h"]
computer_point = 0
player_point = 0
def convt(strinp):
    if strinp == "se":
        return "sessor"
    elif strinp == "st":
        return "stone"
    elif strinp == "h":
        return "handkerchief"
    else:
        print("invalid input")

while True:
    if computer_point == 5 or player_point == 5:
        break
    u_i = input("Enter [Se: Sessor | St: Stone | H: Handkerchief]: ").lower()
    c_i = random.choice(moves)

        # Check round decision
    if u_i == "se" or u_i == "st" or u_i == "h":
        if u_i == c_i:
            print("Draw!")
        elif u_i == "se" and c_i == "h" or u_i == "h" and c_i == "st" or u_i == "st" and c_i == "se":
            user_input = convt(u_i)
            comp_input = convt(c_i)
            print(f"\"User\" {user_input} : {comp_input} \"Computer\"")
            player_point += 1
            print(f"+Point for Player\nUser point: {player_point}\nComputer Point: {computer_point}\n\n")
        else:
            user_input = convt(u_i)
            comp_input = convt(c_i)
            print(f"\"User\" {user_input} : {comp_input} \"Computer\"")
            computer_point += 1
            print(f"+Point for Computer\nUser point: {player_point}\nComputer Point: {computer_point}\n\n")
    else:
        print("Invalid input!")
if computer_point > player_point:
    print(f"Game Over you lost!")
else:
    print("Congratulation you Win!")