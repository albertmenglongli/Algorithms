"""
When prototyping (or even finalizing) data structures such as trees, it can be useful to have a flexible
class that will allow you to specify arbitrary attributes in the constructor. 
In these cases, the “Bunch” pattern (named by Alex Martelli in the Python Cookbook) can come in handy.
There are many ways of implementing it, but the gist of it is the following:
"""


class Bunch(dict):
    """docstring for Bunch"""

    def __init__(self, *arg, ** kwargs):
        super(Bunch, self).__init__(*arg, **kwargs)
        self.__dict__ = self

T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))
print t.left.right
print t['left']['right']


"""
This pattern isn’t useful only when building trees, of course.
You could use it for any situation where you’d want a flexible object
whose attributes you could set in the constructor.
"""
