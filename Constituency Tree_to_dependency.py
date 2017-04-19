from copy import deepcopy

temp=""
with open("input.txt","r") as file1:
	for l in file1:
		temp=temp+l

pcfg=""
for c in temp:
	if c=='(':
		pcfg=pcfg+c
		pcfg=pcfg+' '
	elif c==')':
		pcfg=pcfg+' '
		pcfg=pcfg+c
	else :
		pcfg=pcfg+c

#print pcfg	

pcfglist=pcfg.split()

print pcfglist	


# strat class 
head_Node={'DT':['DT'],'NP':['NP','NN','PRP','NNS','NNP'],'S':['VP'],'VP':[ 'VP','VB','VBG','VBD','VBZ','VBN','VBP'],'ADJP':['JJ','PP'],'PP':['NP'],'ROOT':['S'],'PRT':['RP']}

class GraphNode:
    def __init__(self,data): # label is an int, data is DT,VB etc.
        self.data = data
        self.children = None
        self.head = None #to update the head based on rules

    def add_child(self,child): # Child is an object of type GraphNode
        if not self.children:  # No Child
            self.children = list()
        self.children.append(child)

    def check_child(self,test_object):
        return test_object in self.children

class DepGraph:
    def __init__(self,head): # label is an int, data is DT,VB etc.
        self.head = head
        self.children = None
        self.karak = None #to update the head based on rules

    def add_child(self,child): # Child is an object of type GraphNode
        if not self.children:  # No Child
            self.children = list()
        self.children.append(child)

    def check_child(self,test_object):
        return test_object in self.children


def prepcfg(root,t):
	for j in xrange(t):
		print '\t',
	print root.data,root.head

	if root.children==None:
		return
	t=t+1	
	for i in root.children:

		prepcfg(i,deepcopy(t))		

def dependency(deproot,root):
	if root.children != None:
		for j in root.children:
			if j.head == deproot.head :
				dependency(deproot,j)
			else:
				child=DepGraph(j.head)
				deproot.add_child(child)
				dependency(child,j)

karaka=dict()

def karak(root):
	global karaka
	child=root.children[0]
	if len(child.children)==1:
		child=child.children[0]
		flag=0
		if child.children!=None:
			while True :
				for j in child.children:
					if j.data=='VP':
						flag=2
						child=j
						break
					elif j.data=='NP':
						karaka[j.head]="K2"
					elif j.data=='PP':
						for ch in j.children:
							if ch.head=='to':
								karaka[j.head]="K4"
							elif ch.head=='with' or ch.head=='by':
								karaka[j.head]="K3"
							elif ch.head=='from':
								karaka[j.head]="K5"
							elif ch.head=='in' or ch.head=='at' or ch.head=='on' or ch.head=='over':
								karaka[j.head]="K7"
					flag=0				
				if flag==0:
					break				
	else:
		NpChild=child.children[0]

		child=child.children[1]
		flag=0
		passive=False
		pp=True
		if child.children!=None:
			if child.children[1].data=="VP":
				GrandChild=child.children[1]
				if GrandChild.children[0].data=='VBN' or GrandChild.children[0].data=='VBD':
					print "a"
					passive=True
			if child.children[0].head=="has" or child.children[0].head=="have" or child.children[0].head=="had" :
				passive=False		
			print passive		

			while True :
				for j in child.children:
					if j.data=='VP':
						flag=2
						child=j
						break
					elif j.data=='NP':
						pp=False
						karaka[j.head]="K2"
					elif j.data=='PP':
						for ch in j.children:
							if ch.head=='to' or ch.head=='for':
								karaka[j.head]="K4"
							elif ch.head=='with' or ch.head=='by':
								if passive == True:
									karaka[j.head]="K1"
								else:	
									karaka[j.head]="K3"
							elif ch.head=='from':
								karaka[j.head]="K5"
							elif ch.head=='in' or ch.head=='at' or ch.head=='on' or ch.head=='over':
								karaka[j.head]="K7"
					elif j.data=='S':
						karaka[j.head]="K4"			
					flag=0											
				if flag==0:
					break	
		if passive==False:
			karaka[NpChild.head]="K1"
		else:
			if pp == True:
				karaka[NpChild.head]="K2"
			else:
				karaka[NpChild.head]="K4"	

	

def treebuild(lst):
	level=0
	l=len(lst)
	#print l
	if l==4:
		#print lst[1]
		cur_rot=GraphNode(lst[1])
		cur_rot.head=lst[2]
		return cur_rot
	lst1=[]
	root=GraphNode(lst[1])
	for t in range(2,l-1):
		lst1.append(lst[t])
		if lst[t]=='(':
			level=level+1
		elif lst[t]==')':
			level=level-1
			if level==0:
				#print "in level 0"
				lst2=deepcopy(lst1)
				#print lst2
				cur_root=treebuild(lst2)
				root.add_child(cur_root)
				lst1=[]
	for p in head_Node[root.data]:
		for ch in root.children:
			if ch.data==p:
				root.head=ch.head
				break
		if root.head != None:
			break				
	return root		


def pre(root,t):
	global karaka
	for j in xrange(t):
		print '\t',
	if karaka.has_key(root.head):	
		print root.head,"["+karaka[root.head]+"]"
	else:	
		print root.head

	if root.children==None:
		return
	t=t+1	
	for i in root.children:

		pre(i,deepcopy(t))


root=treebuild(pcfglist)
karak(root)
deprot=DepGraph(root.head)
dependency(deprot,root)
prepcfg(root,0)
print "DEPENDENCY TREE"
pre(deprot,0)
print karaka


		
				