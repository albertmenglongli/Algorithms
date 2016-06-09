class Solution(object):
    @staticmethod
    def compareVersion(version1, version2):
        v1_lst = [int(e) for e in  version1.split('.')]
        v2_lst = [int(e) for e in  version2.split('.')]
        len_v1_lst = len(v1_lst)
        len_v2_lst = len(v2_lst)
        for (num1, num2) in zip(v1_lst, v2_lst):
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        if(len_v2_lst > len_v1_lst):
            for num2 in v2_lst[len_v1_lst: len_v2_lst]:
                if num2 != 0:
                    return -1
        elif(len_v2_lst < len_v1_lst):
            for num1 in v1_lst[len_v2_lst: len_v1_lst]:
                if num1 != 0:
                    return 1
        return 0
