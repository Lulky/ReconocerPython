num1 = 42 #Declaración de número entero
num2 = 2.3 #Declaracion de número flotante
boolean = True #Boleano
string = 'Hello World' #Cadena
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Arreglo
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Diccionario
fruit = ('blueberry', 'strawberry', 'banana') #tupla
print(type(fruit)) #Type Check Tupla
print(pizza_toppings[1]) #'Sausage'
pizza_toppings.append('Mushrooms') # ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives', 'Mushrooms']
print(person['name']) # 'John'
person['name'] = 'George' #{'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person['eye_color'] = 'blue' # {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
print(fruit[2]) #Tupla acceder al valor

if num1 > 45:
    print("It's greater") #condicional if
else:
    print("It's lower") #condicional else  "It's lower"

if len(string) < 5:
    print("It's a short word!")#condicional if
elif len(string) > 15:
    print("It's a long word!") #condicional else if
else:
    print("Just right!") #Condicional else  Print "Just right!" porque tiene 11 caracteres

for x in range(5): #for bucle 0 to 4
    print(x)
for x in range(2,5): #for bucle 2 to 4
    print(x)
for x in range(2,10,3): #for bucle 2 to 9 going 3 by 3 so it will be 
    print(x) # print 2, 5, 8
x = 0
while(x < 5): #whie loop 0 to 4
    print(x)
    x += 1 #print 0, 1, 2, 3, 4

pizza_toppings.pop() # Arreglo, quita el último valor del arreglo
pizza_toppings.pop(1) #Arreglo, quita el valor en la posicion 1 del arreglo , quita Sausage.

print(person) #{'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color')
print(person) #{'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') #'After 1st if statement' 'After 1st if statement' 'After 1st if statement' 
    if topping == 'Olives':
        break 

def print_hello_ten_times():
    for num in range(10):
        print('Hello')#Imprime 10 veces Hello

print_hello_ten_times() #

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')#Imprime 4 veces Hello

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #Parametro
    for num in range(x): #buble
        print('Hello')

print_hello_x_or_ten_times() #Imprime 10 veces el valor de HEllo ya que se le daun avlor de 10 arriba
print_hello_x_or_ten_times(4)#Imprimer 4 veces Hello porque X toma el valor de 4


"""
Bonus section
"""

# print(num3) # NameError name variable name is not defined
# num3 = 72 # 
# fruit[0] = 'cranberry'  #  TypeError 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError 'favorite_team'
# print(pizza_toppings[7]) # IndexError list index out of range
#   print(boolean) # Identacion problem
# fruit.append('raspberry') #AttributeError 'tuple' object has no attribute 'append'
# fruit.pop(1)  # AttributeError 'tuple' object has no attribute 'pop'