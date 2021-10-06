#WRITE YOUR CODE IN THIS FILE
#define function
#add parameters
def countA(x):
    x = x.lower()
    z = 0
    for i in range (0, len(x)):
        if x[i] == 'a':
            z = z + 1
    return z
#run function
print(countA("apple"))