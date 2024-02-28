#Riley Pollard
# Lab thursday 2pm, Wednesday Class

def in_order(nums):
    # Type your code here.
    condition = True
    for i in range(0, len(nums)-1,1):
          if nums[i] > nums[i+1]:
              condition = False
    return condition



if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
