# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  说明：你不能倾斜容器，且 n 的值至少为 2。 
# 
#  
# 
#  
# 
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  
# 
#  示例： 
# 
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
#  Related Topics 数组 双指针 
#  👍 1720 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # method1: 粗暴法，两次遍历，但是会超时
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         max_area = max(max_area, min(height[i], height[j]) * (j - i))
        #
        # return max_area

        # method2:双指针法, 刚开始时左右指针分别在最左侧和最右侧。移动哪一个指针是哪一个数字小
        max_area = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            max_area = max(min(height[i], height[j]) * (j - i), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area



# leetcode submit region end(Prohibit modification and deletion)
