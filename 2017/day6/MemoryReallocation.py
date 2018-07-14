class MemoryReader:
    def __init__(self, name):
        self.filename = name

    def read(self):
        file = open(self.filename, 'r')
        for line in file:
            return [int(s) for s in line.split() if s.isdigit()]


class MemoryReallocator:
    def getMax(self, data):
        m = max(data)
        return [i for i, j in enumerate(data) if j == m][0], m

    def reallocate(self, data):
        steps = 1
        configurations = [data.copy()]
        while True:
            index, maxvalue = self.getMax(configurations[len(configurations) - 1])
            data[index] = 0
            while maxvalue > 0:
                index = index + 1
                if index >= len(data):
                    index = 0
                data[index] = data[index] + 1
                maxvalue = maxvalue - 1
            if self.areDuplicated(configurations, data):
                return steps
            else:
                configurations.append(data.copy())
                steps = steps + 1

    def areDuplicated(self, data, part):
        for row in data:
            if row == part:
                return True
        return False


if __name__ == "__main__":
    reader = MemoryReader("input.txt")
    data = reader.read()
    reallocator = MemoryReallocator()
    result = reallocator.reallocate(data)
    print(result)
