def symbolTable(token):
    if((token not in operators.keys()) and (token not in dataType.keys()) and (token not in keyWords) and (token not in numbers) and (token not in nonIdentifiers) ):
        print(token + "\t\t" + str(id(token)))

operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', 
            '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator', '%' : 'Modulo Operator', 
            '<':'Relational operator','>':'Relational operator','|':'Logical operator','&':'Logical operator','!':'Logical operator' }
dataType = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
numbers = str(list(range(-100,100)))
keyWords = ['if','else','for', 'while','do','return','break','continue','print']
nonIdentifiers = ['_','`','~','@','#','$','(',')','"',':',';','{','}','[',']','?']

code = input("Enter the string: ")
tokens = code.split(' ')

print("\nSymbol \t\t Address")
tokens = set(tokens)
for i in tokens:
    symbolTable(i)
