
'''
    打印
    *******
     *****
      ***
       *
      ***
     *****
    *******
'''
'''
# 第一步打印倒三角形
# starsCount = lineCount - spaceCount
# spaceCount = lineCount * 2
lineCount = 0
while lineCount <= 4:
    print(' '* lineCount,end = '')
    starsCount = 0
    while starsCount < 7 - lineCount * 2:
        print('$',end = '')
        starsCount += 1
    print('')
    lineCount += 1
# 第二步打印正三角形
while lineCount >= 0:
    lineCount -= 1
    print(' '* lineCount,end = '')
    starsCount = 0
    while starsCount < 7 - lineCount * 2:
        print('$',end = '')
        starsCount += 1
    print('')
'''
# 合并倒三角和正三角

lineCount = 7
starsCount = 0
spaceCount = 0
middleLine = 0
lineNum = 0
while lineNum < lineCount:
    if linenum < middleLine:
        spaceCount = lineNum
    else:
        spaceCount -= 1
    starsCount = lineCount - lineNum * 2
    #打印一行开头的空格和$
    print(' '*spaceCount,end='')
    starsNum = 0
    while starsNum < starsCount:
        print('$'*starsNum,end='')
        starsNum += 1



