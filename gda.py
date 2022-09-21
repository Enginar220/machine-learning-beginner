import numpy as np


"""Use the method of least squares to fit a line to the three given data points
(0,0),(1,2),(2,1)
"""
import numpy as np
#our objective is to fit the best representative line through the given data.
#hypothesis fuction y=m*x+n

def gr_ds(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.01

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {} , b {} , iteration {} ,cost  {}".format(m_curr,b_curr,i,cost))

#x= np.array([0,1,2])
#y= np.array([0,2,1])

#gr_ds(x,y)



def nor_eq(x,y):
    n=len(x)
    x.shape = (n,1)
    
    try:
        B=np.linalg.inv(x.transpose()*x)
        print(B)

    except(np.linalg.LinAlgError):
        print("Given data is not appropriate to use normal equation,you ought to use regularization.")

x= np.array([2,5,7])
y= np.array([0,2,1])

nor_eq(x,y)

        
    






