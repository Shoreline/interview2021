# ord('A') is 65
class Excel:
    def __init__(self, H, W):
        # num_rows = Height
        # num_columns = Width
        self.M = [[{'v': 0, 'sum': None} for j in range(ord(W) - ord('A') + 1)] for i in range(H)]

    def set(self, r, c, v):
        self.M[r - 1][ord(c) - ord('A')] = {'v': v, 'sum': None}

    def get(self, r, c):
        cell = self.M[r - 1][ord(c) - ord('A')]
        if not cell['sum']:
            return cell['v']

        sum_vals = 0
        for pos in cell['sum']:
            sum_vals += self.get(pos[0], pos[1]) * cell['sum'][pos]  # get cell value * cell_occurences

        return sum_vals

    # def sum(self, row: int, column: str, numbers: List[str]) -> int:
    def sum(self, r, c, strs):
        self.M[r - 1][ord(c) - ord('A')]['sum'] = self.compute(strs)
        return self.get(r, c)

    # returns a counter which counts the number of occurences of the cell in the sum string.
    def compute(self, strs):
        c = collections.Counter()
        for s in strs:
            start, end = s, s
            if ':' in s:
                # start, end = s.split(':')[0], s.split(':')[1]
                start, end = s.split(':')

            for i in range(int(start[1:]), int(end[1:]) + 1):
                for j in range(ord(start[0]) - 64, ord(end[0]) - 64 + 1):
                    c[(i, chr(j + 64))] += 1
        return c

    # Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)