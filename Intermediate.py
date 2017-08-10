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
        print("the year %d is a leap year" %(year))
    else:
        print("the year %d is not a leap year" %(year))

leapCheck(400)
leapCheck(1200)
leapCheck(1999)
leapCheck(2020)

#Paint Wizard

def paintWizard(coverage,litres,price,roomSize):

    value = round((((coverage*litres)/price)/price),2)
    print("This option offers %s m*m per pound" %(value))

    tinsNeeded = roomSize/(litres*coverage)
    print("It would take %d tins to do the job" %(tinsNeeded))

    wastage = (tinsNeeded*coverage) - roomSize
    print("%d ltrs would be wasted" %(wastage))

    priceForRoom = tinsNeeded*price
    print("it would cost: %d" %(priceForRoom))


paintWizard(10,20,19.99,500) #CheapoMax
paintWizard(11,15,17.99,500) #AverageJoes
paintWizard(20,10,25.00,500) #DuluxourousPaints


