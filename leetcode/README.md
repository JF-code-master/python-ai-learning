# 算法练习

一个文件一道题，按「题号_题目名」命名，方便按题号排序和检索：

- `0001_two_sum.py`
- `0002_add_two_numbers.py`

这个文件夹里的 `0001_two_sum.py` 是之前留的空文件，建议改名成上面这种格式再写，或者直接删掉。

单题文件保持这个结构，既能本地调试也方便贴回 LeetCode：

```python
class Solution:
    def two_sum(self, nums, target):
        ...


if __name__ == "__main__":
    print(Solution().two_sum([2, 7, 11, 15], 9))
```
