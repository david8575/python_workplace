import time
def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
        print(f'{i}번 정렬{nums}')
        time.sleep(1)

nums = [5,4,9,7,0,3,4,2,5,7,9,10,2,6,5]
insertionSort(nums)