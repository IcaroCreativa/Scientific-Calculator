import re
from fractions import Fraction 


def split_math_expression(expr: str):
    number_pattern = r"-?\d+(?:\.\d+)?"
    operator_pattern = r"[+\-*/()]"
    tokens = re.split(f"({number_pattern}|{operator_pattern})", expr)
    tokens = [token for token in tokens if token]
    return tokens

def decimal_to_fraction(decimal):  
    fraction = Fraction(decimal).limit_denominator()  
    return fraction


# string='10+2*(1+10.1111)+22.2/255'
# array=['10','+','2','*','(','1.10','+''10'] 

# print(split_math_expression(string))

def convert(string):
    array=split_math_expression(string)

    for i in range(len(array)):
        if '.' in array[i]:
            # print(array[i])
            fraction=str(decimal_to_fraction(float(array[i])))
            array[i]='('+fraction+')'
            
            # print(fraction)
            

    new_string=''.join(array)
    # print(new_string)
    return new_string

 

# print(convert('2*(-2)'))





















# fraction = decimal_to_fraction(decimal) # The fraction will be printed as a string, e.g. "1/4"print(fraction)
# print(fraction)
