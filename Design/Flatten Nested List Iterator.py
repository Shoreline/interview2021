# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Unlike "flatten 2d vector", this problem gives a custom class NestedInteger
# Don't do flatten unless needed.
# Use a stack (list) to save NestedInteger elements in reverse order.
#   The reason of using reverse order, is because list.pop() is o(1) for the last element, not the first
# While poping the top NestedInteger, if it is not a singular integer, flatten its NestedInteger list and push back to stack in reverse order
# Not ideal since the constructor takes a O(n) time
# Tricky part is empty list like [[]]
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        self.format()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.format()
        return len(self.stack) > 0

    # let the top element in stack is an Integer
    def format(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return
            else:
                top_element = self.stack.pop()
                self.stack.extend(top_element.getList()[::-1])

            # Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())