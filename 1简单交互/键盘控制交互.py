cars = ['bmw', 'audi', 'toyota', 'subaru']

while True:
    key=input("请输入jk 进行倒置")
    if(key=="j"):
        print(cars)
    elif(key=="k"):
        cars.reverse()       
        print(cars)