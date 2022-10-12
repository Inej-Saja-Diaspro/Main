## Automated quiz marker

answers = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

responses = ["C", "B", "A"]

def check(a):
    if responses[-1] == answers[len(responses)-1]:
        correct = True
    else:
        correct = False

    if not correct:
        del responses[-1]
        print("Sorry, please try the last question again!")
    elif len(responses) < len(answers):
        print("Quiz not complete.")
        correct = str(len(responses))
        print("You've got "+ correct + " answers correct so far, please add an answer for the next question.")
    else:
        print("well done, you have completed the quiz!")

responses = ["C", "B", "C"]

print(check(a = responses))

responses = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

print(check(a = responses))