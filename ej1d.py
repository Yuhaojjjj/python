# Este programa sirve para ...
def programa_1():
    max_num = input("Introduce un número: ")
    sum_nums = max_num
    i = 0
    numa = 0
    num = 0
    while (i <= 10):
        numa = num
        num = input("Introduce otro número ")
        sum_nums =sum_nums+ num
        i += 1
        if num > numa:
            print("creciente")
        if num > max_num:
            max_num = num
    print("The largest number is:" + str(max_num))
    print("The average is:" + str(float(sum_nums/10)))
programa_1()
