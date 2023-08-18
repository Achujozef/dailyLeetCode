#int reverse

def rev(wordx):
    word=str(wordx)
    word=list(word)
    first=0
    last=len(word)-1
    m=''
    for i in range(len(word)):
        if 0>=first < last:
            word[first],word[last]=word[last],word[first]
    print(word)
    num = m.join(word)
    return int(num)
x=rev(123)
print(x)