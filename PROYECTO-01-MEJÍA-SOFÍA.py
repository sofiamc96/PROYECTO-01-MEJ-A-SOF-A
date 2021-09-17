from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

# -------------------
# VENTAS Y BÚSQUEDAS
# -------------------

# Se eliminan datos que no correspondan al año 2020:
for venta in lifestore_sales:
    if venta[3][6:10] != '2020':
        lifestore_sales.remove(venta)

# print(lifestore_sales)

# Se contabiliza el número de ventas por producto:
ventas = []
num_ventas = 0
for producto in lifestore_products:
    for venta in lifestore_sales:
        if producto[0] == venta[1]:
            num_ventas += 1
    ventas.append([producto[0], producto[1], num_ventas])
    num_ventas = 0

# print(ventas)

# Se ordena el número de ventas por producto de mayor a menor:
ventas_ord = []
while ventas:
    num_ventas_max = ventas[0][2]
    prod_ventas_max = ventas[0]
    for venta in ventas:
        if venta[2] > num_ventas_max:
            num_ventas_max = venta[2]
            prod_ventas_max = venta
    ventas_ord.append(prod_ventas_max)
    ventas.remove(prod_ventas_max)
    
# print(ventas_ord)

# Se obtienen los 50 productos más vendidos (si los hay):
prod_mas_vendidos = []
for i in range(50):
    if ventas_ord[i][2] != 0:
        prod_mas_vendidos.append(ventas_ord[i])

# print(prod_mas_vendidos)
# print(len(prod_mas_vendidos))

# Se obtienen los productos que no se han vendido (si los hay):
prod_rezagados = []
for i in range(len(ventas_ord)):
    if ventas_ord[i][2] == 0:
        prod_rezagados.append(ventas_ord[i])

# print(prod_rezagados)
# print(len(prod_rezagados))

'''Se obtienen las ventas por categoría de productos 
    (ordenadas de mayor a menor):'''
procesadores = []
tarjetas_de_video = []
tarjetas_madre = []
discos_duros = []
memorias_usb = []
pantallas = []
bocinas = []
audifonos = []
for venta in ventas_ord:
    for producto in lifestore_products:
        if venta[0] == producto[0]:
            if producto[3] == 'procesadores':
                procesadores.append(venta)
            elif producto[3] == 'tarjetas de video':
                tarjetas_de_video.append(venta)
            elif producto[3] == 'tarjetas madre':
                tarjetas_madre.append(venta)
            elif producto[3] == 'discos duros':
                discos_duros.append(venta)
            elif producto[3] == 'memorias usb':
               memorias_usb.append(venta)
            elif producto[3] == 'pantallas':
                pantallas.append(venta)
            elif producto[3] == 'bocinas':
                bocinas.append(venta)
            elif producto[3] == 'audifonos':
                audifonos.append(venta)
ventas_por_categoria = [procesadores, tarjetas_de_video, tarjetas_madre,
                        discos_duros, memorias_usb, pantallas, bocinas, 
                        audifonos]

'''Se obtienen las ventas por categoría de productos 
    (ordenadas de menor a mayor):'''
procesadores_rev = list(reversed(procesadores))
tarjetas_de_video_rev = list(reversed(tarjetas_de_video))
tarjetas_madre_rev = list(reversed(tarjetas_madre))
discos_duros_rev = list(reversed(discos_duros))
memorias_usb_rev = list(reversed(memorias_usb))
pantallas_rev = list(reversed(pantallas))
bocinas_rev =  list(reversed(bocinas))
audifonos_rev = list(reversed(audifonos))
ventas_por_categoria_rev = [procesadores_rev, tarjetas_de_video_rev, 
                            tarjetas_madre_rev, discos_duros_rev, 
                            memorias_usb_rev, pantallas_rev, bocinas_rev, 
                            audifonos_rev]

# print(ventas_por_categoria)
# print(ventas_por_categoria_rev)

# Se contabiliza el número de búsquedas por producto:
busquedas = []
num_bus = 0
for producto in lifestore_products:
    for busqueda in lifestore_searches:
        if producto[0] == busqueda[1]:
            num_bus += 1
    busquedas.append([producto[0], producto[1], num_bus])
    num_bus = 0

# print(busquedas)

# Se ordena el número de búsquedas por producto de mayor a menor:
busquedas_ord = []
while busquedas:
    num_bus_max = busquedas[0][2]
    prod_bus_max = busquedas[0]
    for busqueda in busquedas:
        if busqueda[2] > num_bus_max:
            num_bus_max = busqueda[2]
            prod_bus_max = busqueda
    busquedas_ord.append(prod_bus_max)
    busquedas.remove(prod_bus_max)
    
# print(busquedas_ord)
# print(len(busquedas_ord))

# Se obtienen los 50 productos más buscados (si los hay):
prod_mas_buscados = []
for i in range(50):
    if busquedas_ord[i][2] > 1:
        prod_mas_buscados.append(busquedas_ord[i])

# print(prod_mas_buscados)
# print(len(prod_mas_buscados))

# Se obtienen los 50 productos menos buscados (si los hay):
prod_menos_buscados = []
for i in range(1,51):
    if busquedas_ord[-i] not in prod_mas_buscados:
        prod_menos_buscados.append(busquedas_ord[-i])

# print(prod_menos_buscados)
# print(len(prod_menos_buscados))

'''Se obtienen las búsquedas por categoría de productos 
    (ordenadas de mayor a menor):'''
procesadores_bus = []
tarjetas_de_video_bus = []
tarjetas_madre_bus = []
discos_duros_bus = []
memorias_usb_bus = []
pantallas_bus = []
bocinas_bus = []
audifonos_bus = []
for busqueda in busquedas_ord:
    for producto in lifestore_products:
        if busqueda[0] == producto[0]:
            if producto[3] == 'procesadores':
                procesadores_bus.append(busqueda)
            elif producto[3] == 'tarjetas de video':
                tarjetas_de_video_bus.append(busqueda)
            elif producto[3] == 'tarjetas madre':
                tarjetas_madre_bus.append(busqueda)
            elif producto[3] == 'discos duros':
                discos_duros_bus.append(busqueda)
            elif producto[3] == 'memorias usb':
               memorias_usb_bus.append(busqueda)
            elif producto[3] == 'pantallas':
                pantallas_bus.append(busqueda)
            elif producto[3] == 'bocinas':
                bocinas_bus.append(busqueda)
            elif producto[3] == 'audifonos':
                audifonos_bus.append(busqueda)
busquedas_por_categoria = [procesadores_bus, tarjetas_de_video_bus, tarjetas_madre_bus,
                        discos_duros_bus, memorias_usb_bus, pantallas_bus, bocinas_bus, 
                        audifonos_bus]

'''Se obtienen las búsquedas por categoría de productos 
    (ordenadas de menor a mayor):'''
procesadores_bus_rev = list(reversed(procesadores_bus))
tarjetas_de_video_bus_rev = list(reversed(tarjetas_de_video_bus))
tarjetas_madre_bus_rev = list(reversed(tarjetas_madre_bus))
discos_duros_bus_rev = list(reversed(discos_duros_bus))
memorias_usb_bus_rev = list(reversed(memorias_usb_bus))
pantallas_bus_rev = list(reversed(pantallas_bus))
bocinas_bus_rev =  list(reversed(bocinas_bus))
audifonos_bus_rev = list(reversed(audifonos_bus))
busquedas_por_categoria_rev = [procesadores_bus_rev, tarjetas_de_video_bus_rev, 
                            tarjetas_madre_bus_rev, discos_duros_bus_rev, 
                            memorias_usb_bus_rev, pantallas_bus_rev, 
                            bocinas_bus_rev, audifonos_bus_rev]

# print(busquedas_por_categoria)
# print(busquedas_por_categoria_rev)

# ---------------------------
# MEJORES Y PEORES PRODUCTOS
# ---------------------------
    
# prod_calif_dev = [id_prod, nombre_prod, prom_calif, raz_dev]

'''Se calcula el promedio de reseñas y la razón de devolución 
por producto vendido:'''
prod_calif_dev = []
num_ventas = 0
num_dev = 0
suma_calif = 0
for producto in lifestore_products:
    for venta in lifestore_sales:
        if producto[0] == venta[1]:
            num_ventas += 1
            suma_calif += venta[2]
            if venta[4] == 1:
                num_dev += 1
    if num_ventas != 0:
        prom_calif = suma_calif / num_ventas
        raz_dev = num_dev / num_ventas
        prod_calif_dev.append([producto[0], producto[1], prom_calif, raz_dev])
        num_ventas = 0
        suma_calif = 0
        num_dev = 0

# print(prod_calif_dev)

'''Se obtienen los mejores y los peores productos de acuerdo al promedio 
    de reseñas y la razón de devolución:'''
prod_mejor_calif = []
prod_peor_calif = []
for producto in prod_calif_dev:
    if producto[2] > 4.8 and producto[3] == 0.0:
        prod_mejor_calif.append(producto)
    elif producto[2] < 4.7 or producto[3] > 0.0:
        prod_peor_calif.append(producto)

# print(prod_mejor_calif)
# print(len(prod_mejor_calif))
# print(prod_peor_calif)
# print(len(prod_peor_calif))

# Se ordenan los mejores y peores productos obtenidos previamente:
prod_mejor_calif_ord = []
prod_peor_calif_ord = []
while prod_mejor_calif:
    calif_max = prod_mejor_calif[0][2]
    prod_calif_max = prod_mejor_calif[0]
    for producto in prod_mejor_calif:
        if producto[2] > calif_max:
           calif_max = producto[2]
           prod_calif_max = producto
    prod_mejor_calif_ord.append(prod_calif_max)
    prod_mejor_calif.remove(prod_calif_max)
while prod_peor_calif:
    calif_min = prod_peor_calif[0][2]
    prod_calif_min = prod_peor_calif[0]
    for producto in prod_peor_calif:
        if producto[2] < calif_min:
           calif_min = producto[2]
           prod_calif_min = producto
    prod_peor_calif_ord.append(prod_calif_min)
    prod_peor_calif.remove(prod_calif_min)

# print(prod_mejor_calif_ord)
# print(len(prod_mejor_calif_ord))
# print(prod_peor_calif_ord)
# print(len(prod_peor_calif_ord))

# ------------------
# VENTAS E INGRESOS
# ------------------

# Se obtienen las ventas e ingresos por mes:
ingresos_ene = 0
ingresos_feb = 0
ingresos_mar = 0
ingresos_abr = 0
ingresos_may = 0
ingresos_jun = 0
ingresos_jul = 0
ingresos_ago = 0
ingresos_sep = 0
ingresos_oct = 0
ingresos_nov = 0
ingresos_dic = 0
ventas_ene = 0
ventas_feb = 0
ventas_mar = 0
ventas_abr = 0
ventas_may = 0
ventas_jun = 0
ventas_jul = 0
ventas_ago = 0
ventas_sep = 0
ventas_oct = 0
ventas_nov = 0
ventas_dic = 0
for venta in lifestore_sales:
    for producto in lifestore_products:
        if producto[0] == venta[1]:
            if venta[3][3:5] == '01':
                ventas_ene += 1
                ingresos_ene += producto[2]
            elif venta[3][3:5] == '02':
                ventas_feb += 1
                ingresos_feb += producto[2]
            elif venta[3][3:5] == '03':
                ventas_mar += 1
                ingresos_mar += producto[2]
            elif venta[3][3:5] == '04':
                ventas_abr += 1
                ingresos_abr += producto[2]
            elif venta[3][3:5] == '05':
                ventas_may += 1
                ingresos_may += producto[2]
            elif venta[3][3:5] == '06':
                ventas_jun += 1
                ingresos_jun += producto[2]
            elif venta[3][3:5] == '07':
                ventas_jul += 1
                ingresos_jul += producto[2]
            elif venta[3][3:5] == '08':
                ventas_ago += 1
                ingresos_ago += producto[2]
            elif venta[3][3:5] == '09':
                ventas_sep += 1
                ingresos_sep += producto[2]
            elif venta[3][3:5] == '10':
                ventas_oct += 1
                ingresos_oct += producto[2]
            elif venta[3][3:5] == '11':
                ventas_nov += 1
                ingresos_nov += producto[2]
            elif venta[3][3:5] == '12':
                ventas_dic += 1
                ingresos_dic += producto[2]
ventas_ingresos_mes = [['Enero', ventas_ene, ingresos_ene], 
                             ['Febrero', ventas_feb, ingresos_feb], 
                             ['Marzo', ventas_mar, ingresos_mar], 
                             ['Abril', ventas_abr, ingresos_abr],
                             ['Mayo', ventas_may, ingresos_may], 
                             ['Junio', ventas_jun, ingresos_jun],
                             ['Julio', ventas_jul, ingresos_jul], 
                             ['Agosto', ventas_ago, ingresos_ago],
                             ['Septiembre', ventas_sep, ingresos_sep], 
                             ['Octubre', ventas_oct, ingresos_oct],
                             ['Noviembre', ventas_nov, ingresos_nov], 
                             ['Diciembre', ventas_dic, ingresos_dic]]
ventas_ingresos_mensuales = [['Enero', ventas_ene, ingresos_ene], 
                             ['Febrero', ventas_feb, ingresos_feb], 
                             ['Marzo', ventas_mar, ingresos_mar], 
                             ['Abril', ventas_abr, ingresos_abr],
                             ['Mayo', ventas_may, ingresos_may], 
                             ['Junio', ventas_jun, ingresos_jun],
                             ['Julio', ventas_jul, ingresos_jul], 
                             ['Agosto', ventas_ago, ingresos_ago],
                             ['Septiembre', ventas_sep, ingresos_sep], 
                             ['Octubre', ventas_oct, ingresos_oct],
                             ['Noviembre', ventas_nov, ingresos_nov], 
                             ['Diciembre', ventas_dic, ingresos_dic]]

# Se ordenan las ventas por mes de mayor a menor:
ventas_ingresos_mes_ord = []
while ventas_ingresos_mes:
    num_vent_max = ventas_ingresos_mes[0][1]
    mes_vent_max = ventas_ingresos_mes[0]
    for ventas in ventas_ingresos_mes:
        if ventas[1] > num_vent_max:
            num_vent_max = ventas[1]
            mes_vent_max = ventas
    ventas_ingresos_mes_ord.append(mes_vent_max)
    ventas_ingresos_mes.remove(mes_vent_max)

# print(ventas_ingresos_mes_ord)

# Se obtienen las ventas promedio mensuales:
ventas_tot_anual = 0
for i in range(len(ventas_ingresos_mes_ord)):
    ventas_tot_anual += ventas_ingresos_mes_ord[i][1]
ventas_prom_mensual = int(ventas_tot_anual / 12)

# print(ventas_tot_anual)
# print(ventas_prom_mensual)

# Se obtienen los ingresos promedio mensuales:
ingresos_tot_anual = 0
for i in range(len(ventas_ingresos_mes_ord)):
    ingresos_tot_anual += ventas_ingresos_mes_ord[i][2]
ingresos_prom_mensual = int(ingresos_tot_anual / 12)

# print(ingresos_tot_anual)
# print(ingresos_prom_mensual)

# Se obtienen los meses con ventas mayores al promedio mensual:
meses_mas_ventas = []
for venta in ventas_ingresos_mes_ord:
    if venta[1] > ventas_prom_mensual:
        meses_mas_ventas.append(venta)

# print(meses_mas_ventas)



# -------------------
# ENTRADA AL SISTEMA
# -------------------

# Se definen los administradores:
admins = [['Karina', 'ls4515'], ['Edgar', 'ht7816'], ['Laura', 'kr9830']]

# Se realiza el Login al sistema:
print('\nLifeStore - Login')
usuario = input('Ingresa tu nombre de usuario: ')
password = input('Ingresa tu contraseña: ')

'''Se verifica que el usuario ingresado sea administrador y que la
   contraseña corresponda al mismo, y si no es así, se otorgan dos 
   oportunidades más para ingresar tanto el usuario como la contraseña:'''
j = 0
k = 0
m = 2
while k == 0 and j <= 2:
    for i in range(len(admins)):
        if usuario == admins[i][0]:
            k = 1
            break
        else:
            continue
    if k == 0 and j < 2:
        print('\nUsuario incorrecto, intente nuevamente.\nQueda(n) ' + str(m) + ' intento(s).')
        usuario = input('Ingresa tu nombre de usuario: ')
        password = input('Ingresa tu contraseña: ')
        j += 1
        m -= 1
    else:
        break
if k == 0:
    print('\nAcceso denegado. Se agotó el número de intentos permitidos.')
else:
    k = 0
    j = 0
    m = 2
    while j <= 2:
        if password == admins[i][1]:
            print('\n\n¡Bienvenido(a), ' + admins[i][0] + '!')
            k = 1
            break
        elif password != admins[i][1] and j < 2:
            print('\nContraseña incorrecta, intente nuevamente.\nQueda(n) ' + str(m) + ' intento(s).')
            password = input('Ingresa tu contraseña: ')
            j += 1
            m -= 1
        else:
            break
    if k == 0:
        print('\nAcceso denegado. Se agotó el número de intentos permitidos.')

# Si tanto el usuario como la contraseña son correctos, se otorga el acceso:
if k == 1:
    a = '1'
    while a == '1':    
        texto = '''
    ¿Qué información deseas consultar?
    
    Opciones:
           
    (1) Ventas y búsquedas (general y por categorías)
    (2) Productos por reseña en el servicio
    (3) Total de ingresos y ventas promedio mensuales, 
        total anual y meses con más ventas al año'''
        print (texto)
    
        '''Se pide la opción que el usuario desea consultar y si lo que se ingresa
           no está entre las opciones, se vuelve a pedir hasta que se ingrese una 
           opción correcta, posteriormente se muestra la información correspondiente:'''
        opc = input('Indique el número de opción deseada: ')
        while opc != '1' and opc != '2' and opc != '3':
            print('\nEntrada inválida, intente nuevamente.')
            opc = input('Indique el número de opción deseada (1, 2 o 3): ')
        opc = int(opc)
        if opc == 1:
            texto2 = '''
    ¿Qué información deseas consultar?
    
    Opciones:
           
    (1) Productos más vendidos y productos rezagados 
    (2) Productos más buscados y productos menos buscados 
    (3) Ventas por categoría
    (4) Búsquedas por categoría'''
            print(texto2)
            opc = input('Indique el número de opción deseada: ')
            while opc != '1' and opc != '2' and opc != '3' and opc != '4':
                print('\nEntrada inválida, intente nuevamente.')
                opc = input('Indique el número de opción deseada (1, 2, 3 o 4): ')
            opc = int(opc)
            if opc == 1:
                print('\n\nPRODUCTOS MÁS VENDIDOS:\n-----------------------')
                i = 1
                for prod in prod_mas_vendidos:
                    print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de ventas: ' + str(prod[2]))
                    i += 1
                print('\n\nPRODUCTOS REZAGADOS:\n--------------------')
                i = 1
                for prod in prod_rezagados:
                    print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de ventas: ' + str(prod[2]))
                    i += 1
                print('\n\n¿Deseas consultar más información?')
                a = input('Presiona "1" si tu respuesta es sí, o cualquier otra tecla para salir: ')
                if a != '1':
                    print('\nSe ha cerrado la sesión.')
            elif opc == 2:
                print('\n\nPRODUCTOS MÁS BUSCADOS:\n-----------------------')
                i = 1
                for prod in prod_mas_buscados:
                    print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de búsquedas: ' + str(prod[2]))
                    i += 1
                print('\n\nPRODUCTOS MENOS BUSCADOS:\n-------------------------')
                i = 1
                for prod in prod_menos_buscados:
                    print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de búsquedas: ' + str(prod[2]))
                    i += 1
                print('\n\n¿Deseas consultar más información?')
                a = input('Presiona "1" si tu respuesta es sí, o cualquier otra tecla para salir: ')
                if a != '1':
                    print('\nSe ha cerrado la sesión.')
            elif opc == 3:
                print('\n\nVENTAS POR CATEGORÍA (de mayor a menor):\n-----------------------------------------')
                j = 0
                categorias = ['PROCESADORES', 'TARJETAS DE VIDEO', 'TARJETAS MADRE', 'DISCOS DUROS', 'MEMORIAS USB', 'PANTALLAS', 'BOCINAS', 'AUDÍFONOS']
                for categoria in ventas_por_categoria:
                    i = 1
                    print('\nCATEGORÍA: ' + categorias[j])
                    for prod in categoria:
                        print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de ventas: ' + str(prod[2]))
                        i += 1
                    j += 1
                print('\n\nVENTAS POR CATEGORÍA (de menor a mayor):\n-----------------------------------------')
                j = 0
                for categoria in ventas_por_categoria_rev:
                    i = 1
                    print('\nCATEGORÍA: ' + categorias[j])
                    for prod in categoria:
                        print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de ventas: ' + str(prod[2]))
                        i += 1
                    j += 1
                print('\n\n¿Deseas consultar más información?')
                a = input('Presiona "1" si tu respuesta es sí, o cualquier otra tecla para salir: ')
                if a != '1':
                    print('\nSe ha cerrado la sesión.')
            elif opc == 4:
                print('\n\nBÚSQUEDAS POR CATEGORÍA (de mayor a menor):\n--------------------------------------------')
                j = 0
                categorias = ['PROCESADORES', 'TARJETAS DE VIDEO', 'TARJETAS MADRE', 'DISCOS DUROS', 'MEMORIAS USB', 'PANTALLAS', 'BOCINAS', 'AUDÍFONOS']
                for categoria in busquedas_por_categoria:
                    i = 1
                    print('\nCATEGORÍA: ' + categorias[j])
                    for prod in categoria:
                        print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de búsquedas: ' + str(prod[2]))
                        i += 1
                    j += 1
                print('\n\nBÚSQUEDAS POR CATEGORÍA (de menor a mayor):\n--------------------------------------------')
                j = 0
                for categoria in busquedas_por_categoria_rev:
                    i = 1
                    print('\nCATEGORÍA: ' + categorias[j])
                    for prod in categoria:
                        print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Número de búsquedas: ' + str(prod[2]))
                        i += 1
                    j += 1
                print('\n\n¿Deseas consultar más información?')
                a = input('Presiona "1" si tu respuesta es sí, o cualquier otra tecla para salir: ')
                if a != '1':
                    print('\nSe ha cerrado la sesión.')
        elif opc == 2:
            print('\n\nPRODUCTOS CON MEJORES RESEÑAS:\n-------------------------------')
            i = 1
            for prod in prod_mejor_calif_ord:
                print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Promedio de reseñas (1-5): ' + str(prod[2]))
                i += 1
            print('\n\nPRODUCTOS CON PEORES RESEÑAS:\n------------------------------')
            i = 1
            for prod in prod_peor_calif_ord:
                print('\n' + str(i) + '. Nombre del producto: ' + prod[1] + ' | Promedio de reseñas (1-5): ' + str(prod[2]))
                i += 1
            print('\n\n¿Deseas consultar más información?')
            a = input('Presiona "1" si tu respuesta es sí, o cualquier otra tecla para salir: ')
            if a != '1':
                print('\nSe ha cerrado la sesión.')
        elif opc == 3:
            print('\n\nTOTAL VENTAS ANUALES (2020): '+ str(ventas_tot_anual) + '\n----------------------------')
            print('\n\nINGRESOS ANUALES (2020): $ ' + str(ingresos_tot_anual) + '\n------------------------')
            print('\n\nVENTAS E INGRESOS POR MES:\n--------------------------')
            for mes in ventas_ingresos_mensuales:
                print('Mes: ' + mes[0] + ' | Número de ventas: ' + str(mes[1]) + ' | Ingresos: $ ' + str(mes[2]))      
            print('\n\nVENTAS E INGRESOS PROMEDIO MENSUALES:\n-------------------------------------\nPromedio ventas: ' + str(ventas_prom_mensual) + ' | Promedio ingresos: $ ' + str(ingresos_prom_mensual))
            print('\n\nMESES CON MÁS VENTAS:\n---------------------')
            for mes in meses_mas_ventas:
                print('Mes: ' + mes[0] + ' | Número de ventas: ' + str(mes[1]))
            print('\n\n¿Deseas consultar más información?')
            a = input('Presiona "1" si tu respuesta es sí, o cualquier otra tecla para salir: ')
            if a != '1':
                print('\nSe ha cerrado la sesión.')
