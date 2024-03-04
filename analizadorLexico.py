
#Leer el archivo
file = open("read.py")
a=file.read()


#Diccionario con los operadores
operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()


#Diccionario con los tipos de dato
data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

#Diccionario con los símbolos de puntuación
punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()


#Diccionario con los identificadores
identifier = { 'a' : 'id', 'b' : 'id', 'c' : 'id' , 'd' : 'id' }
identifier_key = identifier.keys()




count=0
#separar el archivo en lineas
program = a.split("\n")
for line in program:

    #imprimir linea
    count = count + 1
    print("line#" , count, "\n" , line)


    #separar por espacios
    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in operators_key:
            print("operator is ", operators[token])
        if token in data_type_key:
            print("datatype is", data_type[token])
        if token in punctuation_symbol_key:
            print (token, "Punctuation symbol is" , punctuation_symbol[token])
        if token in identifier_key:
            print (token, "Identifier is" , identifier[token])

        
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 



#Identificar declaración y asignación
    

#Identificar entrada y salida