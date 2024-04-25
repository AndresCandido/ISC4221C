# -*- coding: utf-8 -*-
"""HW4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zaw9RlDx5NG230yGATdxCSccVEuHvbXU
"""

# ISC4221 - Homework 4
# by: Andres Candido
# Problem 1: Parts A and B

import numpy as np
from scipy.spatial import distance
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

X = np.array([[1,2],[-4,-2],[3,3],[5,6],[-3,-1],[-5,-3],
              [5,4],[6,8],[-5,-2],[-1,-2]])

Y = distance.pdist(X, 'euclidean')
print("distance bewteen all points: \n", Y)

print("\n")

Z = hierarchy.linkage(Y, method='single', metric='euclidean')
hierarchy.dendrogram(Z)
plt.show()

# Problem 1: Part C

Z = hierarchy.linkage(Y, method='complete', metric='euclidean')
hierarchy.dendrogram(Z)
plt.show()

"""Part C (cont.): compare it with the  single linkage clustering and discuss the key difference between them. (10 points)

As we can see from the two generated dendrograms, complete and single linkage clustering generate the same clusters (same points in each cluster) but they differ in determining which individual point is closer to one another.

"""

# Problem 2:

import random

def Rand(start, end, num):
    list1 = []
    list2 = []

    for j in range(num):
        list1.append(random.randint(start, end))
        list2.append(random.randint(start, end))

    combine = list(map(list, zip(list1, list2)))
    return combine

# Driver Code
num = 20
start = -5
end = 5

# Generate 20 points randomly in the [-5,5] × [-5,5] domain
points = Rand(start, end, num)
print(points, '\n')
points = np.array(points)


# use Python’s voronoi() function to draw the Voronoi diagram.
from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
plt.show()

"""Problem 3:

Part a:

Class: + and -

p(+)= 4/9 = 0.444

p(-)= 5/9 = 0.556

Gini(t) = 1 - (0.444^2 + 0.556^2) = 0.4937

Entropy(t) = -((.444*log _(2)(.444))+(.556*log _(2)(.556))) = 0.991

Problem 3:

Part b:

Atribute A: T and F

p(T)= 4/9 = 0.444

p(F)= 5/9 = 0.556

Entropy(t) = -((.444log _(2)(.444))+(.556log _(2)(.556))) = 0.991

Information gain = 0.991 - ((4/9)*0.991 + (5/9)*0.991) = 0  

Atribute B: T and F

p(T)= 5/9 = 0.556

p(F)= 4/9 = 0.444

Entropy(t) = -((.556log _(2)(.556))+(.444log _(2)(.444))) = 0.991

Information gain = 0.991 - ((4/9)*0.991 + (5/9)*0.991) = 0

Problem 3:

Part c:

Atribute C: Less than 3, between 3 and 6, greater than 6

p(Less than 3) = 1/9 = 0.111

p(between 3 and 6) = 5/9 = 0.556

p(greater than 6) = 3/9 = 0.333

Entropy(t) = -((.556log _(3)(.556))+(.111log _(3)(.111))+(.333log _(3)(.333))) = 0.8525

Information gain = 0.991 - ( (1/9)0.8525 + (5/9)0.8525 + (3/9)0.8525 ) = 0.1385

Problem 3:

Part d:

Seeing that the information gain was the largest when using atribute C (0.1385), we can determine that atribute C is the attribute to split the root node.

Next, we divide the two child nodes atribute A and B. Since the information gain of atribute A and B was 0. We don't need to split the tree any further.

It would look something like this:

![Screenshot 2022-11-30 212214.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABNCAYAAAAW92IAAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQuSURBVHhe7ZtNSFRRFMeP2fjRaI2hlkwWmSUqpNhUZkWNuKhFFJRQRMs20Qct2lSraCOB0Qdt2hVRUC0iaCVZVPZlYZJffUyUDVZaTuqUNkr5v55nA2m+N765E937g8d5c+fd57z/Pfecw7vXuNLS0p+kMFPYKosWgK2yaAHYKosWgK2yKC+ArYVQQdZM2rmqkBKnxovPFx610b3XHeJ8IsL7DgwO0dm7TdTc8YW/jR62C7DVs5BO1j6jrr5+bv3NygVZtH1Znjgf7yHTU5Jor7eILtW/lCKAtCmwpSRXHKdvNdKui7fo8LX7tGRuBjkTpvIVsUGKABhVz7xMuvL01eioBn8M0vmHbcLGEikC5M1KE7btY7ew/xI6DbJVFikCdH8bEOnNmAr/ElIEQODzdfXQhsXzRUAEiP47luepkQXAqeHawB8I0pENpXRm21o6unEFPXnXqUYWMIAIqAFw7L98R0qhMxE6CLK1jdSkhFE3R+lrFpTRxytXi764hyz0W2G2yqIFYKssWgC2yhI1ASoqKqi6upoKCwu5ZXzcbjdVVVVRZWUlt8gjagKUlZWRz+ejpqYmbhkfv99P9fX1lJ+fzy3yiIoAGHWn00m1tbXcMjHNzc3kcrmE58gkKgJ4vV4KBoOmRt8A18Jj4DkysV0AjH5OTg7V1dVxi3laW1uFF5iJG3ZhuwAFBQUUCoWopaWFW8xTU1NDgUBAeJAsbBUA0dzj8YiAhsAWCRAuOztb3EsGtgqAKO5wOERAixRj6siKBbYKYCX1jQc8p729XVpKtE0ABC4EMASyyYL0KSsl2iYAAhcCGALZZJGZEvULEbbKogVgqyxaALbKogVgqyx/1AF7vEWUP3tkGft9dx+duNlgegETe4DK8+aIc6t9sUq8r7yY5qSliM8tH7rFWqJZwn+3lb5jCtDxNSj284yFsdPrb38E16xZ6I5IgNsv/X9srQsXFvxtGx2uzZrhNC2A5SlQMjeTbjx/S6mJjtG1fhnAow5cvStWliHQpqIcW/YWWBIAD5wxfPi6vlLvQChmOz4w8kmOeEqWLQAeuD80RG8/94hpAm+IBVhJ7uzrH3MzplUsCYAHfvEpIOY1RgHeIGsaIDge27xKLLtjz+HFx238zeQwLYDh/kbggRfAG2RNg/AYcL3xDR1av1R4wmQxLQAeND0lmXavXSxGAaOBUYnFNGho76TO3u+UNi2RWyLHtABILUh9xh4fHNgN7nY5pWYDUJydQdOTE2zZeWpKAKSbRZkuevruE7eMYPwAGdMgPAYg15970GpLELRcCJnB7kLIClEvhP43xhQAZSdc7eA6j6VqC+qjn/FPEZGAvrgHPNEKuB79wktmM+iXomyVRQvAVlm0AGyVRQvAVlm0AGyVRQvAVlm0AGyVRQvAVlnicnNzfw7DH1WD6BchOKjOSdZUeQAAAABJRU5ErkJggg==)
"""