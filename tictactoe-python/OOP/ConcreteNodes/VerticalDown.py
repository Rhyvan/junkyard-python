import Node


class VerticalDown(Node.Node):
    index = 0

    def isTrue(self, table, value):
        try:
            return table[self.r + self.i][self.c] == value
        except IndexError:
            return False