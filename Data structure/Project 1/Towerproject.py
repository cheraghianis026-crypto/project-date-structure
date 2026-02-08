def hanoi (x):
    if x == 1 :
        return 1;
    else :
        return 2*hanoi(x-1) +1

x = int(input("Enter the number of disk = "))
print("Number of steps will be : " , hanoi(x))
