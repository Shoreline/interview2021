class SnapshotArray:
    def __init__(self, length: int):
        self.id = 0
        self.history_records = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.history_records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.history_records[index], [snap_id, 10 ** 9])
        return self.history_records[index][snap_index - 1][1]

class SnapshotSet(object):
    def __init__(self):
        self.hash = {}  # map key to a list of snapshot tuples
        self.snap_id = 0
        self.data = []  # list of distinct keys in hash for creating iterator.

    def add(self, key):
        if key not in self.hash:
            self.hash[key] = [(self.snap_id, True)]
            self.data.append(key)
        else:
            if self.hash[key][0] != self.snap_id:
                self.hash[key].append((self.snap_id, True))

    def remove(self, key):
        if key not in self.hash:
            return
        if self.hash[key][0] != self.snap_id:
            self.hash[key].append((self.snap_id, False))
        else:
            self.hash[key] = (self.snap_id, True)

    def contains(self, key):
        # Time: O(1).
        return self.contains_snapshot(key)

    def contains_snapshot(self, key, snap_id=None):
        # Time: O(logm), where m is number of snapshot versions for the key.
        if key not in self.hash:
            return False
        if snap_id is None:
            return self.hash[key][-1][1]
        # Binary search for the rightmost tuple such that tuple[0] <= snap_id.
        row = self.hash[key]
        start = 0
        end = len(row) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if row[mid][0] <= snap_id:
                start = mid
            else:
                end = mid
        if row[end][0] <= snap_id:
            return row[end][1]
        if row[start][0] <= snap_id:
            return row[start][1]
        return False

    def iterator(self):
        it = Iterator(self.snap_id, self, len(self.data))
        self.snap_id += 1
        return it


class Iterator(object):
    def __init__(self, snap_id, snap_set, length):
        self.snap_id = snap_id
        self.snap_set = snap_set
        self.length = length
        self.i = 0
        self.next_key = None
        self.load()

    def load(self):
        # O(nlogm), where n is number of keys in the set and m is the number of
        # snapshots for a key.
        data = self.snap_set.data
        ss = self.snap_set
        n = self.length
        # Skip non-existing keys for this snapshot.
        while self.i < n \
                and not ss.contains_snapshot(data[self.i], self.snap_id):
            self.i += 1
        if self.i < n:
            self.next_key = data[self.i]
            self.i += 1
        else:
            self.next_key = None

    def next(self):
        res = self.next_key
        self.load()
        return res

    def has_next(self):
        return self.next_key is not None


ss = SnapshotSet()
# ss.add('k1')
# ss.add('k2')
# ss.add('k3')
# it1 = ss.iterator()
# ss.add('k4')
# ss.remove('k3')
# print('it1:')
# # k1, k2, k3
# while it1.has_next():
#           print(it1.next())
# it2 = ss.iterator()
# print('it2:')
# # k1, k2, k4
# while it2.has_next():
#           print(it2.next())
# assert ss.contains('k1')
# assert ss.contains('k4')
# assert not ss.contains('k3')
# ss.add('k1')
# ss.add('k5')
# ss.add('k3')
# it3 = ss.iterator()
# print('it3:')
# # k1, k2, k3, k4, k5
# while it3.has_next():
#           print(it3.next())
# ss.remove('k1')
# assert not ss.contains('k1')
# ss.add('k1')
# assert ss.contains('k1')
# ss.remove('k1')
# it4 = ss.iterator()
# ss.add('k1')
# print('it4:')
# # k2, k3, k4, k5
# while it4.has_next():
