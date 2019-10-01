
def active_func(x1,x2,b):
    sum = x1 + x2 + b
    if sum >= 0 :    #пороговая функция активации
        return 1
    else:
        return 0


x1 = [0,1,0,1]
x2 = [0,0,1,1]
b = -1
#============== AND ===========================
w1 = 1
w2 = 1
w3 = 1.5

w1_n1 = 1
w2_n1 = 1
w3_n1 = 0.5

#================ OR ==========================

for i in range(len(x1)):
    x1_n1 = x1[i] * w1
    x2_n1 = x2[i] * w2
    b_n1 = b * w3

    x1_n2 = x1[i] * w1_n1
    x2_n2 = x2[i] * w2_n1
    b_n2 = b * w3_n1
    #============= first layer ====================
    L1_n1 = active_func(x1_n1,x2_n1,b_n1) # нейрон №1 первого слоя - ИЛИ
    L1_n2 = active_func(x1_n2,x2_n2,b_n2) # нейрон №2 первого слоя - И
    #============= exit layer =====================
    w1_L2 = -1
    w2_L2 = 1
    w3_L2 = 0.5
    print(active_func(L1_n1*w1_L2,L1_n2*w2_L2,b*w3_L2))
