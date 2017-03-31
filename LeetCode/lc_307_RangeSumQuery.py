class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = 0

    @classmethod
    def build_tree(cls, nums, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            root.sum = nums[start]
        else:
            mid = start + (end - start) / 2
            root.left = SegmentTreeNode.build_tree(nums, start, mid)
            root.right = SegmentTreeNode.build_tree(nums, mid + 1, end)
            root.sum = root.left.sum + root.right.sum
        return root

    def update_tree(self, pos, value):
        if self.start == self.end == pos:
            self.sum = value
        else:
            mid = self.start + (self.end - self.start) / 2
            if pos <= mid:
                self.left.update_tree(pos, value)
            else:
                self.right.update_tree(pos, value)

            self.sum = self.left.sum + self.right.sum

    @classmethod
    def sum_range(cls, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.sum
        mid = root.start + (root.end - root.start) / 2
        if end < mid:
            return SegmentTreeNode.sum_range(root.left, start, end)
        elif start > mid:
            return SegmentTreeNode.sum_range(root.right, start, end)
        else:
            return SegmentTreeNode.sum_range(root.left, start, mid) + \
                   SegmentTreeNode.sum_range(root.right, mid + 1, end)


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.length = len(nums)
        self.root = SegmentTreeNode.build_tree(nums, 0, self.length - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.root.update_tree(i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return SegmentTreeNode.sum_range(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
