import random
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice
    return card 
def cal_score(cards):
    if sum(cards)==21 & len(cards)==21:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(u_score,c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "lose"
    elif u_score == 0:
        return "win"
    elif u_score > 21:
        return "lose"
    elif c_score >21:
        return "win"
    elif  c_score<u_score:
        return"win"
    else:
        return"lose"
    
def play_game():
    user_cards=[]
    comp_cards=[]
    comp_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not is_game_over:
        user_score=cal_score(user_cards)
        comp_score=cal_score(comp_cards)
        print(f"ur cards:{user_cards} ur score:{user_score}")
        print(f"computer first card:{comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score >21:
            is_game_over=True
        else:
            user_should_deal=input("do you want to continue type:'y',else type: 'n'")
            if user_should_deal=='y':
               user_cards.append(deal_cards())

            else:
               is_game_over=True


        while comp_score !=0 or comp_score < 17:
          comp_cards.append(deal_cards())
          comp_score=cal_score(comp_cards)


    print(f"your final:{user_cards},ur final score:{user_score}")
    print(f"computer cards :{comp_score},final score:{comp_score}")
    print(compare(user_score,comp_score))

while input("do you want to continue to play type 'y' or 'n'") == "y":
    print("/n"*20)
    play_game()




    
