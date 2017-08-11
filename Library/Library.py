import unittest

#Classes
from abc import ABC, abstractmethod
class AbstractStock(ABC):
    def __init__(self, id, type, title, onloan):
        self.id = id
        self.type = type
        self.name = title
        self.onloan =onloan

class Book(AbstractStock):
    def __init__(self, id, type, title, author, onloan):
        AbstractStock.__init__(self, id, type, title, onloan)
        self.id = id
        self.type = type
        self.title = title
        self.author = author
        self.onloan = onloan

class Journal(AbstractStock):
    def __init__(self, id, type, title, subject, onloan):
        AbstractStock.__init__(self, id, type, title, onloan)
        self.id = id
        self.type = type
        self.title = title
        self.subject = subject
        self.onloan = onloan

class Thesis(AbstractStock):
    def __init__(self, id, type, title, author, university, onloan):
        AbstractStock.__init__(self, id, type, title, onloan)
        self.id = id
        self.type = type
        self.title = title
        self.author= author
        self.university = university
        self.onloan = onloan

class Person(object):
    def __init__(self, id, name, relationship, address):
        self.id = id
        self.name = name
        self.relationship = relationship
        self.address = address


#Functionality


#Adding Stock

stockList = []

def addBookToStock(id, type, title, author, onloan):
    stockList.append(Book(id, type, title, author, onloan))

def addJournalToStock(id, type, title, subject, onloan):
    stockList.append(Journal( id, type, title, subject, onloan))

def addThesisToStock(id, type, title, author, university, onloan):
    stockList.append(Thesis(id, type, title, author, university, onloan))

addBookToStock("bT", "book", "Test Book", "Test Author", False)
addJournalToStock("jT", "journal", "Test Journal", "Test Subject", False)
addThesisToStock("jT", "thesis", "Test Thesis", "Test Author", "Test Uni", False)

print(stockList)


#Deleting Stock

def deleteStock(n):
   stockList.pop(n)

deleteStock(2)

print(stockList)


#Updating Stock
#Example Stock

bookT = Book("bT", "book", "Test Book", "Test Author", False)
book1 = Book("b1","book","Game of Thrones", "G.R.R.Martin", False)
book2 = Book("b2","book","The Girl with the Dragon Tatoo", "Stieg Larsson", False)
book3 = Book("b3","book","The Lord of the Rings", "J.R.R.Tolkien", False)

journalT = Journal("jT", "journal", "Test Journal", "Test Subject", False)
journal1 = Journal("j1", "journal","Climate Change", "Environmental Science", False)
journal2 = Journal("j2", "journal", "Our World","Life Science", False)
journal3 = Journal("j3", "journal", "Space, The Final Frontier","Astrophysics", False)

thesisT = Thesis("jT", "thesis", "Test Thesis", "Test Author", "Test Uni", False)
thesis1 = Thesis("t1", "thesis", "On the life of Ladybirds", "Jeremy Beatle", "Oxford", False)
thesis2 = Thesis("t2", "thesis", "The Secret World of Woodland Mammels", "Micheal J fox", "Cambridge", False)
thesis3 = Thesis("t3", "thesis", "Bizzare Rituals of Horses", "Usain Colt", "Stanford", False)

personT = Person("pT", "Test Person", "Tester", "Test Address")
person1 = Person("P1", "Tom Palmer", "Customer", "Somewhere Down under")
Person2 = Person("P2", "Esti Ramos", "Customer", "Currently in Spain")
person3 = Person("P3", "Jack Whistlecraft", "Employee", "In the Library")


#tests

class tests(unittest.TestCase):
    def test_book1(self):
        self.assertEqual("Test Book", bookT.title)
    def test_journal2(self):
        self.assertEqual("Test Subject", journalT.subject)
    def test_Thesis3(self):
        self.assertEqual("Test Uni", thesisT.university)

if __name__ == '__main__':
     unittest.main()




