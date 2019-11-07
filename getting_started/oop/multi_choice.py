from user_class import User

user1 = User("user@usemail.com", "User", "Lastname", "lastUser")
user2 = User("user2@use2mail.com", "Usina", "Lastenamen", "yaya")

questions = [
    "What colour is Donald Trump?\n(a) American colour\n(b) Orange\n(c) Seven\n\nAnswer : ",
    "Do you even?\n(a) What?\n(b) WTF?\n(c) Bruh...\n\nAnswer : ",
    "What is the airspeed velocity of a laden swallow?\n(a) Seven\n(b) 12m/s\n(c) African or European?\n\nAnswer : "
]

answers = []
for ques in questions:
    ans = input(ques)
    print("")
    if ans != "a" and ans != "b" and ans != "c":
        print("That was not a choice, but okay...\n")
    else:
        answers.append(ans)

score = 0
for nr in range(0, 3):
    try:
        score += user1.mark(nr+1, answers[nr])
    except:
        print("You did not answer question "+str(nr)+" properly!")

print(score)
