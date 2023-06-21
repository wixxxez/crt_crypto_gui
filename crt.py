import random
from decimal import Decimal
import sympy
import numpy as np
import warnings
warnings.filterwarnings("error")

def generate_keys_for_layers(layer, keys_per_layer)->dict:
        layer = layer[0]/10
        def generate_prime(min_value, max_value):
            # Generate a random number within the specified range
            number = random.randint(min_value, max_value)

            # Find the next prime number greater than or equal to the generated number
            prime = sympy.nextprime(number)

            return prime
        min = int(layer/1000)
        max = int(layer/100)
        print(min)
        print(max)
        keys = [generate_prime(min,max) for i in range(keys_per_layer)]
        # print(keys)
   
            
        return keys
    
def encrypt_message( message: str) -> list:
        
        encrypted_numbers = []
        for char in message:
            if char.isalpha():
                char = char.upper()
                number = ord(char) - 64
                encrypted_numbers.append(str(number))
            if char == " ":
                number = 40
                encrypted_numbers.append(str(number))
                
        return int("".join(encrypted_numbers))

def encrypt_number( number:int, keys: list)->list:
   
        return  [number % mod for mod in keys]

def chinese_remainder_theorem(modules, remainders):
    # Step 1: Calculate N
    N = 1
    for module in modules:
        N *= module

    result = 0
    # Step 2-5: Calculate x_i and the result
    for module, remainder in zip(modules, remainders):
        n_i = N // module
        x_i = pow(n_i, -1, module)
        try:
            result += remainder * n_i  * x_i
        except RuntimeWarning: 
            result += remainder * Decimal(n_i)  * Decimal(x_i)
    # Step 6: Calculate the final result
    return result % N


def init_1_layer(encrypted_message, keys_per_layer):
    encrypted_message = int(encrypted_message)
    keys_per_layer = int(keys_per_layer)
    keys = generate_keys_for_layers([encrypted_message], keys_per_layer)
    layer = encrypt_number(encrypted_message, keys)
    return layer,keys 

def init_layer(layer , keys_per_layer):
    new_layer = []
    
    keys_per_layer = int(keys_per_layer)
    keys = generate_keys_for_layers(layer , keys_per_layer)
    for i in layer:
    
        new_value = encrypt_number(int(i), keys)
        new_layer.append(new_value)
    
    reshaped_list = [element for sublist in new_layer for element in sublist]    

    return  reshaped_list, keys

