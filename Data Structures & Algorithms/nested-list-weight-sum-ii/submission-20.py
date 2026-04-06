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
        def deep(arr,depth):
            maxD = 1
            for i in arr:
                if not i.isInteger():
                    maxD = max(maxD, deep(i.getList(),depth+1) +1)
            return maxD
        
        maxDepth = deep(nestedList,1)

        def summed(arr,depth, maxDepth):
            sums = 0
            for i in arr:
                if i.isInteger():
                    sums += i.getInteger() * (maxDepth - depth + 1)
                else:
                    sums += summed(i.getList(), depth+1, maxDepth)
            return sums

        return summed(nestedList,1,maxDepth)
        