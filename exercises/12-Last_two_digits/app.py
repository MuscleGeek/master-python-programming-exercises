#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
    if num > 9:
        return int(str(num)[-2:])
    else:
        print("Ingrese un numero mayor 9")
    return 
     

#Invoke the function with any interger greater than 9.
print(last_two_digits(1234))
