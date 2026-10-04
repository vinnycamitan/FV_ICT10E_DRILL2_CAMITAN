# working with numbers
from pyscript import display, document

# Adds two values
def adding_numbers(e): 
    document.getElementById('result').innerHTML = " " # clear the previous result    
    first_number = float(document.getElementById('number1').value)
    second_number = float(document.getElementById('number2').value)
    sum = first_number + second_number

    display(f'The sum of {first_number} & {second_number} is {sum} imnida!', target='result')


# Subtarcts two values
def subtracting_numbers(e): 
    document.getElementById('result').innerHTML = " " # clear the previous result    
    first_number = float(document.getElementById('number1').value)
    second_number = float(document.getElementById('number2').value)
    difference = first_number - second_number

    display(f'The difference of {first_number} & {second_number} is {difference} imnida!', target='result')


# Multiplys two values
def multiplying_numbers(e): 
    document.getElementById('result').innerHTML = " " # clear the previous result    
    first_number = float(document.getElementById('number1').value)
    second_number = float(document.getElementById('number2').value)
    product = first_number * second_number

    display(f'The product of {first_number} & {second_number} is {product} imnida!', target='result')


# Divides two values
def dividing_numbers(e): 
    document.getElementById('result').innerHTML = " " # clear the previous result    
    first_number = float(document.getElementById('number1').value)
    second_number = float(document.getElementById('number2').value)
    quotient = first_number / second_number

    display(f'The quotient of {first_number} & {second_number} is {quotient} imnida!', target='result')


# Using floor divison on two values; divides and removes the decimal
def floor_numbers(e): 
    document.getElementById('result').innerHTML = " " # clear the previous result    
    first_number = float(document.getElementById('number1').value)
    second_number = float(document.getElementById('number2').value)
    floor = first_number // second_number

    display(f'The floor division of {first_number} & {second_number} is {floor} imnida!', target='result')


 # Using modulus on two values; finds the remainder in the equation.
def modulus_numbers(e): 
    document.getElementById('result').innerHTML = " " # clear the previous result    
    first_number = float(document.getElementById('number1').value)
    second_number = float(document.getElementById('number2').value)
    remainder = first_number % second_number

    display(f'The remainder of {first_number} & {second_number} is {remainder} imnida!', target='result')


# Using Exponentiation on two values; raises the first nnumber to the power of the second number
def exponents_numbers(e): 
    document.getElementById('result').innerHTML = " " # clear the previous result    
    first_number = float(document.getElementById('number1').value)
    second_number = float(document.getElementById('number2').value)
    power = first_number ** second_number

    display(f'The {first_number} raised to the {second_number} is {power}  target='result')