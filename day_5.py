# How would you reverse a list in-place without using the built-in reverse() method?

list1=[1,2,3,4,5,6,7,8]

def revers(List):

    first=0
    last=len(List)-1

    while first<last:
        List[first],List[last]=List[last], List[first]
        first+=1
        last -=1
    return List

x=revers(list1)
print(x)