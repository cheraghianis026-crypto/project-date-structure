def hanoi (n , source , target , auxilary):
   if  n > 0 :
    # Move n-1 disks from source to auxilary peg
     hanoi(n-1 , source , auxilary , target)

    # Move the nth disk from source to target peg
     print("Move disk", n , "from" , source , "to" , target)

     # Move the n-1 disks from auxilary peg to target peg
     hanoi(n-1 , auxilary , target , source)

x = int(input("Enter the number of disks :  " ))
hanoi(x ,'A','C','B')


