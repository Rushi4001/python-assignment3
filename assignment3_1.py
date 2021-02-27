def xyz(data):
    sum=0
    for i in range(len(data)):
        sum=sum+data[i]
    return sum


def main():
    arr=[]
    print("enter the number of element")
    size=int(input())
    
    for i in range(size):
        print("enter the element no :",i+1)
        value=int(input())
        arr.append(value)
        
        
        
    print("accepted data is :",arr)
    
    ret=xyz(arr)
    
    print("addition of whole list is",ret)

if __name__=="__main__":
    main()