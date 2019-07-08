# -*- coding:utf-8 -*-


class Solution(object):
    from operator import add, mul, sub
    op_mapping = {
        '+': add,
        '-': sub,
        '*': mul,
    }

    def dfs_for_building_operation_tree(self, start, end):
        numbers = self.numbers
        operators = self.operators
        lst = []
        # 利用数组range的上下限, 来控制递归的结束情况,

        for i in range(start, end + 1):
            op_function = self.op_mapping[operators[i]]

            left_child_values = self.dfs_for_building_operation_tree(start, i - 1)
            right_child_values = self.dfs_for_building_operation_tree(i + 1, end)

            # 左子节点没有值列表, 说明是当前运算符的左边应该是原始的操作数
            if not left_child_values:
                # 加入原始的左操作数
                left_child_values.append(numbers[i])
            # 右子节点没有值列表, 说明是当前运算符的右边应该是原始的操作数
            if not right_child_values:
                # 加入原始的右操作数
                right_child_values.append(numbers[i + 1])

            for left_child_value in left_child_values:
                for right_child_value in right_child_values:
                    value = op_function(left_child_value, right_child_value)
                    lst.append(value)
        return lst

    def extract_numbers_operators(self, s):
        i, j = 0, 0
        operators = []
        numbers = []
        while True:
            if j == len(s):
                numbers.append(int(s[i:j]))
                break
            if s[j] in ('+', '-', '*'):
                numbers.append(int(s[i:j]))
                operators.append(s[j])
                i = j + 1
            j += 1
        return numbers, operators

    def diffWaysToCompute(self, input):
        """
        :type n: int
        :rtype: List[TreeNode]

        """
        self.numbers, self.operators = self.extract_numbers_operators(input)
        numbers = self.numbers
        operators = self.operators

        # 处理特殊输入情况
        if not operators and numbers:
            the_only_number = numbers[0]
            return [the_only_number]

        # 以构建树型结构的方式, dfs 计算结果
        '''
            以 "2*3-4*5" 为例
           *         *     *      -      *
            \       /     /      / \      \
             *     -     *      *   *      -
            /     /       \                 \
           -     *         -                 *
        '''
        n = len(operators)
        return self.dfs_for_building_operation_tree(0, n - 1)


s = "2*3-4*5"
# s = "2-1-1"
# s = "0"
print(Solution().diffWaysToCompute(s))
