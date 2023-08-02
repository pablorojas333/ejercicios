articulo= int(input('ingrese precio del articulo: '))
marca= (input('ingrese nombre de la marca: '))

if marca=='nosy' and articulo>=2000:
    pago=articulo*0.90
    pagototal=pago*0.95
    print('usted pagara: ',pagototal,'pesos')
elif marca=='nosy' and articulo<2000:
    pago2=articulo*0.90
    print('usted pagara: ',pago2, 'pesos')
elif marca!='nosy' and articulo>=2000:
     pago3=articulo*0.95
     print('usted pagara: ',pago3,'pesos')
else:
    print('usted pagara', articulo,'pesos')