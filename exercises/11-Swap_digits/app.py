#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):

    res = int(num%100)
    decenas = int(res-(res%10))/10
    unidades = int(res%10)

    return str(unidades)+str(round(decenas))
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(79))

