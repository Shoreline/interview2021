class Logger:

    def __init__(self):
        self.thresholds = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.thresholds.get(message, 0):
            return False

        self.thresholds[message] = timestamp + 10
        return True

# class Logger:

#     def __init__(self):
#         self.last_seen = {}

#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

#         if message in self.last_seen and self.last_seen[message] + 10 > timestamp:
#             return False

#         self.last_seen[message] = timestamp
#         return True