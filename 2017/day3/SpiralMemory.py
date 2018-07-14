from math import sqrt
from math import inf


class SpiralMemory:
    def getCentres(self, n):
        len = sqrt(n)
        m1 = n - 1 / 2 * (len - 1)
        m2 = n - 1 / 2 * (len - 1) * 3
        m3 = n - 1 / 2 * (len - 1) * 5
        m4 = n - 1 / 2 * (len - 1) * 7
        return m1, m2, m3, m4

    def calculate(self, number):
        n = 1

        if number <= 1:
            return 0

        while n * n < number:
            n = n + 2

        centers = self.getCentres(n * n)

        minval = inf
        for cen in centers:
            if abs(cen - number) < minval:
                minval = abs(cen - number)

        return sqrt(n * n) - 1 - (n - 1) / 2 + minval


if __name__ == "__main__":
    sm = SpiralMemory()
    result = sm.calculate(368078)
    print(result)
