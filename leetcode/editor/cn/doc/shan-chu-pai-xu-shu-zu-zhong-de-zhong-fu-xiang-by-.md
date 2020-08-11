#### 方法：双指针法

**算法**

数组完成排序后，我们可以放置两个指针 *i* 和 *j*，其中 *i* 是慢指针，而 *j* 是快指针。只要 *nums[i] = nums[j]*，我们就增加 *j* 以跳过重复项。

当我们遇到 ![nums\[j\]\neqnums\[i\] ](./p__nums_j__neq_nums_i__.png)  时，跳过重复项的运行已经结束，因此我们必须把它（*nums[j]*）的值复制到 *nums[i + 1]*。然后递增 *i*，接着我们将再次重复相同的过程，直到 *j* 到达数组的末尾为止。

```java [q797kMcS-Java]
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
```


**复杂度分析**

* 时间复杂度：*O(n)*，假设数组的长度是 *n*，那么 *i* 和 *j* 分别最多遍历 *n* 步。

* 空间复杂度：*O(1)*。