ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else if (elifs)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual > 3000:
        print("bien bro, estas bien")
else:
    print("ey bro, esta gastando una banda, hay que ver si te alcanza")