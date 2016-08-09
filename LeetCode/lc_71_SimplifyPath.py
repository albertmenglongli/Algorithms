class Solution(object):

    @staticmethod
    def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        >>> path = "/User/menglong/./home/../"
        >>> Solution().simplifyPath(path)
        '/User/menglong'
        """
        lst = [tmp for tmp in path.split('/') if tmp and tmp != '.']
        lst.reverse()
        stack = list()
        while len(lst):
            tmp = lst.pop()
            if tmp != '..':
                stack.append(tmp)
            elif len(stack):
                stack.pop()
        return '/' + '/'.join(stack)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
