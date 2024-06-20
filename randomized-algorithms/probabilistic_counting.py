import math
import random


class MorrisCounter:
    def __init__(self, n_i: callable):
        """
        Take a sequence n_i which acts as an estimate for the actual count
        :param n_i: callable sequence n_i
        """
        self.n_i = n_i
        self.i = 0

    def increment(self):
        self.i += 1

    def count(self, n: int):
        """
        Simulate counting n times.
        :param n: The value
        :return:
        """
        for _ in range(n):
            delta = random.random()
            if delta < 1 / (self.n_i(self.i + 1) - self.n_i(self.i)):
                self.increment()
        print(f"Estimated count: {self.n_i(self.i)}")


if __name__ == "__main__":
    counter = MorrisCounter(n_i=lambda i: 2 ** (i - 1) if i else 0)
    counter.count(10000)
