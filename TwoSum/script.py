def twoSum(nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
int_list = [2,7,11,15]
target = 18

result = twoSum(int_list, target)

for x in result:
    print(x)