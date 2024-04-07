from Practice1.abstract_object import Employee


class DoubleNode:

    def __init__(self, data: Employee):
        self.data = data
        self.next: None | DoubleNode = None
        self.prev: None | DoubleNode = None

    def __repr__(self):
        return self.data
