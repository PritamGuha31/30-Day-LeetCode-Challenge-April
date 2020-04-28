# Day 28
# First Unique Number

# You have a queue of integers, you need to retrieve the first unique integer in the queue.

# Implement the FirstUnique class:

# FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
# int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
# void add(int value) insert value to the queue.

# Input: 
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
# [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output: 
# [null,2,null,2,null,3,null,-1]

# Explanation: 
# FirstUnique firstUnique = new FirstUnique([2,3,5]);
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(5);            // the queue is now [2,3,5,5]
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(2);            // the queue is now [2,3,5,5,2]
# firstUnique.showFirstUnique(); // return 3
# firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
# firstUnique.showFirstUnique(); // return -1

class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = []
        self.dict = dict()
        
        for num in nums:
            
            if num in self.dict:
                self.dict[num] += 1
            else :
                self.nums.append(num)
                self.dict[num] = 1

    def showFirstUnique(self):
        """
        :rtype: int
        """
        
        while(True):
            if len(self.nums) == 0:
                return -1
            elif self.dict[self.nums[0]] > 1:
                self.nums.pop(0)
            else:
                return self.nums[0]
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.nums.append(value)
            self.dict[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)