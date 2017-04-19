from numpy import*
from sklearn.metrics import*

def sigmoid(T):
    n=T.shape[0]
    for i in range(n):
        T[i][0]=1.00/(1+exp(-1*T[i][0]) );
    return T

def cost(X,theta,y):
    z=X.dot(theta)
    z=sigmoid(z)
    m=y.shape[0]
    t=0
    s=[]
    for i in range(m):
        if z[i][0]>=0.50:
            if y[i][0]==1:
                t=t+1
            s.append(1)    
        else:
            if y[i][0]==0:
                t=t+1
            s.append(0)
        #print z[i],s[i],y[i][0]    
    print (t*1.0)/m
    return s

def computeCost(X,y,theta):
    m=X.shape[0]
    g=sigmoid(X.dot(theta))
    c=ones((m,1))
    c=(-1*y*(log(g))-(1-y)*log(1-g))
    a=c.sum()
    return a/m
                         
    
def normalization(X,XX):
    n=X.shape[1]
    for i in range(1,n):
        mu=X[:,i].mean()
        max1=X[:,i].max()
        min1=X[:,i].min()
        if max1-min1 >0.00001:
            XX[:,i]=(XX[:,i]-mu)/(max1-min1)
    return XX       

def graDescent(X,y,theta,alpha,num_it):
    m=y.shape[0]
    for i in range(0,num_it):
        z=X.dot(theta)
        g=sigmoid(z)
        theta=theta-( (alpha/m)*( X.conj().transpose().dot( g-y) ) )
        #print computeCost(X,y,theta)
    return theta

data=[]
yvalue=[]
with open("IONO.txt","r") as file1:
    for line in file1:
        temp=map( float,line.rstrip().split(',') )
        temp.insert(0,1)
        data.append(temp[:-1])
        yvalue.append([temp[-1]])
        


m=len(data)
n=len(data[0])
m1=int(.7*m)


X=array(data[:m1])
y=array(yvalue[:m1])
X_test=array(data[m1:m])
y_test=array(data[m1:m])


alpha=0.001
ite=1000
#print X
#X_test=normalization(X,X_test)
#X=normalization(X,X)


theta=zeros((X.shape[1],1))

theta=graDescent(X,y,theta,alpha,ite)

print "train cost %"
cost(X,theta,y)
print "train cost"
print computeCost(X,y,theta)
print "test cost"
print computeCost(X_test,y_test,theta)
print "test cost %"
c=cost(X_test,theta,y_test)
#print theta

p=[]
q=[]
for i in range(m-m1):
    p.append(int(y_test[i][0]))
    q.append(int(c[i]))
    
#print p
#print q    
aa=array(p)
bb=array(q)
#print "Classification Report: " + classification_report(aa,bb)



    
