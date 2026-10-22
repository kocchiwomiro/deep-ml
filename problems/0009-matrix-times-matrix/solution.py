def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if(len(a[0])!=len(b)):
        return -1
    else:
        c=[]
        for row in range(len(a)):
            x=[]
            for column in range(len(b[0])):
                summate=0
                for count in range(len(b)):
                    summate+=a[row][count]*b[count][column]
                x.append(summate)
            c.append(x)           
    return c