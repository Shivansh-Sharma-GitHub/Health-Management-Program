def gettime():
    ''' this function is to import date and time'''
    import datetime
    return datetime.datetime.now()

k = int(input("Enter client number\n 1:Hitesh Kumar Sharma\n 2:Manju Sharma\n 3:Shivansh Sharma\n"))


if k==1:
    h = int(input("Press 1 to log data\nPress 2 to retrieve data\n" ))
    if h==1:
        log = int(input("Press 1 to enter Exercise\nPress 2 to enter Diet\n"))
        if log==1:
            value=input("type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif log==2:
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")    
    elif h==2:
        get = int(input("Press 1 to retrieve Exercise\nPress 2 to retrieve Diet\n"))   
        if get == 1:
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")  
        elif get == 2:
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
elif k==2:
        r = int(input("Press 1 to log data\nPress 2 to retrieve data\n" ))
        if r==1:
            log = int(input("Press 1 to enter Exercise\nPress 2 to enter Diet\n"))
            if log==1:
                value=input("type here\n")
                with open("rohan-ex.txt","a") as op:
                    op.write(str([str(gettime())])+": "+value+"\n")
                print("successfully written")
            elif log==2:
                value = input("type here\n")
                with open("rohan-food.txt", "a") as op:
                    op.write(str([str(gettime())]) + ": " + value + "\n")
                print("successfully written")    
        elif r==2:
            get = int(input("Press 1 to retrieve Exercise\nPress 2 to retrieve Diet\n"))   
            if get == 1:
                with open("rohan-ex.txt") as op:
                    for i in op:
                        print(i,end="")  
            elif get == 2:
                with open("rohan-food.txt") as op:
                    for i in op:
                        print(i, end="")
elif k==3:
    m = int(input("Press 1 to log data\nPress 2 to retrieve data\n" ))
    if m==1:
        log = int(input("Press 1 to enter Exercise\nPress 2 to enter Diet\n"))
        if log==1:
            value=input("type here\n")
            with open("hammad-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif log==2:
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")    
    elif m==2:
        get = int(input("Press 1 to retrieve Exercise\nPress 2 to retrieve Diet\n"))   
        if get == 1:
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i,end="")  
        elif get == 2:
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
                       

                                 