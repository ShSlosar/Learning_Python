num1 = 42 # Variable declaration 
num2 = 2.3 # Variable declaration 
boolean = True #data type-boolean
string = 'Hello World' #dataType-String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #type check
print(pizza_toppings[1]) #list access value log statement
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #dictionary log value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #log statement tuple access value

if num1 > 45: #conditional
    print("It's greater") #log statement
else:
    print("It's lower") #log statement

if len(string) < 5: #length check Conditional
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop 0 to 5
    print(x)
for x in range(2,5): #for loop 2 to 5
    print(x)
for x in range(2,10,3): #for loop, 2 to 10, with an incriment of 3
    print(x)
x = 0 #varible decliration 
while(x < 5): #while loop range 
    print(x)
    x += 1 #icriment of 1 

pizza_toppings.pop() #list remove last value 
pizza_toppings.pop(1) #list remove value in "1" position

print(person) #log statement 
person.pop('eye_color') #dictionary remove value 
print(person) #log statement

for topping in pizza_toppings: #initinize list, "decare topping" variable 
    if topping == 'Pepperoni': #conditional
        continue #continue to next loop iteration 
    print('After 1st if statement')
    if topping == 'Olives':
        break #break the loop

def print_hello_ten_times(): #define function 
    for num in range(10): #var num, range 0 to 10. peramiter
        print('Hello')

print_hello_ten_times() #Invoke function 

def print_hello_x_times(x): # define function with "x" as an argument. 
    for num in range(x): #using variable "x" as the range for the loop
        print('Hello')

print_hello_x_times(4) #passing "4" as the arguent for the function

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #prints "hello" 10 times 
print_hello_x_or_ten_times(4) #prints "hello" 4 times


"""
Bonus section
"""

print(num3) #log statement 
num3 = 72 #variable decleration "number"
fruit[0] = 'cranberry' #Change list value 
print(person['favorite_team']) #log tuple value
print(pizza_toppings[7]) #log list value at index 7
print(boolean) #log True boolean
fruit.append('raspberry') #ERROR
fruit.pop(1) #ERROR