class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s_without_dash = list(S.replace('-', ''))
        n = len(s_without_dash)
        num_of_dash = n / K if n % K != 0 else n / K - 1
        new_string_list = s_without_dash + [''] * num_of_dash
        idx = n + num_of_dash - 1
        p = n - 1
        flag_of_dash = K
        while idx >= 0:
            if flag_of_dash:
                new_string_list[idx] = new_string_list[p].upper()
                flag_of_dash -= 1
                p -= 1
            else:
                new_string_list[idx] = '-'
                flag_of_dash = K
            idx -= 1

        return ''.join(new_string_list)
