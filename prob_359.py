class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.di = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        # print(self.di)
        if message in self.di:
            if timestamp - self.di[message] >= 10:
                self.di[message] = timestamp
                return True
            else:
                return False
        else:
            self.di[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)