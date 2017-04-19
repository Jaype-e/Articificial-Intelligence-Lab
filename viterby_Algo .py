data=[]
tag=['b','f','c']
dic={'wordname':'something'}
Numtag={}
inicialtag={}
tag=[]
with open('tag.txt','r') as file2:
	for l in file2:
		tag.append(l.rstrip())

for j in tag:
	dic[j]=0
        inicialtag[j]=0

tagdata=[]
temp=1



with open('com_train.txt','r') as file1:
	for l in file1:
		if len(l)>=2:
			data.append(l.rstrip().split())
			tagdata.append(l.rstrip().split()[1])
			if temp==1:
				inicialtag[l.rstrip().split()[1]]=inicialtag[l.rstrip().split()[1]]+1
				temp=0
		else:
			temp=1
			tagdata.append(' ')

data.sort()




for ll in tag:
	Numtag[ll]=tagdata.count(ll)

#print Numtag
#print inicialtag

#calculating inicial probability
summ=0
for ll in tag:
	summ=summ+inicialtag[ll]

inicialprob={}

for ll in tag:
	inicialprob[ll]=round((1.00*inicialtag[ll])/summ,5)

#print inicialprob


length=len(data)
matrix={}
for i in xrange(length):
	if data[i][0]!=dic['wordname']:
		dii={}
		for j in tag:
			if j!='wordname':
				dii[j]=dic[j]			
 		matrix[dic['wordname']]=dii
		dic={'wordname':data[i][0]}
		for j in tag:
			dic[j]=0

	if data[i][0]==dic['wordname']:
		dic[data[i][1]]=dic[data[i][1]]+1
	if i==length-1:
		dii={}
		for j in tag:
			if j!='wordname':
				dii[j]=dic[j]			
 		matrix[dic['wordname']]=dii
		



#calculating emmision probability matrix		

for i in matrix:
	for ll in tag:
		matrix[i][ll]=(matrix[i][ll]*1.00)/Numtag[ll]
			
#print matrix

			
#calculation of transition probability matrix
tra_mat={}
for ll in tag:
	Dic={}
	for jj in tag:
		Dic[jj]=0
        tra_mat[ll]=Dic


kk=len(tagdata)

for i in xrange(1,kk):
	if tagdata[i-1]!=' ' and tagdata[i]!=' ':
		tra_mat[tagdata[i-1]][tagdata[i]]=tra_mat[tagdata[i-1]][tagdata[i]]+1


sumtag={}
for ll in tag:
	summ=0
	for jj in tag:
		summ=summ+tra_mat[ll][jj]
	sumtag[ll]=summ

for ll in tag:
	for jj in tag:
		tra_mat[ll][jj]=(tra_mat[ll][jj]*1.00)/sumtag[ll]
	

"""print "      ",
for ll in tag:
	print ll+" ",
print " "
for ll in tag:
	print ll+" ",
	for jj in tag:
		print tra_mat[ll][jj],
        print "\n"
"""

# tarnsition matrix : tra_mat
# tag
# inicialprob  as dictinory
# matrix (emmision matrix) matrix[word][tag]=???

listt=[]
with open('test1.txt','r') as file1:
	for l in file1:
		if l:
			listt.append(l.rstrip())


#viterby implimentation 

l_sen=len(listt)
l_tag=len(tag)

#inicilisation of dp
dp=[]
for i in xrange(l_tag):
	llll=[]
	for j in xrange(l_sen):
		llll.append(0) 
	dp.append(llll)

for i in xrange(l_tag):
	dp[i][0]=inicialprob[tag[i]]*matrix[listt[0]][tag[i]]

pre=[]
for i in xrange(l_tag):
	llll=[]
	for j in xrange(l_sen):
		llll.append(0) 
	pre.append(llll)


for i in xrange(l_tag):
	pre[i][0]=i


for j in xrange(1,l_sen):
	for i in xrange(l_tag):
		for k in xrange(l_tag):
			if dp[k][j]<dp[i][j-1]*matrix[listt[j]][tag[k]]*tra_mat[tag[i]][tag[k]] :
				dp[k][j]=dp[i][j-1]*matrix[listt[j]][tag[k]]*tra_mat[tag[i]][tag[k]]
				pre[k][j]=i


var=0
temp=0
for i in xrange(l_tag):
	if dp[i][l_sen-1]>var:
		temp=i
		var=dp[i][l_sen-1]
ans=[]
for j in xrange(l_sen):
	ans.append(tag[temp])
	temp=pre[temp][l_sen-1-j]

for j in xrange(len(ans)-1,-1,-1):
	print listt[len(ans)-1-j] +" : " +ans[j]	


















