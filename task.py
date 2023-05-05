# from math import ceil
try:

    speed =int(input("Введите скорость \v"))
    distance = int(input("Введите растояние \n"))
    # time = ceil(distance/speed)
    time = distance/speed
    if (distance%speed !=0):
        time = distance//speed +1
    else:
        time = distance//speed

    print ('Количество дней =')  
    print ( time)
except:
        print("Вы ввели некоректные данные")