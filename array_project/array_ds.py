class Array:
    def __init__(self, size):
        self.size = size             
        self.data = [None] * size              # ساختن آرایه ی خالی با سایز داده شده
        self.length = 0                        #طول فعلی


    def insert(self, obj, index):
    
        if self.length == self.size:           #بررسی میکنیم ببینیم آرایه ظرفیت دارد یا نه
            print("Array is full")
            return

        
        if index < 0 or index > self.length:   #بررسی میکنیم ببینیم ایندکس خواسته شده با سایز آرایه همخوانی داره یا نه
            print("Invalid index")
            return

        
        i = self.length                        #شیفت ببه سمت آخر آرایه
        while i > index:
            self.data[i] = self.data[i - 1]    #در این قسمت مقدار خانه ی قبلی به خانه ی بعدی کپی میشود تا جا باز بشه
            i -= 1

        
        self.data[index] = obj                 #تو جای خالی ایجاد شده با شیفت، مقدار عنصر رو قرار میدیم
        self.length += 1


    def delete (self , index):
            pass
    def find (self , obj):
            pass  


size = int(input("Enter array size: "))
arr = Array(size)                         #ساخت آرایه با سایز داده شده

while True:
    print("\nCurrent Array:", arr.data)
    print("1. Insert")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        value = int(input("Enter value: "))
        index = int(input("Enter index: "))
        arr.insert(value, index)

    elif choice == "2":
        print("Program finished.")
        break

    else:
        print("Invalid choice")