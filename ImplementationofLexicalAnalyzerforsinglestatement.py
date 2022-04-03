def checker(token):
    if(token in operators.keys()):
        print(token + " is " + operators[token])
        return
    elif(token in dataType.keys()):
        print(token + " is " + dataType[token])
        return
    elif(token in keyWords):
        print(token + " is keyword")
        return
    elif(token in numbers):
        print(token + " is constant")
        return
    elif(token in nonIdentifiers):
        print(token + " is not a identifier")
        return
    else:
        print(token + " is identifier" )



operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', 
            '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator', '%' : 'Modulo Operator', 
            '<':'Relational operator','>':'Relational operator','|':'Logical operator','&':'Logical operator','!':'Logical operator' }
dataType = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
numbers = str(list(range(-100,100)))
keyWords = ['if','else','for', 'while','do','return','break','continue','print']
nonIdentifiers = ['_','`','~','@','#','$','(',')','"',':',';','{','}','[',']','?']

code = input("Enter the statement: ")
tokens = code.split(' ')
print("Tokens are : \n")
for i in tokens:
    checker(i)
