def gun(data):
    count=0
    print("enter element you want to search")
    x=int(input())
    for i in range(len(data)):
        if (x==data[i]):
            count=count+1
    return count  


def main():
    drr=[]
    print("enter the number of element")
    value=int(input())
    for i in range(value):
        print("enter the number of :",i+1)
        num=int(input())
        drr.append(num)
    print("you enter the data is ",drr)  

    print("you enter the data is ",len(drr))  

    ret=gun(drr)
    print("frequency is",ret)  
    
if __name__=="__main__":
    main()