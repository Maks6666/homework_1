# Створіть клас «Країна». Збережіть у класі: назву країни,
# назву континенту, кількість жителів країни, телефонний
# код країни, назву столиці, назву міст країни. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.

class State():
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def info_output(self):
        print(f"Country {self.name} located at {self.continent} with population of {self.population}. Phone code is: {self.phone_code}, capital city is {self.capital} and cities of country are: {self.cities}")
    def info_input(self):
        self.name = input("Input country name: ")
        self.continent = input("Input continent: ")
        self.population = input("Input number of population: ")
        self.phone_code = input("Input phone code: ")
        self.capital = input("Input capital city name: ")
        self.cities = input("Input some cities: ")
        print(f"Country {self.name} located at {self.continent} with population of {self.population}. Phone code is: {self.phone_code}, capital city is {self.capital} and cities of country are: {self.cities}")



state = State("Ukraine", "Europe", "40M", "+380", "Kiyv", "Kharkiv, Odessa, Lviv, Dnipro")
state.info_input()

