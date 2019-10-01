
def active_func(x1,x2,b):
    sum = x1 + x2 + b
    if sum >= 0 :    #пороговая функция активации
        return 1
    else:
        return 0

x1 = [0,1,0,1]
x2 = [0,0,1,1]
b = -1

w1 = 1
w2 = 1
w3 = 0.5

x1 = x1*w1
x2 = x2*w2
b = b * w3

for i in range(len(x1)):
    print('выходное значение = ',active_func(x1[i],x2[i],b))