import random
while True:
    c_input = ["Rock","Paper","Scissor"]
    user_input = input("Please choose an option :").capitalize()
    if user_input in c_input:
        pass
    else:
        print("You have choose a wrong option")
        continue
    c = random.choice(c_input)
    print(f"You choose : {user_input}")
    print(f"Computer choose : {c} \n")

    if user_input == "Rock" and c == "Paper":
        print("Computer wins \n")
    elif user_input == "Rock" and c == "Rock":
        print("Draw \n")
    elif user_input == "Rock" and c == "Scissor":
        print("You wins \n")
    elif user_input == "Paper" and c == "Paper":
        print("Draw \n")
    elif user_input == "Paper" and c == "Rock":
        print("You wins \n")
    elif user_input == "Paper" and c == "Scissor":
        print("Computer wins \n")
    elif user_input == "Scissor" and c == "Paper":
        print("You wins \n")
    elif user_input == "Scissor" and c == "Rock":
        print("Computer wins \n")
    elif user_input == "Scissor" and c == "Scissor":
        print("Draw \n")

    repeat = input("Do you want to continue the game ? (Y/N):").capitalize()

    if "Y" in repeat:
        continue
    else:
        break
