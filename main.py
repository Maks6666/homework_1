# Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
# дату народження, контактний телефон, місто, країну,
# домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Person():
    def __init__(self, name, birth, phone, city, state, adress):
        self.name = name
        self.birth = birth
        self.phone = phone

        self.city = city
        self.state = state
        self.adress = adress
    def info_output(self):
        print(f"Person {self.name} was born in {self.birth} has phone number: {self.phone}. Currently lives in {self.city} in {self.state} with following adress: {self.adress} ")
    def info_input(self):
        self.name = input("Input name: ")
        self.birth = input("Input birth date: ")
        self.phone = input("Input phone number: ")

        self.city = input("Input home city: ")
        self.state = input("Input home state: ")
        self.adress = input("Input home adress: ")

        print(f"Person {self.name} was born in {self.birth} has phone number: {self.phone}. Currently lives in {self.city} in {self.state} with following adress: {self.adress} ")



person = Person("A", "20.02.2002", "0392092", "London", "UK", "Greenroad-2" )
person.info_input()

