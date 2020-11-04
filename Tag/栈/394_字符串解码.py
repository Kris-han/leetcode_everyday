# 2020-11-04 - 394. 字符串解码（01. 数组，栈，队列 ）
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#  
#
# 示例 1：
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"

# 示例 2：
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"

# 示例 3：
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"

# 示例 4：
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
思路
1、对字符串进行遍历，如果不是]的话，就把当前数放到栈中
2、首先判断是不是[，若果是[的话，那么就要吧前面的数字和字母分别用数组存起来放到栈中
3、如果是数字的话，就要先将默认的mui*10然后在+int(one),这么做是为了防止多个数字连续
4、如果是字母的话，则直接res += one
5、如果是]的话，就一次吧数据从栈中取出来，然后用上一次的数字和这次的字母向乘在+=上一个存储的字母
代码如下：

'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, mui = [], '', 0
        for one in s:
            if one == '[':
                stack.append([mui, res])
                res, mui = '', 0
            elif '0' <= one <= '9':
                mui = mui * 10 + int(one)
            elif one == ']':
                last_mui, last_res = stack.pop()
                res = last_res + int(last_mui) * res
            else:
                res += one
        return res

复杂度分析
时间复杂度O(n)
空间复杂度O(n)