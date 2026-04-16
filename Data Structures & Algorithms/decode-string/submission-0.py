class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        st = ""
        counter = ""

        for i in s:
            if i in "0123456789":
                counter +=i
            elif i == "[":
                stack.append([st,counter])
                st = ""
                counter=""
            elif i == "]":
                popped=stack.pop()
                if int(popped[1])>0:
                    st = popped[0]+st*int(popped[1])
                else:
                    st+=popped[0]
            else:
                st += i
        return st