"""
Flatonacci Function
Parameters:
    signature (list): list with 3 numbers
    n (int): n-elements of the output list

Returns:
    output (list): sequence of n elements in which every item is the sum of the last 3 (starting at index 3) 

"""

def flatonacci(signature: list, n: int) -> list:
    #input validations
    if isinstance(signature,list) == False:
        return "Invalid input for signature"
    
    elif isinstance(n,int) == False:
        return "Invalid input for n"

    #seed cases
    if n == 0:
        return []
    
    elif n == 1:
        return [signature[0]]
    
    elif n == 2:
        return [signature[0], signature[1]]

    elif n == 3:
        return signature
     
    i = 0
    output = signature
    while i < n-3:
        temp = output[i] + output[i+1] + output[i+2]
        output.append(temp)
        i += 1
    return output