# is palindrome


def pali(num):
    num=str(num)
    for i in range(len(num)):

        if num[i]!=num[(len(num)-i)-1]:
            return False
    return True
        
print(pali(121))