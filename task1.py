try:
    file = open("sample.txt","r")
    r = file.readlines()
    count = 1
    print("reading file contenets\n")
    for i in r:
        print("LINE",count,": ",i)
        count+=1
        
except FileNotFoundError:
    print("FILE DOESNT EXSISTS!!")
