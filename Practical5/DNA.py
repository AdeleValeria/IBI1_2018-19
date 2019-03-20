s = input("Give me a sequence of DNA: ")
DNA = {'A':s.count("A"), 'G':s.count("G"), 'C':s.count("C"), 'T':s.count("T")}
print (DNA)

import matplotlib.pyplot as plt
label = 'A', 'G', 'C', 'T'
sizes = [s.count("A"), s.count("G"), s.count("C"), s.count("T")]
explode = [0.05, 0.05, 0.05, 0.05]
colors = ['cyan', 'beige', 'orange', 'indigo']
plt.pie(sizes, labels=label, autopct='%1.1f%%', shadow=True, startangle=90, explode=explode, colors=colors)
plt.axis('equal')
plt.show()