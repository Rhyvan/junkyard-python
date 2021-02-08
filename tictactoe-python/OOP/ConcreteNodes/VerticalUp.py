import Node


class VerticalUp(Node.Node):
    index = 0

    def isTrue(self, table, value):
        if self.r - self.i >= 0:
            return table[self.r - self.i][self.c] == value

        return False