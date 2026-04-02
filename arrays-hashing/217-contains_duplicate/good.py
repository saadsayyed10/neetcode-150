nums1 = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

def goodApproach(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

print("Duplicate found:", goodApproach(nums1))