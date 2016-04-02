class Bunch(dict):
    """docstring for Bunch"""

    def __init__(self, *arg, ** kwargs):
        super(Bunch, self).__init__(*arg, **kwargs)
        self.__dict__ = self

T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))
print t.left.right
print t['left']['right']
