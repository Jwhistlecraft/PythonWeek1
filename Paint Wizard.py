import math
import unittest
#Paint Wizard


class PaintJob(object):
    def __init__(self,name,coverage,litres,price):
        self.name = name
        self.coverage = coverage
        self.litres = litres
        self.price = price

    def paintWizard(self,roomSize):
        value = round((((self.coverage * self.litres) / self.price) / self.price), 2)
        print("This option offers %s m*m per pound" % (value))

        tinsNeeded = math.ceil(roomSize / (self.litres * self.coverage))
        print("It would take %s tins to do the job" % (tinsNeeded))

        wastage = ((tinsNeeded * (self.litres * self.coverage)) - roomSize) / self.coverage
        print("%s ltrs would be wasted" % (wastage))

        priceForRoom = tinsNeeded * self.price
        print("It would cost: %s\n" % (priceForRoom))
        return priceForRoom


def paintComparer() :
    print("Soooo which one was the cheapest?\nwell.. it seems that,\n")
    if compareList[0] < compareList[1] and compareList[0] < compareList[2]:
        print("option 1 was the cheapest at £%s" % (compareList[0]))
    elif compareList[1] < compareList[0] and compareList[1] < compareList[2]:
        print("option 2 was the cheapest at £%s" % (compareList[1]))
    elif compareList[2] < compareList[0] and compareList[2] < compareList[1]:
        print("option 3 was the cheapest at £%s" % (compareList[2]))
    else:
        print("something major went wrong, please try again")


#paint variables
cheapoMax = PaintJob("CheapoMax", 10, 20, 19.99)
averageJoes = PaintJob("AverageJoes", 11, 15, 17.99)
duluxourousPaints = PaintJob("DuluxourousPaints", 20, 10, 25.00)

#create compare list
compareList = []
compareList.append(cheapoMax.paintWizard(165))
compareList.append(averageJoes.paintWizard(165))
compareList.append(duluxourousPaints.paintWizard(165))

#run the program
paintComparer()

class testPaintWizaed(unittest.TestCase):
    def test_cheapest_165(self):
        self.assertEqual(17.99,compareList[1])
    def test_secondCheapest_165(self):
        self.assertEqual(19.99,compareList[0])
    def test_Most_expensive(self):
        self.assertEqual(25,compareList[2])

    averageJoe = PaintJob("AverageJoes", 11, 15, 17.99)

    def test_averageJoes_name(self):
        self.assertEqual("AverageJoes", averageJoes.name)
    def test_averageJoes_Price(self):
        self.assertEqual(17.99, averageJoes.price)
    def test_averageJoes_coverage(self):
        self.assertEqual(11, averageJoes.coverage)

if __name__ == '__main__':
	unittest.main()


