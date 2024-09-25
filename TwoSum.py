# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
num = [2,7,11,15]
# target = int(input('enter the target value:'))
def Twosum(target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                print([i, j])


Twosum(17)

