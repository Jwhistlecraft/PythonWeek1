class Stock(object):
    def __init__(self, id, type, title, onloan):
        self.id = id
        self.type = type
        self.name = title
        self.onloan =onloan


class Books(Stock):
    def __init__(self,id, type, title, author, onloan):
        self.id = id
        self.type = type
        self.name = title
        self.author = author
        self.onloan = onloan

class Journals(Stock):
    def __init__(self, id, type, title, subject, onloan):
        self.id = id
        self.type = type
        self.name = title
        self.subject = subject
        self.onloan = onloan

class Theses(Stock):
    def __init__(self, id, type, title, author, university, onloan):
        self.id = id
        self.type = type
        self.name = title
        self.author= author
        self.university = university
        self.onloan = onloan

class Person(object):
    def __init__(self, id, name, relationship, address):
        self.id = id
        self.name = name
        self.relationship = relationship
        self.adress = address

