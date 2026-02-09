def input_matrix():
    n = int(input("Enter n: "))

    matrix = []                                        #لیست خالی = ماترسه
    for i in range(n):                                 #هر بار یک سطر از ماتریسو نشون میده 
        row = []                                       #لیست خالی برای هر سطر 
        for j in range(n):                             #هر بار یک ستون از ماتریسو نشون میده
            value = int(input(f"matrix[{i}][{j}]: "))  #مقدار دهی
            row.append(value)
        matrix.append(row)

    return matrix


def print_matrix(matrix):                              #تابع نمایش ماتریس 
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


 
mat = input_matrix()                                   #صدا زدن ماتریس برای نمایش شکل تمام شده
print("Matrix:")
print_matrix(mat)