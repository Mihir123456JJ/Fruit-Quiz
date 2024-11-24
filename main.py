import random
class fruit_quiz:
    def __init__(self):
        self.fruits={"apple":"red",
                    "orange":"orange",
                    "pineapple":"yellow",
                    "kiwi":"green",
                    "papya":"orange"}
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer=input("Enter answer:")
            if(user_answer.lower())==color:
                print("Correct")
            else:
                print("Wrong")
            option=int(input("Enter 0 to continue and 1 to stop:"))
            if(option):
                break
print("Fruit Quiz App")
fq=fruit_quiz()
fq.quiz()                         