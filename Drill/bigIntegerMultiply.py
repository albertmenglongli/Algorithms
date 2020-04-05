class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        c = [0] * (l1 + l2)
        for i in range(0, l1):
            for j in range(0, l2):
                c[i + j] += (ord(num2[j]) - ord('0')) * (ord(num1[i]) - ord('0'))
                c[i + j + 1] += c[i + j] // 10
                c[i + j] %= 10
        cl = l1 + l2
        while c[cl - 1] == 0 and cl > 1:
            cl -= 1

        res = ''.join(str(v) for v in c[cl - 1::-1])
        return res


print(Solution().multiply('456', '123'))
