from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

#----------------------------------------------------------------------------------------------------#

operador = ''
precios_comida = [1.32,1.65,2.31,3.22,1.22]
precios_bebida = [0.25,0.99,1.21,1.54,1.08]
precios_postre = [1.54,1.68,1.32,1.97,2.55]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador = 0
    visor_calculadora.delete(0,END)

def resultado():
    global operador
    res = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,res)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0,END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def total_final():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1

    sub_total = subtotal_bebida + subtotal_comida + subtotal_postre
    impuesto = sub_total * 0.07
    total = sub_total + impuesto

    var_costo_comida.set(f'$ {round(subtotal_comida,2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida,2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre,2)}')
    var_subtotal.set(f'${round(sub_total,2)}')
    var_impuesto.set(f'${round(impuesto,2)}')
    var_total.set(f'${round(total,2)}')

def recibo():
    texto_recibo.delete(1.0,END)
    numero_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}')
    texto_recibo.insert(END,f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant. \tCosto Items\n')
    texto_recibo.insert(END,f'-'*54 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != 0:
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != 0:
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    
    x = 0
    for postre in texto_postre:
        if postre.get() != 0:
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t${int(postre.get()) * precios_postre[x]}\n')
        x += 1

    texto_recibo.insert(END,f'-'*54+'\n')
    texto_recibo.insert(END,f'Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END,f'Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END,f'Costo del Postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END,f'-'*54+'\n')
    texto_recibo.insert(END,f'Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END,f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END,f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END,f'-'*54+'\n')

def guardar():
    info_recibo = texto_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','Su recibo a sido guardado')

def resetear():
    texto_recibo.delete(0.1,END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
        
#----------------------------------------------------------------------------------------------------#

# Iniciar tkinter
aplicacion = Tk()

# Tamanio de la ventana
aplicacion.geometry('1280x720+0+0')

# Evitar agrandar ventana
aplicacion.resizable(0,0)

# Titulo ventana
aplicacion.title('Sistema de facturacion, Dan proyect')

# Color de fondo
aplicacion.config(bg='burlywood')

#----------------------------------------------------------------------------------------------------#

# Panel superior
panel_superior = Frame(aplicacion,bd=1,relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior,text='Sistema de Facturacion',fg='azure4',
                        font=('Arial', 58),bg='burlywood', width=27)
etiqueta_titulo.grid(row=0,column=0)

# Panel izquierdo

panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT,bg='azure4',padx=40)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida',font=('Dosis',19,'bold'),
                            bd=1,relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas',font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres',font=('Dosis',19,'bold'),
                          bd=1,relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_botones.pack()

# Lista de productos
lista_comidas = ['Pollo','Cordero','Pescado','Pizza','Cerdo']
lista_bebidas = ['Vino','Cerveza','Soda','Agua','Gaseosa']
lista_postres = ['Torta','Helado','Flan','Fruta','Licores']

#----------------------------------------------------------------------------------------------------#

# Generar items comida

variables_comida = []

cuadros_comida = []

texto_comida = []

contador = 0

for comida in lista_comidas:
    
    # Crear checkbuttons
    
    variables_comida.append('')
    
    variables_comida[contador] = IntVar()
    
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0, 
                         variable=variables_comida[contador],
                         command=revisar_check)
    
    comida.grid(row=contador,
                column=0,
                sticky=W)
    
    # Crear los cuadros de entrada
    
    cuadros_comida.append('')
    
    texto_comida.append('')

    texto_comida[contador] = StringVar()

    texto_comida[contador].set('0')
    
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable = texto_comida[contador])
    
    cuadros_comida[contador].grid(row=contador,
                                  column=1,
                                  sticky=W)
    
    contador += 1

#----------------------------------------------------------------------------------------------------#

# Generar items bebida

variables_bebida = []

cuadros_bebida = []

texto_bebida = []

contador = 0

for bebida in lista_bebidas:
    
    # Crear checkbuttons
    
    variables_bebida.append('')
    
    variables_bebida[contador] = IntVar()
    
    bebida = Checkbutton(panel_bebidas,
                        text=bebida.title(),
                        font=('Dosis',19,'bold'),
                        onvalue=1,
                        offvalue=0, 
                        variable=variables_bebida[contador],
                        command=revisar_check)
    
    bebida.grid(row=contador,
                column=0,
                sticky=W)
    
    # Crear los cuadros de entrada
    
    cuadros_bebida.append('')
    
    texto_bebida.append('')

    texto_bebida[contador] = StringVar()

    texto_bebida[contador].set('0')
    
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable = texto_bebida[contador])
    
    cuadros_bebida[contador].grid(row=contador,
                                  column=1,
                                  sticky=W)
    
    contador += 1

#----------------------------------------------------------------------------------------------------#

# Generar items postres

variables_postre = []

cuadros_postre = []

texto_postre = []

contador = 0

for postre in lista_postres:

    # Crear checkbuttons
    
    variables_postre.append('')
    
    variables_postre[contador] = IntVar()
    
    postre = Checkbutton(panel_postres,
                         text=postre.title(), 
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0, 
                         variable=variables_postre[contador],
                         command=revisar_check)
    
    postre.grid(row=contador, column=0,sticky=W)
    
    # Crear los cuadros de entrada
    
    cuadros_postre.append('')
    
    texto_postre.append('')

    texto_postre[contador] = StringVar()

    texto_postre[contador].set('0')
    
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable = texto_postre[contador])
    
    cuadros_postre[contador].grid(row=contador,
                                  column=1,
                                  sticky=W)
    
    contador += 1

#----------------------------------------------------------------------------------------------------#

# Variables

var_costo_comida = StringVar()

# Etiquetas de costo y campos de entrada

etiqueta_costo_comida = Label(panel_costos,
                                text='Costo Comida',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')

etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_comida)

texto_costo_comida.grid(row=0,column=1)

#----------------------------------------------------------------------------------------------------#

# Subtotal comida

# Variables

var_costo_bebida = StringVar()

# Etiquetas de costo y campos de entrada

etiqueta_costo_bebida = Label(panel_costos,
                                text='Costo bebida',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')

etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1,column=1,padx=41)

#----------------------------------------------------------------------------------------------------#

# Subtotal bebida

# Variables

var_costo_postre = StringVar()

# Etiquetas de costo y campos de entrada

etiqueta_costo_postre = Label(panel_costos,
                                text='Costo postre',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')

etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_postre)

texto_costo_postre.grid(row=2,column=1,padx=41)

#----------------------------------------------------------------------------------------------------#

# Subtotal postre

# Variables

var_subtotal = StringVar()

# Etiquetas de costo y campos de entrada

etiqueta_subtotal = Label(panel_costos,
                                text='Subtotal',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')

etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_subtotal)

texto_subtotal.grid(row=0,column=3,padx=41)

#----------------------------------------------------------------------------------------------------#

# Subtotal

# Variables

var_impuesto = StringVar()

# Etiquetas de costo y campos de entrada

etiqueta_impuesto = Label(panel_costos,
                                text='Impuesto',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')

etiqueta_impuesto.grid(row=1,column=2)

texto_impuesto = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_impuesto)

texto_impuesto.grid(row=1,column=3,padx=41)

#----------------------------------------------------------------------------------------------------#

# Impuesto

# Variables

var_total = StringVar()

# Etiquetas de costo y campos de entrada

etiqueta_total = Label(panel_costos,
                                text='Total',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')

etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_total)

texto_impuesto.grid(row=2,column=3,padx=41)

#----------------------------------------------------------------------------------------------------#

# Total

# Botones

botones = ['total','recibo','guardar', 'resetear']

botones_creados = []

columnas = 0

for boton in botones:
    
    boton = Button(panel_botones,
                    text = boton.title(),
                    font=('Dosis',14,'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=9)

    botones_creados.append(boton)

    boton.grid(row=0,column=columnas)

    columnas += 1

botones_creados[0].config(command=total_final)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)



# Area de recibo

texto_recibo = Text(panel_recibo,
                    font=('Dosis',14,'bold'),
                    bd=1,
                    width=42,
                    height=10)

texto_recibo.grid(row=0,column=0)

#----------------------------------------------------------------------------------------------------#

# Calculadora

visor_calculadora = Entry(panel_calculadora,
                            font=('Dosis',16,'bold'),
                            width=32,
                            bd=1)

visor_calculadora.grid(row=0,column=0,columnspan=4)

botones_calculadora = ['7','8','9', '+','4','5','6','-','1','2','3','x','R','B','0','/']

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                    text=boton.title(),
                    font=('Dosis',16,'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8)
    
    botones_guardados.append(boton)

    boton.grid(row=fila,column=columna)

    if columna == 3:
        fila += 1
    
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=resultado)   
botones_guardados[13].config(command=borrar)   
botones_guardados[14].config(command=lambda : click_boton('0'))   
botones_guardados[15].config(command=lambda : click_boton('/'))

#----------------------------------------------------------------------------------------------------#

# Evitar que la pantalla se cierre

aplicacion.mainloop()