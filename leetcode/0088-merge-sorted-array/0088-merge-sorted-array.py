class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # num1 숫자의 맨 끝
        idx1 = m-1
        
        # num2 숫자의 맨 끝
        idx2 = n-1
        
        # merge할 num1의 맨 끝
        idx3 = len(nums1)-1
        
        if idx2 < 0:
            return 
        
        while(idx1>=0 and idx2>=0):
            a = nums1[idx1]
            b = nums2[idx2]
            
            if a>=b:
                nums1[idx3] = a
                idx1-=1
                idx3-=1
            
            else:
                nums1[idx3] = b
                idx2-=1
                idx3-=1
        print(idx2,idx3)
        while(idx2>=0):
            nums1[idx3] = nums2[idx2]
            idx2-=1
            idx3-=1
            