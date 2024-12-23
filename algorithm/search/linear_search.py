# 선형 탐색 linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True  
    return False