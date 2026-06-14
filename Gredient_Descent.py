import numpy as np
import matplotlib.pyplot as plt
import math


y = np.array([3,6,4,8,9,12,16])
X = np.array([5,6,7,8,9,10,11])


m = 0
b = 0
alpha = 0.1
iteration = 1000
n = len(X)

for i in range(iteration):
    J = (1/n)*sum(((m*X+b)-y)**2)
    m = m- alpha*((2/n)*sum((m*X+b)-y))
    b = b- alpha*((2/n)*sum((m*X+b)-y))
    print('cost {} in {} iteration'.format(J,i))
print('m {} b {}'.format(m,b))

n = 5
a = 0
b = 0
learning_rate = 0.01
x = np.array([1,2,3,4,5])
y = np.array([5,8,11,14,17])
#plt.scatter(x,y,color = 'red')
for i in range(100):
    y_pred = a*x+b
    cost = (1/n)*sum([value**2 for value in (y-y_pred)])
    #plt.plot(x,y_pred,color = 'blue')
    plt.scatter(a,cost)
    da = -(2/n)*sum(x*(y-y_pred))
    db = -(2/n)*sum(y-y_pred)
    a = a-learning_rate*da
    b = b-learning_rate*db
    if(math.isclose(cost,0)):
        break

