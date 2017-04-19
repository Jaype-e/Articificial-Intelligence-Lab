from numpy import*
from sklearn.metrics import*
def computeCost(X,y,theta):
    m=X.shape[0]
    c=ones((y.shape[0],1))
    c=X.dot(theta)-y
    return (c**2).sum()/(2*m*1.0)
    
def normalization(X,XX):
    n=X.shape[1]
    for i in range(1,n):
        mu=X[:,i].mean()
        sigma=X[:,i].std()
        XX[:,i]=(XX[:,i]-mu)/sigma
    return XX       
    
    
def graDescent(X,y,theta,alpha,num_it):
    m=y.shape[0]
    for i in range(0,num_it):
        theta=theta-( (alpha/m)*( X.conj().transpose().dot( X.dot(theta)-y) ) )
        #print computeCost(X,y,theta)
    return theta



data=[]
yvalue=[]
with open("data11.txt","r") as file1:
    for line in file1:
        temp=map( float,line.rstrip().split(',') )
        temp.insert(0,1)
        data.append(temp[:-1])
        yvalue.append([temp[-1]])
        

m=len(data)
n=len(data[0])

m1=int(0.7*m)
X=array(data[:m1])
y=array(yvalue[:m1])

X_test=array(data[m1:m])
y_test=array(yvalue[m1:m])

theta=zeros((X.shape[1],1))


alpha=0.01
ite=10000
#X_test=normalization(X,X_test)
#X=normalization(X,X)


theta=graDescent(X,y,theta,alpha,ite)
print "cost on training data",computeCost(X,y,theta)
print "cost on testing data",computeCost(X_test,y_test,theta)
print theta

c=X_test.dot(theta)
print "mean absolute error"
print mean_absolute_error(y_test,c)
import math
print math.sqrt(mean_squared_error(y_test,c))    
