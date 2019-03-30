#Practical 5

#Input a sequence of DNA
#Use .upper to capitalize the letters
valid_dna = "ACGT"
s = input("Give me a sequence of DNA:")
check = all(i in valid_dna for i in s)
if check is True:
#s = input("Give me a sequence of DNA: ").upper()

#To count the total of each nucleobase appearing in the sequence
    DNA = {'A':s.count("A"), 'G':s.count("G"), 'C':s.count("C"), 'T':s.count("T")}
    print(DNA)
#Pie chart
    import matplotlib.pyplot as plt
    label = 'A', 'G', 'C', 'T'
    sizes = [s.count("A"), s.count("G"), s.count("C"), s.count("T")]
    #To offset a slice
    explode = [0.05, 0.05, 0.05, 0.05]
    colors = ['cyan', 'beige', 'orange', 'indigo']
    #autopct to determine how the percentage is shown. 1f%% means 1 number after the decimal, if 2f%%, then two numbers.
    plt.pie(sizes, labels=label, autopct='%1.1f%%', shadow=True, startangle=90, explode=explode, colors=colors)
    plt.axis('equal')
    plt.show()
    
    
    #bar graph
    import numpy as np
    import matplotlib.pyplot as plt
    N = 4
    x = (s.count("A"), s.count("G"), s.count("C"), s.count("T"))
    ind = np.arange(N)
    width = 0.5
    p1 = plt.bar(ind, x, width)
    plt.ylabel('Total')
    plt.xticks(ind, ('A', 'G', 'C', 'T'))
    #20 is the max number on the y axis and 2 determines the repetition of the point on y axis. In this case, there will be point at 2,4,6,8,10 and so on.
    plt.yticks(np.arange(0, 20, 2))
    plt.show

else:
    print("Invalid DNA sequence. Ensure the sequence only consists of A, G, C and T")