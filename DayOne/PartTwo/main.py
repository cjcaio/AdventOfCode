class AoC:
    def __init__(self):
        self.script = 'script.txt'
        self.input = []

    def read_input(self):
        with open(self.script, "r") as f:
            self.input = f.read().splitlines()

    def break_lines(self):
        lines = self.input
        left_column = []
        right_column = []
        for i in lines:
            if '   ' in i:
                left_column.append(i[0:i.index('   ')])
                right_column.append(i[i.index('   ') + 3:])

        lColumn = [int(x) for x in left_column]
        rColumn = [int(x) for x in right_column]

        lColumn.sort()
        rColumn.sort()

        return lColumn, rColumn

    def times_each_appears(self):
        lcolumn, rcolumn = self.break_lines()
        sum = 0
        hash = {}
        for i in range(len(lcolumn)):
            for j in range(len(rcolumn)):
                if lcolumn[i] == rcolumn[j]:
                    num = lcolumn[i]
                    if num not in hash:
                        hash[num] = 0
                    hash[num] += 1

        return hash

    def calculate_similarity_score(self, hash):
        sum = 0
        for i in hash:
            sum += i * hash[i]

        print(sum)
        return sum

    def run(self):
        self.read_input()
        lcolumn, rcolumn = self.break_lines()
        hash = self.times_each_appears()
        sum = self.calculate_similarity_score(hash) ## answer


aoc = AoC()
aoc.run()
