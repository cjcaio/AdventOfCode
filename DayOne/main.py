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
                right_column.append(i[i.index('   ')+3:])

        lColumn = [int(x) for x in left_column]
        rColumn = [int(x) for x in right_column]

        lColumn.sort()
        rColumn.sort()

        return lColumn, rColumn

    def difference_between_numns(self, lcolumn, rcolumn):
        sum = 0
        for i in range(len(lcolumn)):
            sum += abs(lcolumn[i] - rcolumn[i])

        return sum

    def run(self):
        self.read_input()
        lcolumn, rcolumn = self.break_lines()
        sum = self.differenc_between_numns(lcolumn, rcolumn)
        print(sum) ## answer

aoc = AoC()
aoc.run()