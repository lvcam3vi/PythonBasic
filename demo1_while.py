'''
num = 1
while num <= 10:
    print('%d'%num)
    num+=1
'''
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


