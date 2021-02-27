def fun(array):
    min=array[0]
    for i in range(len(array)):
        if array[i]<min:
            min=array[i]
    
    return min


def main():
    brr=[]
    print("enter the number of element")
    num=int(input())
    for i in range (num):
        print("number of brr:{} is".format(i+1))
        A=int(input())
        brr.append(A)
    print("you enter number is",brr)

    print("you enter number of element is",len(brr))

    ret=fun(brr)
    
    print("minimum number of array is",ret)

if __name__=="__main__":
    main()