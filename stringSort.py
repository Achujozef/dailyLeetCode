hello="this repository moved. please use the new location"
splited_string= hello.split()
sorted_words=sorted(splited_string, key=lambda x:(len(x),x))
sorted_string=' '.join(sorted_words)
print(sorted_string)