class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        print("Hello {},".format(self.name))

    def get_age(self):
        """This is gets the age of the object """
        return self.age

    def __str__ (self):
        return self.name, self.age


if __name__ == '__main__':

    kirwa = Person('Kirwa', 16) # p is an object of type Person
    peter = Person('Peter', 17) # m is also an object of type person

    print(type(Person)) # the type class object
    print(type(Person.get_age)) # type instancemethod

    print(type(Person)) # the type class object
    print(type(Person.get_age)) # type instancemethod
