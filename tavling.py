import random


def main():
    Vinnare = []
    List = ["2","3","6","8","64"]
    i = 0
    while(i<4):
        luck = random.choice(List)
        if(luck in Vinnare):
            continue
        else:
            Vinnare.append(luck)
            i = i+1
    print(Vinnare)
    
main()    