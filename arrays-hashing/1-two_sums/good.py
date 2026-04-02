def goodApproach(nums: list[int], target: int) -> list[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

nums = [3, 4, 5 ,6]
target = 9

print(goodApproach(nums, target))