from urllib.parse import unquote_plus
import random


def encoding(lines):
    # l = len(lines)
    res = ""
    for i in range(len(lines) - 1):
        cur_line, next_line = lines[i], lines[i + 1]
        # find the max overlap part, between the latter piece of cur_line and the starting piece of next_line:
        for j in range(len(next_line)):
            # if next_line[:j + 1] == cur_line[cur_len - j - 1:]:
            if next_line[:j + 1] == cur_line[-(j + 1):]:
                # cur_line = cur_line[:cur_l - j - 1]
                res += unquote_plus(cur_line[:len(cur_line) - (j + 1)])
                break
        # res += unquote_plus(cur_line)
    res += unquote_plus(lines[-1])  # corner case
    return res


def encodeing_shuffling(str_list):
    # random.shuffle(str_list)
    # l = len(str_list)

    # brute force
    # can use topological sort?
    def helper(cur_str, i, visited):
        cur_l = len(cur_str)
        for j in range(l):
            if not visited[j] and i != j:
                next_str = str_list[j]
                overlapped = False

                for j in range(len(next_str)):
                    if next_str[:j + 1] == cur_str[cur_l - j - 1:]:
                        pre_str = prev_str[:cur_l - j - 1]
                        overlapped = True
                        break

                if overlapped:
                    new_visited = visited.copy()
                    helper(next_str, j, new_visited)


lines = ["%2F%2FSample+progra",
         "e+program%0Apubli",
         "m%0Apublic+class+"]
print(lines)
print(encoding(lines))

# def encodeing_shuffling(str_list):
#     random.shuffle(str_list)
#     l = len(str_list)
#
#     def helper(cur_str, i, visited):
#         cur_l = len(cur_str)
#         for j in range(l):
#             if not visited[j] and i != j:
#                 next_str = str_list[j]
#                 overlapped = False
#
#                 for j in range(len(next_str)):
#                     if next_str[:j + 1] == cur_str[cur_l - j - 1:]:
#                         pre_str = prev_str[:cur_l - j - 1]
#                         overlapped = True
#                         break
#
#                 if overlapped:
#                     new_visited = visited.copy()
#                     helper(next_str, j, new_visited)
