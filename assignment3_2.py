def fun(data):
    max=data[0]
    for i in range (len(data)):
        if(data[i]>max):
            max=data[i]
    return max    



def main():
    crr=[]
    print("enter the number of element")
    value1=int(input())
    for i in range (value1):
        print("enter the elements",i+1)
        value=int(input())
        crr.append(value)
    print("number of element is:",len(crr))   
    print("you enter the data is:",crr)
    
    ret=fun(crr)
    print("maximum number is :",ret)
    

if __name__=="__main__":
    main()