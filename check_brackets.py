# python3

from collections import namedtuple
import sys

# this is a class to store the bracket being added to the stack
# and the index of said bracket in the input
class Node:
    def __init__ (self, value, idx):
        self.value = value
        self.index = idx


# this function returns the index of the first unmatched closing bracket (priority 1).
# if there's no unmatched closing bracket, the function returns the index of the first unmatched opening bracket (priority 2)
# note that the index being returned by this function is in 1-based index scheme
# if all brackets match up properly, the function returns "Success"
# e.g.1. input = "{}], output = 3 (priority 1)
# e.g.2. input = "(){]", output = 4 (priority 1)
# e.g.3. input = "(()[", output = 1 (priority 2)
def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # For every opening bracket, create a node to store the bracket and its index in the input
            # add the node to the opening_brackets_stack
            opening_brackets_stack.append(Node(next,i))
        if next in ")]}":
            # if there is no opening brackets on the stack to match up with this closing bracket
            # return the index of this (first) closing bracket in a 1-based index scheme
            if len(opening_brackets_stack) == 0:
                return i + 1
            else:
                # if the closing bracket matches up with the last opening bracket on the stack,
                # remove the opening bracket from the stack
                if (next == ")" and opening_brackets_stack[-1].value == "(") or (next == "]" and opening_brackets_stack[-1].value == "[") or (next == "}" and opening_brackets_stack[-1].value == "{"):
                    opening_brackets_stack.pop()
                # otherwise, return the index of the unmatched closing bracket in a 1-based index scheme
                else:
                    return i + 1
    # if there are still opening brackets on the stack after iterating through the text
    # return the index of the first opening bracket on the deck in a 1-based index scheme
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0].index + 1
    # otherwise, return "Success" to indicate that all brackets match up properly
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
