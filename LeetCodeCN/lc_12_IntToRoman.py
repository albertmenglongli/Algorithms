class Solution:
    def intToRoman(self, num: int) -> str:
        num_str_mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        res = ''

        config = [
            [1000, 5000, 100000],
            [100, 500, 1000],
            [10, 50, 100],
            [1, 5, 10],
        ]

        idx = 0
        while num != 0:
            min_num = config[idx][0]
            mid_num = config[idx][1]
            max_num = config[idx][2]

            min_str = num_str_mapping.get(min_num, '')
            mid_str = num_str_mapping.get(mid_num, '')
            end_str = num_str_mapping.get(max_num, '')

            if num // min_num != 0:
                digit = num // min_num

                if 1 <= digit <= 3:
                    # 1, 2, 3
                    res += min_str * digit
                elif digit == 4:
                    # 4
                    res += min_str + mid_str
                elif digit == 5:
                    # 5
                    res += mid_str
                elif 6 <= digit <= 8:
                    # 6, 7, 8
                    res += mid_str + (digit - 5) * min_str
                else:
                    # 9
                    res += min_str + end_str

            num -= (num // min_num) * min_num
            idx += 1

        return res


print(Solution().intToRoman(3))
print(Solution().intToRoman(4))
print(Solution().intToRoman(9))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
