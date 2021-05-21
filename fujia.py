#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: leaderboard_service
@file: fujia
@time: 2021/5/21 16:03
@IDE: PyCharm
@desc:
比较两个版本号 version1和 version2。
如果version1>version2返回1，如果version1<version2 返回 -1， 除此之外返回 0。
你可以假设版本字符串非空，并且只包含数字和. 字符。
. 字符不代表小数点，而是用于分隔数字序列。
例如，2.5 不是“两个半”，而是第二版中的第五个小版本。
你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。

示例1:
输入: version1 = "0.1", version2 = "1.1"
输出: -1
示例 2:
输入: version1 = "1.0.1", version2 = "1"
输出: 1
示例 3:
输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1
示例4：
输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
示例 5：
输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。

提示：
版本字符串由以点（.）分隔的数字字符串组成。这个数字字符串可能有前导零。
版本字符串不以点开始或结束，并且其中不会有两个连续的点。
"""


class Solution:
    def compareVersion(self, version1, version2):
        def strtonum(s):
            sum = 0
            for i in range(len(s)):
                sum = sum * 10 + int(s[i])
            return sum
        list1 = version1.split('.')
        list2 = version2.split('.')
        num1 ,num2 = [], []
        for word in list1:
            num1.append(strtonum(word))
        for word in list2:
            num2.append(strtonum(word))
        lenth = min(len(num1), len(num2))
        for i in range(lenth ):
            if num1[i] < num2[i]:
                return -1
            if num1[i] > num2[i]:
                return 1
        if len(num1) > len(num2):
            for i in range(len(num2), len(num1)):
                if num1[i] > 0:
                    return 1
            return 0
        if len(num1) < len(num2):
            for i in range(len(num1), len(num2)):
                if num2[i] > 0:
                    return -1
            return 0
        return 0



v1, v2 = "1.02.3", '1.002.4'
s = Solution()
print(s.compareVersion(v1, v2))