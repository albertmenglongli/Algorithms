class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
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

def main():
    path = "/User/menglong/./home/../"
    print Solution().simplifyPath(path)

if __name__ == "__main__":
    main()
