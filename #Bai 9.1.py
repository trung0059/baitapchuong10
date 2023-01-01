def sign(x):
    if x<0: x=-1
    if x>0: x=1
    if x==0: x=0
    return str(x)
print(sign(4))
import math
s = lambda x,n: math.pow(math.pow(x,2)+1,n)
print("s=",s(3,4))