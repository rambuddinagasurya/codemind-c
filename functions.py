# Function with positional parameters 
def greet(name, greeting): 
     print(greeting, name) 
# Calling the function with positional parameters 
greet("Aditya", "Hello") 
 
# Function with keyword and default parameters 
def greet_default(name, greeting="Hello"): 
    print(greeting, name) 
 
# Calling the function with keyword parameters and using default value 
greet_default(name="Aditya") 
