import functools


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
