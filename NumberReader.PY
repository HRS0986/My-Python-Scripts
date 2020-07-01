from math import floor

words1 = [ "","one","two","three","four","five","six","seven","eight","nine" ]
words2 = [ "","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen" ]
words3 = [ ""," ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety" ]
words4 = [ "","hundred","thousand","million" ]

n = int(input('Enter Number to read: '))

B1 = floor(n/100000000)      
B2 = floor(n/10000000)        
B3 = floor(n/1000000)       
B4 = floor(n/100000)
B5 = floor(n/10000)
B6 = floor(n/1000)
B7 = floor(n/100)
B8 = floor(n/10)

b = B2 - B1*10        
c = B3 - B2*10         
d = B4 - B3*10         
e = B5 - B4*10
f = B6 - B5*10
g = B7 - B6*10
h = B8 - B7*10
i = n - B8*10

nm = []

if (n == 1000000000):
    print('one billion')
elif (n == 0):
    print("zero")
elif (n>1000000000):
    print ("Error: VALUE TOO LARGE!!!!")
else:
    if (B1 != 0):
        nm.append(words1[B1])
        nm.append(words4[1])
    if (b != 0):
        if (b ==1):
            nm.append(words2[c])
        else:
            nm.append(words3[b])
    if (c != 0):
        nm.append(words1[c])

    if (B1 != 0 or b != 0 or c != 0):
        nm.append(words4[3])

    if (d != 0):
        nm.append(words1[d])
        nm.append(words4[1])
    if (e != 0):
        if (e == 1):
            nm.append(words2[f])
        else:
            nm.append(words3[e])
    if (f != 0):
        nm.append(words1[f])

    if (d != 0 or e != 0 or f != 0):
        nm.append(words4[2])

    if (g != 0):
        nm.append(words1[g])
        nm.append(words4[1])
    if (h != 0):
        if (h == 1):
            nm.append(words2[i])
        else:
            nm.append(words3[h])
    if (i != 0):
        nm.append(words1[i])

    # delete one,two,three,...,nine if eleven,twelve,...,nineteen exist
    if (b == 1 and B1 == 0): 
        del nm[1]
        if (e == 1 and d == 0):
            del nm[3]
            if (h == 1 and g == 0):
                del nm[5]
            elif ( h == 1 and g != 0):
                del nm[7]

        elif(e ==1 and d != 0):
            del nm[5]
            if (h == 1 and g == 0):
                del nm[7]
            elif ( h == 1 and g != 0):
                del nm[9]

    elif (b == 1 and B1 != 0):
        del nm[3]
        if (e == 1 and d == 0):
            del nm[5]
            if (h == 1 and g == 0):
                del nm[7]
            elif ( h == 1 and g != 0):
                del nm[9]

        elif(e ==1 and d != 0):
            del nm[7]
            if (h == 1 and g == 0):
                del nm[9]
            elif ( h == 1 and g != 0):
                del nm[11]

    ans = ' '.join(nm)
    print(ans.title())
    
# Test Cases
# 012013014
# 012013514
# 012513014
# 012513814
# 712013014
# 712013614
# 712813014
# 712813514
# 000000001
# 000000000
# 999999999
# 987654321
# 000000100
# 1000000000

    
