

#######################################################################################################
import math

#######################################################################################################
# sigmoid
def sigmoid(x):
    y = 1.0/(1 + math.exp(-x)) #Include math module
    print(y)
    return y

if __name__ == '__main__':
    sigmoid(1)
#######################################################################################################       
# tanh
def tanh(x):
    y = (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))  # Include math module
    print(y)
    return y

if __name__ == '__main__':
    tanh(0.25)
#######################################################################################################
# Relu
def relu(x):
    if x>0:
        print(max(0,x)) #Why? Task.
        return max(0,x)
    else:
        print(0)
        return 0

if __name__ == '__main__':
    #relu(5)
    relu(-300)
#######################################################################################################    
#leaky_relu
def leaky_relu(x):
    if x>0:
        print(max(0,x)) #Why? Task.
    else:
        print(0.01*x)


if __name__ == '__main__':
    leaky_relu(-300)
#######################################################################################################    
#elu
import numpy as np
def elu(x):
    #alpha = 1.0 #Hyperparameter, can be of any value
    alpha = 0.7
    if x>0:
        print(max(0,x)) #Why? Task.
    else:
        print(alpha * (np.exp(x) - 1))


if __name__ == '__main__':
    elu(-100)
#######################################################################################################
