# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [], target = 0
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  0 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        num_row, num_column = len(matrix), len(matrix[0])

        left, right = 0, num_row * num_column - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if matrix[mid / num_column][mid % num_column] == target:
                return True
            elif matrix[mid / num_column][mid % num_column] > target:
                right = mid
            else:
                left = mid
        if matrix[left / num_column][left % num_column] == target or matrix[right/num_column][right%num_column] == target:
            return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
