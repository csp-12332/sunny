nfa = {}                                 
n = int(input("Enter number of states : ")) 
t = int(input("Enter number of input symbols : "))  
for i in range(n):  
    state = input("state name : ")          
    nfa[state] = {}                         
    for j in range(t):
        path = input("input : ")               
        print(f"{state} --{path}--> ",end=" ")
        reaching_state = [x for x in input().split()]  
        nfa[state][path] = reaching_state  

print("Enter final state of NFA : ",end="")
nfa_final_state = [x for x in input().split()]  
    
new_states_list = []                          
dfa = {}                                      
keys_list = list(list(nfa.keys())[0])         
path_list = list(nfa[keys_list[0]].keys())    
states_dict=list(nfa.keys())

print("transition table of e-NFA :")
print('\t',end='')
for i in path_list:
    print(i,end="\t")
print()
for i in nfa.keys():
    print(i,end="\t")
    for j in path_list:
        print(nfa[i][j],end="\t")
    print()


def getEpsilonClosure(state):
  closure = dict()
  closure[state] = 0
  closure_stack = [state]
 
  while (len(closure_stack) > 0):
    cur = closure_stack.pop(0)
    for x in nfa[cur]['e']:
      if x not in closure.keys():
        closure[x] = 0
        closure_stack.append(x)
    closure[cur] = 1
  return closure.keys()

epsilon_closure = dict()
for x in nfa.keys():
    epsilon_closure[x] = list(getEpsilonClosure(x))

print()
for i in epsilon_closure.keys():
  print(f'e-closure of {i}:', epsilon_closure[i] )
print()
                        

var = "".join(list(set(epsilon_closure[keys_list[0]])))
var="".join(sorted(var))
dfa[var] = {}          
if var not in keys_list:                      
    new_states_list.append(var)                 
    keys_list.append(var)   
         


while len(new_states_list) != 0:                    
    dfa[new_states_list[0]] = {}                     
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)-1):
            temp = [] 
            tempE=[]                              
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]
                temp=list(set(temp))
                for k in temp:
                    tempE+=epsilon_closure[k]
            s = ""
            s = s.join(list(set(tempE))) 
            s="".join(sorted(s))                   
            if s not in keys_list:                   
                new_states_list.append(s)            
                keys_list.append(s)                  
            dfa[new_states_list[0]][path_list[i]] = s   
        
    new_states_list.remove(new_states_list[0])

print("\nTransition table of DFA :")
print('\t',end='')
for i in range(len(path_list)-1):
    print(path_list[i],end="\t")

print()
for i in dfa.keys():
    print(i,end="\t")
    for j in range(len(path_list)-1):
        print(dfa[i][path_list[j]],end="\t")
    print()

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
        
print("\nFinal states of the DFA are : ",dfa_final_states)     
