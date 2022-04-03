import re
#gram = {"E":["E+E","E*E","i"]}
#gram = {"E":["E+T","T"],"T":["T*F","F"],"F":["(E)","i"]}
gram = {"S":["(L)","a"],"L":["L,S","S"]}
bdmas={}
start='S'
term=[]
nonterm=[]
for i,j in gram.items():
  print(i,end=' -> ')
  print(*j,sep=' | ')
  for k in j:
    for m in k:
      if((re.match("[A-Z]",m))):
        nonterm.append(m)
      else:
        term.append(m)

term=list(set(term))
nonterm=list(set(nonterm))
term.append('$')
op={}
bm={'(':1,')':1,'*':'2','/':2,'+':3,'-':3}
def bodmas(left,top):
  if(int(bm[left]) < int(bm[top])):
    return '>'
  elif(int(bm[left]) == int(bm[top])):
    return '<>'
  else:
    return '<'

print('terminals: ',*term,'\nnon-terminals: ',*nonterm)

for i in term:
  op[i]={}
  for j in term:
    if(i==j):
      op[i][j]='-'
    elif(i=='$'):
      op[i][j]='<'
    elif(j=='$'):
      op[i][j]='>'
    elif(re.match('[a-z]',i)):
      op[i][j]='>'
    elif(re.match('[a-z]',j)):
      op[i][j]='<'
    elif(i in bm.keys() and j in bm.keys()):
      op[i][j]=bodmas(i,j)
    else:
      op[i][j]='<>'

print('\n ',*op.keys(),sep='\t')
op.values
for i,j in op.items():
  print(i,end='')
  print(' ',*j.values(),sep='\t')

def topterminal(rstk):
  for i in range(len(rstk)):
    if (rstk[i] in term):
      return -(i)-1

def stkchecker(stk):
  k=1
  for _ in range(len(stk)):
    for i,j in gram.items():
      if(''.join(stk[k:]) in j):
        return i,stk[k:]
    k+=1
  return 0

print('\nstack\t\tinput\t\taction')
w='(a,a)$'
stk=['$']
i=0

while 1:
  if(w[i:]=='$' and ''.join(stk)==('$'+start)):
    print(*stk,'\t\t',w[i:],'\t\taccepted ')
    break

  tt=topterminal(stk[::-1])
  if((op[stk[tt]][w[i]] == '<')or(op[stk[tt]][w[i]] =='-')):
    print(*stk,'\t\t',w[i:],'\t\t',stk[tt],op[stk[tt]][w[i]],w[i],'shift')
    stk.append(w[i])
    i+=1
  elif(op[stk[tt]][w[i]] == '>'):
    temp1,temp2=stkchecker(stk)
    print(*stk,'\t\t',w[i:],'\t\t',stk[tt],op[stk[tt]][w[i]],w[i],' reduce ',temp1,' -> ',temp2)
    for _ in range(len(temp2)):
      stk.pop()
    stk.append(temp1)
  else:
    if(stkchecker(stk)):
      temp1,temp2=stkchecker(stk)
      print(*stk,'\t\t',w[i:],'\t\t',stk[tt],'>',w[i],' reduce ',temp1,' -> ',temp2)
      for _ in range(len(temp2)):
        stk.pop()
      stk.append(temp1)
    else:
      print(*stk,'\t\t',w[i:],'\t\t',stk[tt],'<',w[i],'shift')
      stk.append(w[i])
      i+=1
