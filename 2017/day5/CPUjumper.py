class CPUreader:
    def __init__(self, name):
        self.filename = name

    def read(self):
        file = open(self.filename, 'r')
        data = []
        for line in file:
            data.append(int(line))
        return data


class CPUjumper:
    def jump(self, data):
        i = 0
        steps = 0
        while 0 <= i < len(data):
            old = data[i]
            data[i] = data[i] + 1
            i = i + old
            steps = steps + 1
        return steps


if __name__ == "__main__":
    reader = CPUreader("input.txt")
    data = reader.read()
    jumper = CPUjumper()
    result = jumper.jump(data)
    print(result)
