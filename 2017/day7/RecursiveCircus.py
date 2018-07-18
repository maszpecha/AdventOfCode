class RecursiveCircus:
    def __init__(self, name):
        self.filename = name

    def read(self):
        roots = []
        leafs = []
        file = open(self.filename, 'r')
        for line in file:
            if "->" in line:
                data = line.split("->")
                roots.append(data[0].split()[0])
                leafs.extend(data[1].replace(',', '').split())
        return roots, leafs

    def findRoot(self, roots, leafs):
        for root in roots:
            if root not in leafs:
                return root


if __name__ == "__main__":
    rc = RecursiveCircus("input.txt")
    roots, leafs = rc.read()
    root = rc.findRoot(roots, leafs)
    print(root)
