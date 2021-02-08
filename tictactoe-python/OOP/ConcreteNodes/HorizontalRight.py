import Node


class HorizontalRight(Node.Node):
    index = 1

    def isTrue(self, table, value):
        try:
            return table[self.r][self.c + self.i] == value
        except IndexError:
            return False