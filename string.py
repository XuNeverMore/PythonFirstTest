#!/usr/bin/env python
# coding=utf-8
# 字符串或串(String)是由数字、字母、下划线组成的一串字符。
# 一般记为 :
# s="a1a2···an"(n>=0)
# 它是编程语言中表示文本的数据类型。
# python的字串列表有2种取值顺序:
# 从左到右索引默认0开始的，最大范围是字符串长度少1
# 从右到左索引默认-1开始的，最大范围是字符串开头
# 如果你要实现从字符串中获取一段子字符串的话，可以使用变量 [头下标:尾下标]，就可以截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。

char = 'ilovepython'
result = char[1:5]
print result
print result * 2
print result + " haha!"
print char[0:]
print char[0]
