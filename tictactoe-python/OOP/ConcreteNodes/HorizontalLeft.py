import Node


class HorizontalLeft(Node.Node):
    index = 1

    def isTrue(self, table, value):
        if self.c - self.i >= 0:
            return table[self.r][self.c - self.i] == value

        return False