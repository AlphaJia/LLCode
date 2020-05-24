# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 
# 
#  示例 1: 
# 
#  输入: 123
# 输出: 321
#  
# 
#  示例 2: 
# 
#  输入: -123
# 输出: -321
#  
# 
#  示例 3: 
# 
#  输入: 120
# 输出: 21
#  
# 
#  注意: 
# 
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
#  Related Topics 数学

'''
函数str()：将参数转换成字符串类型，即人适合阅读的形式
函数list()：创建一个list列表
函数int()：把一个字符串或者数字转换为【整型】

方法reverse()：反转列表元素的排列顺序
方法remove()：根据值删除元素
方法insert()：在列表中插入元素
方法join()：将序列中的元素（必须是str）以指定的字符连接生成一个新的字符串
'''


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x) #将整数转换成string类型，因为string可以转换成list
        a_list = list(a) # list可以反转 reverse
        a_list.reverse() # list反转 反序排列
        if a_list[0] == 0:
            a_list.remove(a_list[0])

        if a_list[-1] == '-':
            a_list.remove('-')
            a_list.insert(0, '-')

        y2 = ''.join(a_list)

        z = int(str(y2))
        if z < -2 ** 31 or z > 2** 31 -1:
            z = 0

        return z


# leetcode submit region end(Prohibit modification and deletion)
