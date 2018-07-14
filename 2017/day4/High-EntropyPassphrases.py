class PassphrasesReader:
    def __init__(self, name):
        self.filename = name

    def read(self):
        file = open(self.filename, 'r')
        data = []
        for line in file:
            l = line.split()
            data.append(l)

        return data


class PassphrasesChecker:
    def check(self, data):
        uncorrect = 0
        for row in data:
            sortdata = sorted(row)
            for i in range(len(sortdata) - 1):
                if sortdata[i] == sortdata[i + 1]:
                    uncorrect = uncorrect + 1
                    break
        return len(data) - uncorrect


if __name__ == "__main__":
    reader = PassphrasesReader("input.txt")
    checker = PassphrasesChecker()
    result = checker.check(reader.read())
    print(result)
