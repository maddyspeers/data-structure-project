import abc
from lrlist import MTList, NEList, LengthAlgo, ToStringAlgo


class Stack(abc.ABC):
    """
    Abstract class for a stack.
    DO NOT CHANGE THIS CLASS!
    """

    @abc.abstractmethod
    def push(self, elt):
        """
        Pushes an element onto the top of the stack
        :param elt: the element to add to the stack
        """
        return

    @abc.abstractmethod
    def pop(self):
        """
        Removes the top element from the stack
        """
        return

    @abc.abstractmethod
    def top(self):
        """
        Returns the top element on the stack (without removing it)
        :return: the top element on the stack (without removing it)
        """
        return

    @abc.abstractmethod
    def is_empty(self):
        """
        Returns True if and only if the stack is empty
        :return: True if and only if the stack is empty
        """
        return

    @abc.abstractmethod
    def __str__(self):
        return

    @abc.abstractmethod
    def __repr__(self):
        return


class LRStack(Stack):
    def __init__(self):
        self._elements = MTList()
    def push(self, elt):
        self._elements = NEList(elt, self._elements)
        return

    def pop(self):
        if self.is_empty():
            raise AttributeError("Can't pop from an empty stack!")
        elt = self._elements.get_elt()
        self._elements = self._elements.get_rest()
        return elt

    def top(self):
        if self.is_empty():
            raise AttributeError("Can't top from an empty stack!")
        return self._elements.get_elt()

    def is_empty(self):
        return isinstance(self._elements, MTList)
    def size(self):
        return self._elements.execute(LengthAlgo())

    def __str__(self):
        return self._elements.execute(ToStringAlgo())

    def __repr__(self):
        return f"LRStack LRList {str(self._elements)}"

if __name__ == '__main__':
    # This is here for your own use
    pass
