m = input("Give me a string of words:")
x = m.split()
#To backward
y = [z[::-1]for z in x]
#To sort (descending)
print(sorted(y, reverse=True))