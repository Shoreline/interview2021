# PS: "Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right."

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # cur saves words of the current line;
        # num_of_letters saves the total number of characters of the current line
        res, cur, num_of_letters = [], [], 0
        for w in words:

            # Check if in need to pause and construct cur[] into a new line
            # len(cur) is added: it represents the natural whitespace after each word
            if num_of_letters + len(w) + len(cur) > maxWidth:  # still have enough room

                # Add desired whitespaces one by one to the end of each word
                for i in range(maxWidth - num_of_letters):  # number of spaces
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))

                # incomplete, can't handle all corner cases
                # count = maxWidth - num_of_letters
                # rem = count % (len(cur) - 1) if len(cur) > 1 else count
                # tmp = []
                # for i in range(len(cur) - 1):
                #     tmp.append(cur[i])
                #     tmp.append(" " * (count // (len(cur) - 1)) )
                #     if rem > 0:
                #         tmp.append(" ")
                #         rem -= 1
                # tmp.append(cur[-1])
                # res.append(''.join(tmp))

                cur, num_of_letters = [], 0  # reset

            cur += [w]
            num_of_letters += len(w)

        # don't forget the last current line
        return res + [' '.join(cur).ljust(maxWidth)]