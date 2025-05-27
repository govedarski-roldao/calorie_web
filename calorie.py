from temperature import Temperature


class Calorie:
    """Represent amount of calories calculated with
    BMR = 10 * weight + 6.25*height - 5 * age + 5 - 10 * temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.height = height
        self.weight = weight
        self.age = age

    def calculate(self):
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * float(self.temperature)
        return bmr


if __name__ == "__main__":
    temperature = Temperature("Bulgaria", "Sofia").get()
    calories = Calorie(92, 180, 35,temperature)
    print(calories.calculate())
