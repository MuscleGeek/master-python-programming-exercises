#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    horas = (hr2 - hr1)*3600
    minutos = (min2 - min1)*60
    segundos = sec2 - sec1
 
    return horas + minutos + segundos

#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,2,30,1,3,20))