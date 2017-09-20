import functools
import abc

__all__ = ['MinHolder', 'MaxHolder']


def coroutine(func):
    """
    this decorator will run the first next of the generator
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        next(generator)
        return generator

    return wrapper


@coroutine
def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


@coroutine
def maximum():
    current = yield
    while True:
        value = yield current
        current = max(value, current)


class SingleValueHolder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.it = self.generate_it()

    @abc.abstractmethod
    def generate_it(self):
        raise NotImplementedError()


class MinHolder(SingleValueHolder):
    positive_infinite = float('inf')

    def generate_it(self):
        return minimize()

    def send(self, value):
        self.it.send(value)

    @property
    def minimum(self):
        return self.it.send(self.positive_infinite)


class MaxHolder(SingleValueHolder):
    negative_infinite = float('-inf')

    def generate_it(self):
        return maximum()

    @property
    def maximum(self):
        return self.it.send(self.negative_infinite)


if __name__ == "__main__":
    my_min = MinHolder()

    for i in [10, 20, -5, 3]:
        my_min.send(i)

    print(my_min.minimum)
