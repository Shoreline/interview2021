# copied, revised
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # saves non-empty segment names from the root to current directory

        # Split the input string and process each segment
        for seg in path.split("/"):
            if seg == "." or not seg:  # "." means current directory, so no need to do anything
                continue
            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            elif seg == "..":
                if stack:
                    stack.pop()
                else: # do nothing
                    continue
            else:
                stack.append(seg)  # found a normal directory name, add it to the stack

        res = "/" + "/".join(stack) # manually add the first '/'
        return res
