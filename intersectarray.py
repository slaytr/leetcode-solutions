#Problem 349
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) >= len(nums2):
            long = nums1
            short = nums2
        elif len(nums2) > len(nums1):
            long = nums2
            short = nums1

        final = []
        for i in range(len(short)):
            if short[i] in final:
                pass
            else:
                if short[i] in long:
                    final.append(short[i])
        return final
        