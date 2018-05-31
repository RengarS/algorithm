class Person:

    def __init__(self):
        self.name = ""

    total = 10

    def setName(self, name):
        self.name = name
        print(self.name)


if __name__ == '__main__':
    person = Person()
    person.setName("A")
    l = list()
    l.append("a")
    l.append("b")
    l.append("C")
    for e in l:
        print(e)
    print(person.total)
    person.total += 1
    print(person.total)
