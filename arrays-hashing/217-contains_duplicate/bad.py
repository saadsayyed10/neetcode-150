nums1 = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

def badApproach(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i+1 ,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print("Duplicate found:", badApproach(nums1))