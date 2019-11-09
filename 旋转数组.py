'''
在已知升序排列数组，在某个点旋转
0,1,2,3,4,5,6  ->  3,4,5,6,0,1,2
搜索给定的目标值，存在返回索引，不存在返回-1
时间复杂度O(log n)
'''

'''
思路：
1. 采用二分法
2. 利用中点划分数组为两部分
3. 一部分为完全升序排列，直接交换边界二分
   另一侧利用else划定边界二分
'''

def main():
    a = [4,5,0,1,2,3]
    t = -1
    print(spin(a,t))
def spin(arr,target):
    left = 0
    right = len(arr)-1

    while left<=right:
        mid = (left + right) // 2
        #print(left, mid, right)
        #print(arr[left], arr[mid], arr[right])
        if arr[mid] == target:
            return mid

        if arr[mid] < arr[right]:
            if arr[mid] <= target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1
if __name__ == '__main__':
    main()