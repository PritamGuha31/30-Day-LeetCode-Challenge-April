# Day 10
# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        min = self.items[0]
        
        for item in self.items:
            if item < min:
                min = item
        
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()