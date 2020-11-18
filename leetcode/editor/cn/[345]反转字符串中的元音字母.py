# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入："hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  输入："leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  元音字母不包含字母 "y" 。 
#  
#  Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_list = ['a', 'e', 'i', 'o', 'u',
                       'A', 'E', 'I', 'O', 'U']
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in vowels_list and s[right] in vowels_list:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels_list and s[right] in vowels_list:
                left += 1
            elif s[left] in vowels_list and s[right] not in vowels_list:
                right -= 1
            else:
                left += 1
                right -= 1

        return ''.join(s)


        
# leetcode submit region end(Prohibit modification and deletion)
