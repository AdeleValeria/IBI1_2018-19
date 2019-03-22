m = input("Give me a string of words:")
x = m.split()
#To backward
z = [z[::-1]for z in x]
#To sort (descending)
print(sorted(z, reverse=True))