# Similar to https://leetcode.com/problems/stock-price-fluctuation/description/
#
# Need a balanced binary search tree (AVL tree or red-black tree)
#
# SortedDict.peekitem(0): returns a k-v pair in which the key is the minum in SortedDict.
# peekitem() or peekitem(-1): returns the maximum k-v pair
#
# update(): O(NlogN). N is the number of records in the input stream
# current(): O(1)
# max/min/current(): O(1) (even using time_to_prices = SortedDict())

# Solution 1: two sorted_hashmap
# to support delete we need another sorted hashmap
from sortedcontainers import SortedDict


class StockPrice:
    def __init__(self):
        # For returning the current price
        self.time_to_prices = SortedDict()  # sorted_map <time_stamp, price>
        # For returning the min/max price
        self.price_counter = SortedDict()  # sorted_map < price, num_occurrences > , always contains valid prices

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_to_prices:  # if this update() corrects an existing record
            legacy_price = self.time_to_prices[timestamp]

            self.price_counter[legacy_price] -= 1  # Update the existing price
            # Required. Ensure price_counter always contains valid prices
            if self.price_counter[legacy_price] == 0:
                self.price_counter.pop(legacy_price)

        if price is None:
            self.time_to_prices.pop(timestamp)
            return

        if price not in self.price_counter:
            self.price_counter[price] = 0
        self.price_counter[price] += 1
        self.time_to_prices[timestamp] = price

    def current(self) -> int:
        # return self.time_to_prices.peekitem(-1)[1]
        return self.time_to_prices.peekitem()[1]  # default peekitem() returns the maximum k-v pair

    def maximum(self) -> int:
        # return self.rec.peekitem(-1)[0]
        return self.price_counter.peekitem()[0]  # default peekitem() returns the maximum k-v pair

    def minimum(self) -> int:
        return self.price_counter.peekitem(0)[0]

    def out(self):
        print(self.maximum(), self.minimum(), self.current())


sp = StockPrice()
sp.update(100, 13)
sp.out()
sp.update(101, 14)
sp.out()
sp.update(102, 10)
sp.out()
sp.update(103, 12)
sp.out()
sp.update(101, 11)
sp.out()
sp.update(102, None)
sp.out()

# Solution 2: hash_map + sorted_hashmap
# from sortedcontainers import SortedDict
# class StockPrice:
#
#     def __init__(self):
#         self.latest_price = -1
#         self.latest_time = -1
#         self.time_to_prices = {}  # hash_map <time_stamp, price>
#         self.price_counter = SortedDict()  # sorted_map <price, num_occurrences>
#
#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp in self.time_to_prices:  # if this update() corrects an existing record
#             old_price = self.time_to_prices[timestamp]
#
#             self.price_counter[old_price] -= 1  # Remove the existing record
#             # Required. Ensure rec always contains valid prices
#             if self.price_counter[old_price] == 0:
#                 self.price_counter.pop(old_price)
#
#         if price not in self.price_counter:
#             self.price_counter[price] = 0
#         self.price_counter[price] += 1
#         self.time_to_prices[timestamp] = price
#         if timestamp >= self.latest_time:
#             self.latest_price = price
#             self.latest_time = timestamp
#
#     def current(self) -> int:
#         # return self.time_to_prices.peekitem(-1)[1]
#         # return self.time_to_prices.peekitem()[1] # default peekitem() returns the maximum k-v pair
#         return self.latest_price
#
#     def maximum(self) -> int:
#         # return self.rec.peekitem(-1)[0]
#         return self.price_counter.peekitem()[0]
#
#     def minimum(self) -> int:
#         return self.price_counter.peekitem(0)[0]


# Solution 3: two sorted_hashmap
# from sortedcontainers import SortedDict
# class StockPrice:
#
#     def __init__(self):
#         self.time_to_prices = SortedDict()  # sorted_map <time_stamp, price>
#         self.rec = SortedDict()  # sorted_map < price, set(time_stamp) >
#
#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp in self.time_to_prices:  # if this update() corrects an existing record
#             prev_price = self.time_to_prices[timestamp]
#
#             self.rec[prev_price].remove(timestamp)  # Remove the existing record
#             # Required. Ensure rec always contains valid prices
#             if len(self.rec[prev_price]) == 0:
#                 self.rec.pop(prev_price)
#
#         if price not in self.rec:
#             self.rec[price] = set()
#         self.rec[price].add(timestamp)
#         self.time_to_prices[timestamp] = price
#
#     def current(self) -> int:
#         return self.time_to_prices.peekitem(-1)[1]
#
#     def maximum(self) -> int:
#         # return self.rec.peekitem(-1)[0]
#         return self.rec.peekitem()[0]  # default peekitem() returns the maximum k-v pair
#
#     def minimum(self) -> int:
#         return self.rec.peekitem(0)[0]


# Solution 4: hashmap + two heaps
# class StockPrice:
#     def __init__(self):
#         self.latest_time = 0
#         # Store price of each stock at each timestamp.
#         self.timestamp_price_map = {}
#
#         # Store stock prices in sorted order to get min and max price.
#         self.max_heap = []
#         self.min_heap = []
#
#     def update(self, timestamp: int, price: int) -> None:
#         # Update latestTime to latest timestamp.
#         self.timestamp_price_map[timestamp] = price
#         self.latest_time = max(self.latest_time, timestamp)
#
#         # Add latest price for timestamp.
#         heappush(self.min_heap, (price, timestamp))
#         heappush(self.max_heap, (-price, timestamp))
#
#     def current(self) -> int:
#         # Return latest price of the stock.
#         return self.timestamp_price_map[self.latest_time]
#
#     def maximum(self) -> int:
#         price, timestamp = self.max_heap[0]
#
#         # Pop pairs from heap with the price doesn't match with hashmap.
#         while -price != self.timestamp_price_map[timestamp]:
#             heappop(self.max_heap)
#             price, timestamp = self.max_heap[0]
#
#         return -price
#
#     def minimum(self) -> int:
#         price, timestamp = self.min_heap[0]
#
#         # Pop pairs from heap with the price doesn't match with hashmap.
#         while price != self.timestamp_price_map[timestamp]:
#             heappop(self.min_heap)
#             price, timestamp = self.min_heap[0]
#
#         return price
