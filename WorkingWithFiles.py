class Person():
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

person1 = Person("Dan", "Bee enthusiast", 23)
person2 = Person("Jack", "Wasp entertainer", 30)
person3 = Person("Elliott", "Pokeman", 25)
person4 = Person("Adam", "Darksouls collector", 26)
person5 = Person("Tadas", "Being tactical", 27)

listOfPeeps = [person1,person2,person3,person4,person5]

def personFile():
    file = open("myPeeps", "w")
    for i in listOfPeeps:
        file.write(i.name + "," + i.occupation + "," + str(i.age) + ";")
    file.close()

def copyPerson():
    file = open("myPeeps","r")
    readList = str(file.read())
    file.close()
    listSplit = readList.split(";")
    newPeepsList = list(listSplit)
    print(newPeepsList)

copyPerson()




