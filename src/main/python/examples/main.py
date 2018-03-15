class Person():
    def __init__(self, first_name, last_name, birth_date, sex, address):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.address = address

    def __repr__(self):
        return "{} {} {} {} {}" \
            .format(self.first_name, self.last_name, self.birth_date, self.sex, self.address)


if __name__ == '__main__':
    john = Person('Jonh', 'Doe', '21/06/1990', 'male', '216 Caledonia Street')
    print(john)