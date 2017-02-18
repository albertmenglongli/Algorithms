# -*- coding:utf-8 -*-

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        print self.value


class Solution(object):
    def dfs_for_building_operation_tree(self, start, end):
        lst = []
        # 利用数组range的上下限, 来控制递归的结束情况,
        # 即如果start == end, 则循环只执行一次, 返回一个以start数值为根的节点
        # 如果 start > end, 循环不执行, 直接返回空列表, (相当于递归结束)
        for i in range(start, end + 1):
            # 分别计算左右子树可能的根
            left_child_candidates = self.dfs_for_building_operation_tree(start, i - 1)
            right_child_candidates = self.dfs_for_building_operation_tree(i + 1, end)

            # 如果左或右子树为空, 则手动向其中插入一个None值, 否则后续的双重for循环无法执行
            if not left_child_candidates:
                left_child_candidates.append(None)
            if not right_child_candidates:
                right_child_candidates.append(None)

            # 通过左右子树不同的组合, 包括为None的情况, 来生成不同的root, 并将结果存入lst
            for left_child in left_child_candidates:
                for right_child in right_child_candidates:
                    root = TreeNode(i)
                    root.left = left_child
                    root.right = right_child
                    lst.append(root)
        return lst

    def extract_operators_numbers(self, s):
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

    def dfs_for_calculating_value(self, root):
        from operator import add, mul, sub
        numbers = self.numbers
        operators = self.operators
        op_mapping = {
            '+': add,
            '-': sub,
            '*': mul,
        }

        op_function = op_mapping[operators[root.value]]
        if root.left is None:
            valueL = numbers[root.value]
        else:
            valueL = self.dfs_for_calculating_value(root.left)

        if root.right is None:
            valueR = numbers[root.value + 1]
        else:
            valueR = self.dfs_for_calculating_value(root.right)

        result = op_function(valueL, valueR)

        return result

    def calculate(self, roots):
        results = []
        for root in roots:
            results.append(self.dfs_for_calculating_value(root))
        return results

    def diffWaysToCompute(self, input):
        """
        :type n: int
        :rtype: List[TreeNode]

        """
        self.numbers, self.operators = self.extract_operators_numbers(input)
        numbers = self.numbers
        operators = self.operators
        if not operators and numbers:
            the_only_number = numbers[0]
            return [the_only_number]

        # 以下两步, 我们可以合并成一步(即在构建树的同时返回结果), 此处分为两步, 方便理解
        '''
            以 "2*3-4*5" 为例
           *         *     *      -      *
            \       /     /      / \      \
             *     -     *      *   *      -
            /     /       \                 \
           -     *         -                 *
        '''

        # 构建树型结构, 一次dfs
        n = len(operators)
        roots = self.dfs_for_building_operation_tree(0, n - 1)

        # 根据不同的树型, 来分别计算最终的结果, 又一次dfs
        results = self.calculate(roots)
        return results


s = "2*3-4*5"
# s = "2-1-1"
# s = "0"
print Solution().diffWaysToCompute(s)
