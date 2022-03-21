class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.vector = v  # self.vector is also a 2d vector
        self.inner = 0  # points to current index of the outer vector
        self.outer = 0  # points to current index of the inner vector

        self.advance_to_next_outer_list_if_needed()

        # Point to the next integer

    # Let inner and outer pointers point to an integer. Or if we have reached the end, let the outer pointer pointer = len(v)
    # Do nothing if the pointers are already pointing to an integer.
    def advance_to_next_outer_list_if_needed(self):
        # While outer is still within the vector, but inner is over the
        # end of the inner list pointed to by outer, we want to move
        # forward to the start of the next inner vector.
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        self.advance_to_next_outer_list_if_needed()
        return result

    def hasNext(self) -> bool:
        return self.outer < len(self.vector)

# class Vector2D:

#     def __init__(self, v: List[List[int]]):
#         self.vector = v
#         self.inner = 0
#         self.outer = 0

#     # Let inner and outer pointers point to an integer. Or if we have reached the end, let the outer pointer pointer = len(v)
#     # Do nothing if the pointers are already pointing to an integer.
#     def advance_to_next(self):
#         # While outer is still within the vector, but inner is over the
#         # end of the inner list pointed to by outer, we want to move
#         # forward to the start of the next inner vector.
#         while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
#             self.outer += 1
#             self.inner = 0

#     def next(self) -> int:
#         # Ensure the position pointers are moved such they point to an integer,
#         # or put outer = vector.length.
#         self.advance_to_next()
#         # Return current element and move inner so that is after the current
#         # element.
#         result = self.vector[self.outer][self.inner]
#         self.inner += 1
#         return result


#     def hasNext(self) -> bool:
#         # Ensure the position pointers are moved such they point to an integer,
#         # or put outer = vector.length.
#         self.advance_to_next()
#         # If outer = vector.length then there are no integers left, otherwise
#         # we've stopped at an integer and so there's an integer left.
#         return self.outer < len(self.vector)

# Same solution as https://leetcode.com/problems/flatten-nested-list-iterator/
# class Vector2D:

#     def __init__(self, vec: List[List[int]]):
#         self.stack = vec[::-1]

#     def next(self) -> int:
#         self.format()
#         return self.stack.pop()[0]

#     def hasNext(self) -> bool:
#         self.format()
#         return len(self.stack) > 0

#     # Make sure the top item in self.stack is a list with only one element
#     def format(self):

#         while self.stack and (len(self.stack[-1])!=1):
#             top_list = self.stack.pop()
#             for i in range(len(top_list) -1 , -1, -1):
#                 self.stack.append([top_list[i]])
#         return


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()