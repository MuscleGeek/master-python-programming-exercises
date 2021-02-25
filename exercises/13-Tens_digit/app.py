#Complete the function to return the tens digit of a given interger
def tens_digit(num):
    if num > 10:
        return int(str(num)[-2:-1])
    else:
        print("Ingrese un numero mayor 9")
    return 
  




#Invoke the function with any interger.
print(tens_digit(854345))