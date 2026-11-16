# 二分查找

在有序数组中，找到第一个大于或等于 `target` 的位置。

## C++

```cpp
// 左闭右开区间 [left, right)
int lowerBound(const vector<int>& nums, int target) {
    int left = 0, right = nums.size();

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

使用时包含 `<vector>`，并使用 `std::vector` 或引入对应名称。

## Python

```python
def lower_bound(nums, target):
    """返回第一个大于或等于 target 的位置。"""
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

时间复杂度：O(log n)。空间复杂度：O(1)。
