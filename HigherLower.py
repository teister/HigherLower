import random

def game():
    score=0
    cont=True

    print("welcome to HigherLower!")
    print("a random number from 1-100 will appear, and you have to guess if the next number will be higher (H) or lower (L)")
    print("(always input lowercase letters, even if it says you should input an uppercase letter)")

    num=random.randint(1,100)
    print(num)

    while cont:
        print("Higher(H)/Lower(L)?")
        HL=input("")
        if HL == "h" or HL == "l":
            num2=random.randint(1,100)
            print(num2)
            cont=False
        else:
            print("invalid input, exiting")
            cont=False
        if HL == "h" and num2 > num:
            cont=True
            num=num2
            score+=1
        if HL == "l" and num2 < num:
            cont=True
            num=num2
            score+=1
        if cont == False: 
            print("wrong :( your score was ", score,"!")
            if input("play again?(Y/N)") == "y":
                game()
            else:
                print("bye, thanks for playing!")

game()
