from collections import Counter
import random
def run_dice(*diceNumbers,numOfTrials=1_000_000):
    answers={}
    for _ in range(numOfTrials):
        answer=sum([random.randint(1,side) for side in diceNumbers])  
        if answer in answers.keys(): 
            answers[answer]+=1
        else:
            answers[answer]=1
    print("\nOUTCOME\t Probability")
    for answerReturned in range(len(diceNumbers),sum(diceNumbers)+1):
        print(f"{answerReturned}\t {answers.get(answerReturned,0)*100/numOfTrials :0.2f}")
    