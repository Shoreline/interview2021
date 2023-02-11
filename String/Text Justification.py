# PS: "Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does
# not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the
# right."

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_line = []
        cur_line_words_width = 0

        for word in words:
            if cur_line_words_width + len(cur_line) + len(word) > maxWidth:
                spaces = maxWidth - cur_line_words_width
                # Add space after each one but the last word in line!
                for i in range(spaces):
                    pos = i % (len(cur_line) - 1) if len(cur_line) > 1 else 0
                    cur_line[pos] += ' '
                res.append(''.join(cur_line))
                cur_line = []
                cur_line_words_width = 0

            cur_line.append(word)
            cur_line_words_width += len(word)

        # don't forget the last current line
        # return res + [' '.join(cur_line).ljust(maxWidth)]
        if cur_line:
            res.append(' '.join(cur_line))
            res[-1] += ' ' * (maxWidth - len(res[-1]))

        return res

# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         # cur saves words of the current line;
#         # num_of_letters saves the total number of characters of the current line
#         res, cur, num_of_letters = [], [], 0
#         for w in words:
#
#             # Check if in need to pause and construct cur[] into a new line
#             # len(cur) is added: it represents the natural whitespace after each word
#             # If adding w will exceed the maxWidth, then build a new line.
#             if num_of_letters + len(cur) + len(w) > maxWidth:
#
#                 # Add desired whitespaces one by one to the end of each word
#                 for i in range(maxWidth - num_of_letters):  # number of spaces
#                     cur[i % (len(cur) - 1 or 1)] += ' '
#                 res.append(''.join(cur))
#                 cur, num_of_letters = [], 0  # reset
#
#             cur += [w]
#             num_of_letters += len(w)
#
#         # don't forget the last current line
#         return res + [' '.join(cur).ljust(maxWidth)]