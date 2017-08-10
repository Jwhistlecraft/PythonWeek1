#black jack

def hands(hand1,hand2):

    difference = hand1 - hand2

    if hand1 > 21 and hand2 > 21:
        print("both players are bust with a hands of %d and %d" %(hand1,hand2))
    elif hand1 > 21 and hand2 <= 21:
        print("player1 is bust with %d" %(hand1))
    elif hand2 > 21 and hand1 <= 21:
        print("player2 is bust with %d" %(hand2))
    elif hand1 <= 21 and difference  < 0:
        print("player2 wins with %d" %(hand2))
    elif hand2 <= 21 and difference > 0:
        print("player1 wins with %d" %(hand1))
    elif hand1 == hand2:
        print("Its a draw with a hands of %d and %d" %(hand1,hand2))

hands(18,21)
hands(20,18)
hands(22,23)
hands(22,19)
hands(19,22)


#too hot

def hotInput(temp,isSummer):
    if temp >= 60 or temp == 100 and isSummer == True:
        return True
    elif temp >= 60 or temp == 100 and isSummer == False:
        return False
    elif temp <= 90 and temp >= 60:
        return True
    elif temp < 60 :
        return False

print(hotInput(80, False))
print(hotInput(100, False))
print(hotInput(100, True))
print(hotInput(50, True))


#leapyeah check

def leapCheck(year):
    if year%4 ==0:
        print("the year %d is a leap year\n" %(year))
    else:
        print("the year %d is not a leap year\n" %(year))

leapCheck(400)
leapCheck(1200)
leapCheck(1999)
leapCheck(2020)


