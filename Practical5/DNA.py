s = input("Give me a sequence of DNA: ")
DNA = {'A':s.count("A"), 'G':s.count("G"), 'C':s.count("C"), 'T':s.count("T")}
print (DNA)

import matplotlib.pyplot as plt
label = 'A', 'G', 'C', 'T', 'U'
sizes = [s.count("A"), s.count("G"), s.count("C"), s.count("T"), s.count("U")]
explode = [0.05, 0.05, 0.05, 0.05, 0.05]
colors = ['cyan', 'beige', 'orange', 'indigo', 'gray']
plt.pie(sizes, labels=label, autopct='%1.1f%%', shadow=True, startangle=90, explode=explode, colors=colors)
plt.axis('equal')
plt.show()

#bar graph
import numpy as np
import matplotlib.pyplot as plt
N = 5
x = (s.count("A"), s.count("G"), s.count("C"), s.count("T"), s.count("U"))
ind = np.arange(N)
width = 0.5
p1 = plt.bar(ind, x, width)
plt.ylabel('Total')
plt.xticks(ind, ('A', 'G', 'C', 'T', 'U'))
plt.yticks(np.arange(0, 20, 2))
plt.show