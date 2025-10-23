a =  1 if int(input())>0 else 0
b =  1 if int(input())>0 else 0

match (a,b):
    case (1,1):
        print(1)
    case (0,1):
        print(2)
    case (0,0):
        print(3)
    case (1,0):
        print(4)