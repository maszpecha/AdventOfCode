class SpreadSheetReader:
    def __init__(self, name):
        self.filename = name

    def read(self):
        file = open(self.filename, 'r')
        data = []
        for line in file:
            l = [int(s) for s in line.split() if s.isdigit()]
            data.append(l)

        return data


class SpreadSheetCalculator:
    def calculate(self, data):
        result = 0
        for row in data:
            minvalue = min(row)
            maxvalue = max(row)

            diff = maxvalue - minvalue
            result = result + diff

        return result


if __name__ == "__main__":
    reader = SpreadSheetReader("input.txt")
    data = reader.read()
    calculator = SpreadSheetCalculator()
    res = calculator.calculate(data)
    print(res)
