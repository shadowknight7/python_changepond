#write a program which will check the number is greater and equal to 70
# and less than and equal to 90

def main():
    size = int(input("enter the size: "))
    list1=[]
    print("enter values: ")
    for i in range(size):
        value = int(input())
        list1.append(value)
    print("user list : ",list1)

    filter_list=list(filter(lambda number:number>=70 and number<=90,list1))
    print(filter_list)

if __name__=="__main__":
    main()