import math


class FuelRequirementsReader:
    def __init__(self, name):
        self.filename = name

    def read(self):
        file = open(self.filename, 'r')
        data = [int(line) for line in file]
        return data


class FuelRequirementsCalculator:
    def calculate_total_fuel_requirement(self, data):
        result = 0
        for row in data:
            result += self.get_required_fuel(row)
        return result

    def calculate_complex_total_fuel_requirement(self, data):
        result = 0
        for row in data:
            result += self.get_complex_required_fuel(row)
        return result

    def get_complex_required_fuel(self, row):
        fuel = self.get_required_fuel(row)
        if fuel <= 0:
            return 0
        else:
            return fuel + self.get_complex_required_fuel(fuel)

    @staticmethod
    def get_required_fuel(row):
        return round_down(row / 3) - 2


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


if __name__ == "__main__":
    reader = FuelRequirementsReader("input.txt")
    data = reader.read()
    calculator = FuelRequirementsCalculator()

    result1 = calculator.calculate_total_fuel_requirement(data)
    print(result1)
    
    result2 = calculator.calculate_complex_total_fuel_requirement(data)
    print(result2)
