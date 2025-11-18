def inversor():
    num = input("Dime un número: ")
    para = False
    nf = 0
    nd = 0
    i = len(str(num))
    while para == False:
        i = i - 1
        nd = num % 10
        num = num / 10
        nf += nd * (10 ** i)
        if num < 1:
            para = True
    print nf
inversor()
