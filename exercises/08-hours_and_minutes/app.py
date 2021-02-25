#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  
  horas = int(secs/3600) #segundos ingresados consvertidos a horas

  minutos = int(secs/60) #segundos ingresados convertidos a minutos

  return horas, minutos



#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))