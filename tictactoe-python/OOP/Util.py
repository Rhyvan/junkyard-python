from collections import deque
from ConcreteNodes import (
    VerticalDown as VD,
    VerticalUp as VU,
    HorizontalLeft as HL,
    HorizontalRight as HR,
)


class Util:
    directions = 4

    @staticmethod
    def generate_queue(row, column):
        q = deque()
        q.append(VD.VerticalDown(row, column))
        q.append(VU.VerticalUp(row, column))
        q.append(HL.HorizontalLeft(row, column))
        q.append(HR.HorizontalRight(row, column))

        return q

    @staticmethod
    def get_tracker():
        return [1 for x in range(int(Util.directions / 2))]
