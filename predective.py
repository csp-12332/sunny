#gram = {"S":["(L)","a"],"L":["L,S","S"]}
gram={"S":["a","^","(T)"],"T":["T,S","S"]}

start=input('Enter the starting symbol: ')



def removeDirectLR(gramA, A):
	"""gramA is dictonary"""
	temp = gramA[A]
	tempCr = []
	tempInCr = []
	for i in temp:
		if i[0] == A:
			
			tempInCr.append(i[1:]+[A+"'"])
		else:
			
			tempCr.append(i+[A+"'"])
	tempInCr.append(["e"])
	gramA[A] = tempCr
	gramA[A+"'"] = tempInCr
	return gramA


def checkForIndirect(gramA, a, ai):
	if ai not in gramA:
		return False 
	if a == ai:
		return True
	for i in gramA[ai]:
		if i[0] == ai:
			return False
		if i[0] in gramA:
			return checkForIndirect(gramA, a, i[0])
	return False

def rep(gramA, A):
	temp = gramA[A]
	newTemp = []
	for i in temp:
		if checkForIndirect(gramA, A, i[0]):
			t = []
			for k in gramA[i[0]]:
				t=[]
				t+=k
				t+=i[1:]
				newTemp.append(t)

		else:
			newTemp.append(i)
	gramA[A] = newTemp
	return gramA

def rem(gram):
	c = 1
	conv = {}
	gramA = {}
	revconv = {}
	for j in gram:
		conv[j] = "A"+str(c)
		gramA["A"+str(c)] = []
		c+=1
  

	for i in gram:
		for j in gram[i]:
			temp = []	
			for k in j:
				if k in conv:
					temp.append(conv[k])
				else:
					temp.append(k)
			gramA[conv[i]].append(temp)


	#print(gramA)
	for i in range(c-1,0,-1):
		ai = "A"+str(i)
		for j in range(0,i):
			aj = gramA[ai][0][0]
			if ai!=aj :
				if aj in gramA and checkForIndirect(gramA,ai,aj):
					gramA = rep(gramA, ai)

	for i in range(1,c):
		ai = "A"+str(i)
		for j in gramA[ai]:
			if ai==j[0]:
				gramA = removeDirectLR(gramA, ai)
				break

	op = {}
	for i in gramA:
		a = str(i)
		for j in conv:
			a = a.replace(conv[j],j)
		revconv[i] = a

	for i in gramA:
		l = []
		for j in gramA[i]:
			k = []
			for m in j:
				if m in revconv:
					k.append(m.replace(m,revconv[m]))
				else:
					k.append(m)
			l.append(k)
		op[revconv[i]] = l

	return op

result = rem(gram)


def first(gram, term):
	a = []
	if term not in gram:
		return [term]
	for i in gram[term]:
		if i[0] not in gram:
			a.append(i[0])
		elif i[0] in gram:
			a += first(gram, i[0])
	return a

firsts = {}

for i in result:
	firsts[i] = first(result,i)


def follow(gram, term):
	a = []
	for rule in gram:
		for i in gram[rule]:
			if term in i:
				temp = i
				indx = i.index(term)
				if indx+1!=len(i):
					if i[-1] in firsts:
						a+=firsts[i[-1]]
					else:
						a+=[i[-1]]
				else:
					a+=["e"]
				if rule != term and "e" in a:
					a+= follow(gram,rule)
	return a

follows = {}
for i in result:
	follows[i] = list(set(follow(result,i)))
	if "e" in follows[i]:
		follows[i].pop(follows[i].index("e"))
	if start==i:
		follows[i]+=["$"]

print('\nNon-terminals\tfirst\tfollow')
for i in follows:
  print(i,'\t',firsts[i],'\t',follows[i])


termi=[]
for i in follows:
  termi=termi+firsts[i]
  termi=termi+follows[i]
termi=list(set(termi))

	

pt={}
for i in result:
  if(i not in pt.keys()):
    pt[i]={}
  for j in termi:
    if(j not in pt[i].keys()):
      pt[i][j]=[]
  for j in result[i]:
    if((j[0] in termi)and(j[0]!='e')):
      pt[i][j[0]].append(''.join(j))
    elif(j[0]=='e'):
      temp=follows[i]
      for k in temp:
        pt[i][k].append(''.join(j))
    else:
      temp=firsts[j[0]]
      for k in temp:
        pt[i][k].append(''.join(j))


print('Predictive pasing table')
print('non-terminal',end='\t')
for i in termi:
  print(i,end='\t')
print()

for j in pt:
  print(j,end='\t\t')
  for i in termi:
    print((pt[j][i]),end='\t')
  print()


def slic(st):
  temp=[]
  n=len(st)
  i=0
  while n>i:
    if(i<n-1):
      if(st[i+1])=='\'':
        temp.append(st[i]+st[i+1])
        i+=2
      else:
        temp.append(st[i])
        i+=1
    else:
      temp.append(st[i])
      i+=1

  return temp

print('stack\t\tinput\t\taction')
w='(a,a)$'
stk=['$','S']
i=0
while 1:
  if(''.join(stk)==w[i:]):
    print(stk,'\t',w[i:],'\taccepted')
    break
  
  if(stk[-1] not in termi):
    print(stk,'\t',w[i:],'\t',pt[stk[-1]][w[i]])
    if(''.join(pt[stk[-1]][w[i]][0])!='e'):
      temp=slic(pt[stk[-1]][w[i]][0])
      stk.pop()
      stk=stk+temp[::-1]
    else:
      stk.pop()
    
  else:
    if(stk[-1]==w[i]):
      print(stk,'\t',w[i:],'\tpop ->',stk[-1])
      stk.pop()
      i+=1
