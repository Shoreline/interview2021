from typing import Dict

class Sock:
    def __init__(self, color: str, side: str) -> None:
        self.color = color
        self.side = side

from typing import List
import collections

def pair_socks(unpaired_socks: List[Sock], matching_colors: List[List[str]]) -> List[List[int]]:
    store = collections.defaultdict(dict) # map<color, <side,list<index+1> >>
    res = []

    for i, sock in enumerate(unpaired_socks):
        other_side = 'left' if sock.side == 'right' else 'right'

        if other_side in store[sock.color]:
            res.append({store[sock.color][other_side].pop(), i+1}) # deal with same color

            if not store[sock.color][other_side]:
                store[sock.color].pop(other_side)   # clean up

        else:
            if sock.side not in store[sock.color]:
                store[sock.color][sock.side] = []

            store[sock.color][sock.side].append(i+1)

    # follow up: deal with other matching colors
    for c1, c2 in matching_colors:
        if c1 in store and c2 in store:
            for side1, side2 in [['right', 'left'], ['left', 'right']]:
                if side1 in store[c1] and side2 in store[c2]:
                    while store[c1][side1] and store[c2][side2]:
                        res.append({ store[c1][side1].pop(), store[c2][side2].pop() })

    return res


unpaired_socks = [
    Sock('black', 'left'),
    Sock('pink', 'right'),
    Sock('pink', 'left'),
    Sock('black', 'right'),
    Sock('black', 'right'),
    Sock('black', 'left'),
    Sock('black', 'right'),
    Sock('pink', 'right'),
    Sock('yellow', 'left'),
]

print(pair_socks(unpaired_socks, [['yellow', 'black']]))