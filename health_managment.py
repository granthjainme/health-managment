import datetime
n = int(input("enter 1 for harry,2 for rohan,3 for granth: "))
import datetime
def getdate():
    
    x = datetime.datetime.now()
    print(str(x))


if n==1:
    print("you have selected harry")
    var2 = input("enter a for exercise and b for diet: ")

    if var2=="a":
        print("you have chosen exersice")
        with open ("har.txt","w")as f:
            t = input("which exercise you have perfomed: ")
            time = getdate()
            list1 = [t, time]
            write = f.write(str(list1))
            print("your record is recieved! ")
            
    elif var2=="b":
        print("you have chosen diet")
        with open("har1.txt", "w")as f:

            t1 = input("which diet you have taken: ")
            time =getdate()
            list2 = [t1,time]
            write = f.write(str(list2))
            # print(f.read())
            getdate()
        
        print("your record is recieved! ")


elif n==2:
    print("you have selected rohan")
    var3 = input("enter a for exercise and b for diet: ")

    if var3=="a":
        print("you have chosen exersice")
        with open ("rohan.txt","w")as f:
            y= input("which exercise you have perfomed: ")
            time = getdate()
            list3 = [y, time]
            write = f.write(str(list3))
            print("your record is recieved! ")
            
    elif var3=="b":
        print("you have chosen diet")
        with open("rohan1.txt", "w")as f:
            y1 = input("which diet you have taken: ")
        #time =getdate()
        #list4 = [y1]
            write = f.write(y1)
            # read1 = f.read()
            # print(read1)
            getdate()
        
        print("your record is recieved! ")



elif n==3:
    print("you have selected granth")
    var4 = input("enter a for exercise and b for diet: ")

    if var4=="a":
        print("you have chosen exersice")
        with open ("granth.txt","w")as f:
            z = input("which exercise you have perfomed: ")
            time = getdate()
            list5 = [z, time]
            write = f.write(str(list5))
            print("your record is recieved! ")
            
    elif var4=="b":
        print("you have chosen diet")
        with open("granth1.txt", "w")as f:

            z1 = input("which diet you have taken: ")
        #time =getdate()

        #list6 = [z1,time]
            write = f.write(z1)
        # print(m.read())
            getdate()
        
        print("your record is recieved! ")