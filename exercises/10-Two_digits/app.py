#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  
    res = int(digit%100)
    decenas = int(res-(res%10))/10
    unidades = int(res%10)

    return round(decenas),unidades
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
