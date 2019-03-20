m = input("Give me a string of words:")
x = m.split()
x.reverse()
y = [z[::-1]for z in x]
print(sorted(y, reverse=True))