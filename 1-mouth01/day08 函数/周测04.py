"""返回字符串中第一个不重复的字符。
输入：ABCACDBEFD
输出：E"""

def identify(str1):
    xxx=list(str1)
    for item in xxx:
        giao = income.count(item)
        if giao ==1:
            return (item)

income="ABCACDBEFD"
result=identify(income)
print(result)

