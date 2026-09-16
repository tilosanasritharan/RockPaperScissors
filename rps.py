import random

u_wins = 0
cmp_wins = 0

ops = ["r", "p", "s"]

while True:
    user_input = input("Type Rock(R)/Paper(P)/Scissors(S) or Q to quit: ").strip().lower()
    if user_input == 'q':
        break
    if user_input not in ops:
        print("Invalid choice, please try again.")
        continue

    cmp_pick = random.choice(ops)

    print("Computer picked "+ cmp_pick +".")

    if user_input == cmp_pick:
        print("It's a tie")
    elif (user_input == "r" and cmp_pick == "s") or (user_input == "s" and cmp_pick == "p") or \
            ( user_input == "p" and cmp_pick == "r"):
        print("You won!")
        u_wins+=1
    else:
        print("You lost!")
        cmp_wins +=1

print("You won "+str(u_wins)+" times.")
print("Computer won "+str(cmp_wins)+" times.")

print("Goodbye!")