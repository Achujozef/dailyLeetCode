#Create a function to count the frequency of each word in a given string and return the results as a dictionary.

def setCount(String):
    String=String.split()
    Dict={}
    for word in String:

        if word in Dict:
            x=Dict[word]
            Dict[word]=x+1
        else:
            Dict[word]=1
    return Dict
String='Create a function to count the frequency of each word in a given string and return the '

x=setCount(String)
print(x)