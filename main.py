# Створіть клас «Місто». Збережіть у класі: назву міста,
# назву регіону, назву країни, кількість жителів у місті,
# поштовий індекс міста, телефонний код міста. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.

class City():
    def __init__(self, name, region, state, population, phone_code):
        self.name = name
        self.region = region
        self.state = state
        self.population = population
        self.phone_code = phone_code
    def info_output(self):
        print(f"City {self.name} located in region of {self.region} in {self.state}. Current population is: {self.population} and phone code is:'{self.phone_code}' ")
    def info_input(self):
        self.name = input("Input city name: ")
        self.region = input("Input region name: ")
        self.state = input("Input name of the state: ")

        self.population = input("Input number of population: ")
        self.phone_code = input("Input phone code: ")

        print(
            f"City {self.name} located in region of {self.region} in {self.state}. Current population is  {self.population} and phone code is  {self.phone_code}")



city = City("Kyiv", "North", "Ukraine", "2.5M", "+380")
city.info_output()

