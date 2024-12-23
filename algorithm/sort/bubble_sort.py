# 버블 정렬 리스트에서 가장 큰 값을 찾아서 마지막에 배치시키고
# 다음으로 큰 값을 찾아서 끝에서 두 번째에 배치....... 반복

def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-1):
            if nums[j] >= nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            
nums = [5,4,9,7,0,3,4,2,5,7,9,10,2,6,5]
bubbleSort(nums)
print(nums)