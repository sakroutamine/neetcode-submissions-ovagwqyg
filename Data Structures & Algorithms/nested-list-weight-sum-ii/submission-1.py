# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def depth(arr, level):
            maxD = level
            for i in arr:
                if not i.isInteger():
                    print()
                    maxD = max(maxD, depth(i.getList(),level+1))
            return maxD

        maxDepth = depth(nestedList, 1)

        def sumsFun(arr, level):
            sums = 0
            nonlocal maxDepth
            for i in arr:
                if not i.isInteger():
                    sums += sumsFun(i.getList(),level+1)
                else:
                    sums += i.getInteger() * (maxDepth - level + 1)
            return sums

        return sumsFun(nestedList,1)




