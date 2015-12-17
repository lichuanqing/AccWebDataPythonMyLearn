import re

hand=open('regex_sum_206170.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    temp=re.findall('[0-9]+',line)
    if len(temp) !=0:
        for num in temp:
            numlist.append(num)
            
sum1=0
for num in numlist:
    sum1=sum1+int(num)
print 'There are' ,len(numlist),'values with a sum=',sum1

##print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
