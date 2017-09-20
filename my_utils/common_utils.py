import functools


def coroutine(skip=1):
    def decorator(func):
        """
        this decorator will run the first next of the generator
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            generator = func(*args, **kwargs)
            for _ in range(skip):
                next(generator)
            return generator

        return wrapper

    return decorator
