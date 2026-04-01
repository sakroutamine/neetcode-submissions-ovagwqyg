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
        depth = 0
        def maxDepth(arr):
            level = 1
            for i in arr:
                if not i.isInteger():
                    
                    level = max(level, maxDepth(i.getList())+1)

            return level

        def sums(arr,level, depth):
            summed=0
            for i in arr:
                if i.isInteger():
                    summed += i.getInteger() * ((depth-level) + 1)
                    print(i.getInteger(), (depth-level) + 1,(i.getInteger() * (depth-level)))
                else:
                    summed += sums(i.getList(),level+1, depth)
            return summed

        depth = maxDepth(nestedList)
        sumAll = sums(nestedList,1, depth)
        return sumAll
        # def dfs(arr, level):
