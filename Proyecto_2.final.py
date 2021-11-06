import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import math
import sys
import os

formato_tabla = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


#  ------------------------- El siguiente es el algoritmo básico del juego 2048 ---------------------------

#  Reiniciar
def reiniciar():
    "Restablezca los datos del juego, restaure el mapa al estado inicial y agregue dos datos 2 para reproducir el estado inicial"
    formato_tabla[:] = []  # formato_tabla.clear()
    formato_tabla.append([0, 0, 0, 0])
    formato_tabla.append([0, 0, 0, 0])
    formato_tabla.append([0, 0, 0, 0])
    formato_tabla.append([0, 0, 0, 0])
    #  Llene dos 2 en el mapa en blanco
    llenar_2_4()
    llenar_2_4()


#  Obtener 0 recuento
def espacios_vacios():
    """Obtén el número de casillas sin números. Si el número es 0, significa que no se pueden completar nuevos datos y el juego está a punto de terminar.
    """
    contador = 0
    for r in formato_tabla:
        contador += r.count(0)
    return contador


#  Calcular la puntuación
def puntuacion():
    """
    Para obtener la puntuación del juego, la regla de puntuación es que cada vez que se suman dos números, se generará la puntuación correspondiente.
         Por ejemplo, 2 y 2 se comensaje_perdioinan para obtener 4 puntos, y 8 y 8 se comensaje_perdioinan para obtener 16 puntos.
         Según un número mayor que 2, puede saber cuántas veces se ha fusionado y puede calcular directamente la puntuación:
         Como: 
               4 debe comensaje_perdioinarse con dos 2 para obtener 4 puntos
               8 debe comensaje_perdioinarse con dos 4, luego contar: 8 + 4 + 4 obtienen 32 puntos
               ... y así
    """
    puntos = 0
    for r in formato_tabla:
        for c in r:
            puntos += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))
    return puntos  #  Importar módulo de matemáticas


#  Generación de números aleatorios
def llenar_2_4():
    #Llene 2 a la posicionición vacía, si el llenado es exitoso, devuelva Verdadero, si está lleno, devuelva Falso"
    espacios_0 = espacios_vacios()  #  Obtenga el número de ubicaciones en blanco en el mapa
    if 0 == espacios_0:
        return False
    #  Genere posicioniciones aleatorias, por ejemplo, cuando solo hay cuatro espacios vacíos, genere un número de 0 a 3, que represente posicioniciones vacías de izquierda a derecha y de arriba a abajo
    posicion = random.randrange(0, espacios_0)
    nuevo_set = 0
    for fila in formato_tabla:  #  fila es fila
        for columna in range(4):  #  columna es la column=a, column=a
            if 0 == fila[columna]:
                if nuevo_set == posicion:
                    #  Complete 2 en la posicionición de la column=a de la fila y la column=a, y devuelva True
                    fila[columna] = 2
                    return True
                nuevo_set += 1


#  Fin del juicio
def verifica_si_perdio():
    """Determine si el juego terminó, si terminó, devuelva True, si no, devuelva False
    """
    for r in formato_tabla:
        if r.count(0):
            return False
        for i in range(3):
            if r[i] == r[i + 1]:
                return False
    for c in range(4):
        for r in range(3):
            if formato_tabla[r][c] == formato_tabla[r + 1][c]:
                return False
    return True


#  Mover puntuación comensaje_perdioinada
def mover_num_izq(linea):
    
    movimiento = False  #  Ya sea para mover el logo, primero asuma que no hay movimiento
    for g in range(3):  #  Repite el siguiente algoritmo tres veces
        for i in range(3):  #  yo es el índice
            if 0 == linea[i]:  #  Aquí hay un espacio, el número adyacente de la derecha se mueve hacia la izquierda y el de la derecha está en blanco
                movimiento = True
                linea[i] = linea[i + 1]
                linea[i + 1] = 0
    return movimiento


#  mover lugar
def suma_izq(linea):
    """
    Comensaje_perdioine las mismas celdas a la izquierda, columnaoque el resultado comensaje_perdioinado a la izquierda y ceros rellenos a la derecha
         Por ejemplo: línea = [2, 2, 4, 4] significa la siguiente línea:
        +---+---+---+---+
        | 2 | 2 | 4 | 4 |
        +---+---+---+---+
         El resultado tras la fusión es:
        +---+---+---+---+
        | 4 | 0 | 8 | 0 |
        +---+---+---+---+
         Resultado final: línea = [4, 8, 8, 0]
    """
    for i in range(3):
        if linea[i] == linea[i + 1]:
            movimiento = True
            linea[i] *= 2  #  Doble a la izquierda
            linea[i + 1] = 0  #  Cero a la derecha


#  Lógica móvil
def mov_en_linea(linea):
    movimiento = False
    if mover_num_izq(linea):
        movimiento = True
    if suma_izq(linea):
        movimiento = True
    if mover_num_izq(linea):
        movimiento = True
    return movimiento


def izquierda():
    """Algoritmo cuando se presiona el botón izquierdo del juego o cuando se desliza la pantalla hacia la izquierda"""
    movimiento = False  #  movimiento Si la bandera digital se mueve con éxito, si se mueve, es verdadera y el mapa original no camensaje_perdioia, es falsa

    #  Mueve la primera fila a la izquierda. Si hay movimiento, devuelve True
    for linea in formato_tabla:
        if mov_en_linea(linea):
            movimiento = True
    return movimiento


def derecha():
    """Algoritmo cuando se hace clic con el botón derecho en el juego o cuando se desliza la pantalla hacia la derecha
         Elija intercamensaje_perdioiar la pantalla de izquierda a derecha, después del intercamensaje_perdioio, el deslizamiento original hacia la derecha es el deslizamiento actual hacia la izquierda
         Después de deslizar, vuelve a camensaje_perdioiar
    """
    #  Camensaje_perdioiar de izquierda a derecha
    for r in formato_tabla:
        r.reverse()
    movimiento = izquierda()  #  Deslizar a la izquierda
    #  Camensaje_perdioiar de izquierda a derecha de nuevo
    for r in formato_tabla:
        r.reverse()
    return movimiento


def arriba():
    """El algoritmo cuando se presiona la tecla del juego o cuando se desliza la pantalla hacia arriba
         Primero columnaoque cada column=a de arriba a abajo en una línea de lista y luego realice una dirección de deslizamiento,
         Una vez completado el deslizamiento, vuelva a columnaocar la nueva posicionición en la column=a original
    """
    movimiento = False
    linea = [0, 0, 0, 0]  #  Primero inicialice una fila, prepárese para poner datos
    for columna in range(4):  #  Saque cada column=a primero
        #  Cuente cada fila en una column=a en la línea
        for fila in range(4):
            linea[fila] = formato_tabla[fila][columna]
        #  Mueve la column=a actual hacia arriba, es decir, mueve la línea hacia la izquierda
        if (mov_en_linea(linea)):
            movimiento = True
        #  Complete los datos en la línea desplazada a la izquierda de nuevo a la column=a original
        for fila in range(4):
            formato_tabla[fila][columna] = linea[fila]
    return movimiento


def abajo():
    """Algoritmo cuando se presiona el botón del juego o cuando se desliza la pantalla hacia abajo
         Elija camensaje_perdioiar la pantalla hacia arriba y hacia abajo, después del intercamensaje_perdioio, el deslizamiento hacia abajo original es el deslizamiento hacia arriba actual
         Después de deslizar, camensaje_perdioie de un lado a otro nuevamente
    """
    formato_tabla.reverse()
    movimiento = arriba()  #  Deslizar hacia arriba
    formato_tabla.reverse()
    return movimiento


# ------------------------- La siguiente es la interfaz de operación del juego 2048 ------------------ ---------


def juego2048():
    reiniciar()  #  Primero restablece los datos del juego

    root = Tk()  #  Crear ventana tkinter
    root.title("Juego 2048")  #  Establecer el texto del título
    root.resizable(False,False)  #  Ancho y alto fijo
    #  La siguiente es la asignación de teclado
    mapeado_teclas = {
        "Left": izquierda,
        "Right": derecha,
        "Up": arriba,
        "Down": abajo,
    }

    game_bg_columnaor = "#999999"  #  Establecer columnaor de fondo

    #  Establecer el columnaor de cada dato correspondiente al bloque de columnaor en el juego
    colores = {
        0: ("#cdc1b4", "#776e65"),
        2: ("#eee4da", "#776e65"),
        4: ("#ede0c8", "#f9f6f2"),
        8: ("#f2b179", "#f9f6f2"),
        16: ("#f59563", "#f9f6f2"),
        32: ("#f67c5f", "#f9f6f2"),
        64: ("#f65e3b", "#f9f6f2"),
        128: ("#edcf72", "#f9f6f2"),
        256: ("#edcc61", "#f9f6f2"),
        512: ("#e4c02a", "#f9f6f2"),
        1024: ("#e2ba13", "#f9f6f2"),
        2048: ("#ecc400", "#f9f6f2"),
        4096: ("#ae84a8", "#f9f6f2"),
        8192: ("#b06ca8", "#f9f6f2"),
        #  ---- Otros columnaores son los mismos que 8192 ---------
        2 ** 14: ("#b06ca8", "#f9f6f2"),
        2 ** 15: ("#b06ca8", "#f9f6f2"),
        2 ** 16: ("#b06ca8", "#f9f6f2"),
        2 ** 17: ("#b06ca8", "#f9f6f2"),
        2 ** 18: ("#b06ca8", "#f9f6f2"),
        2 ** 19: ("#b06ca8", "#f9f6f2"),
        2 ** 20: ("#b06ca8", "#f9f6f2"),
    }

    def tecleado(event):
        "Función de procesamiento de pulsaciones de teclado"
        keysym = event.keysym
        if keysym in mapeado_teclas:
            if mapeado_teclas[keysym]():  #  Si hay números moviéndose
                llenar_2_4()  #  Llene un nuevo 2
        actualizar_interfaz()
        
        if verifica_si_perdio():
            mensaje_perdio = messagebox.askyesno(
                title="Has perdido", message=" ¡El juego ha terminado! ")
            if mensaje_perdio:
                root.quit()
            else:
                reiniciar()
                actualizar_interfaz()

    def actualizar_interfaz():
        """
        Actualizar función de interfaz
                 Actualice la configuración de cada etiqueta de acuerdo con los datos del mapa f calculados
        """
        for r in range(4):
            for c in range(len(formato_tabla[0])):
                numero = formato_tabla[r][c]  #  Establecer número
                label = etiquetas[r][c]  #  Seleccione el control Lable
                label["text"] = str(numero) if numero else ""
                label["bg"] = colores[numero][0]
                label["foreground"] = colores[numero][1]
        label_puntos["text"] = str(puntuacion())  #  Restablecer puntuación

    #  Cree una ventana de marco, esta creación contendrá todas las partes del widget
    frame = Frame(root, bg=game_bg_columnaor)
    frame.grid(sticky=N + E + W + S)
    #  Establezca el enfoque para recibir movos clave
    frame.focus_set()
    frame.bind("<Key>", tecleado)

    #  Inicializar la interfaz gráfica
    
    etiquetas = []
    for r in range(4):
        row = []
        for c in range(len(formato_tabla[0])):
            value = formato_tabla[r][c]
            text = str(value) if value else ""
            label = Label(frame, text=text, width=4, height=2,
                        font=("Times New Roman", 30, "bold"))
            label.grid(row=r, column=c, padx=5, pady=5, sticky=N + E + W + S)
            row.append(label)
        etiquetas.append(row)

    #  Establecer la etiqueta para mostrar la puntuación
    label = Label(frame, text="Puntuación", font=("Times New Roman", 12, "bold"),
                  bg="#bbada0", fg="#fc0320")
    label.grid(row=5, column=1, padx=3, pady=3)
    
    label_puntos = Label(frame, text="0", font=("Times New Roman", 16, "bold"),
                        bg="#bbada0", fg="black")
    label_puntos.grid(row=4, columnspan=1, column=1, padx=5, pady=5)
    

    #  Configure el botón de reinicio a continuación
    def salir():
        root.destroy()
        
    def reiniciar_juego():
        reiniciar()
        actualizar_interfaz()
        
    boton_iniciar_partida = Button(frame, text="Iniciar\npartida.", font=("Times New Roman", 12, "bold"),
                  bg="#FF5454", fg="black")
    boton_iniciar_partida.grid(row=4, column=0, padx=5, pady=5)
    
    label_indicaciones = Label(frame, text="Teclas\n↑ ← ↓ →\n mueven las\ncasillas.", font=("Times New Roman", 12, "bold"),
                  bg="#bbada0", fg="black")
    label_indicaciones.grid(row=8, column=0, padx=5, pady=5)
    
    inicio_boton = Button(frame, text="Iniciar\npartida", font=("Times New Roman", 12, "bold"),
                            bg="#8f7a66", fg="black")
    inicio_boton.grid(row=4, column=3, padx=5, pady=5)
    
    restart_button = Button(frame, text="Partida\nnueva", font=("Times New Roman", 12, "bold"),
                            bg="#8f7a66", fg="black", command=reiniciar_juego)
    restart_button.grid(row=4, column=3, padx=5, pady=5)
    
    salir_boton = Button(frame, text="Salir", font=("Times New Roman", 12, "bold"),
                            bg="#8f7a66", fg="black", command=salir)
    salir_boton.grid(row=8, column=3, padx=5, pady=5)
    
    partida_nueva_boton = Button(frame, text="Partida\nnueva", font=("Times New Roman", 12, "bold "),
                            bg="#8f7a66", fg="black", )
    partida_nueva_boton.grid(row=9, column=3, padx=5, pady=5)
    
    
    
    

    actualizar_interfaz()  #  Interfaz de actualización

    root.mainloop()  #  Ingrese al bucle de movos principal de tkinter
    
def ayuda():
    """
    Entradas: no posee entradas
    Función: despliega el manual de ayuda
    Salidas: el manual de ayuda
    """
    #Abre pdf de ayuda
    import subprocess
    path = "manual_de_usuario_calificaciones_admisión.pdf"
    subprocess.Popen([path], shell=True)
    
    
def acerca_de():
    acerca_de = tk.Tk()
    acerca_de.title("JUEGO 2048 - AYUDA")
    acerca_de.geometry("800x500")

    acercade =          tk.Label(acerca_de,text="Acerca del Programa",      font=("Times New Roman",16,"bold")).place(x=350,y=30)
    creado_por =        tk.Label(acerca_de,text="Autor del Programa:",      font=("Times New Roman",16,"bold")).place(x=20,y=60)
    nombre_creador =    tk.Label(acerca_de,text="Helberth Cubillo Jarquín", font=("Times New Roman",16)).place(x=330,y=60)
    nombre_proyecto =   tk.Label(acerca_de,text="Nombre del programa:",     font=("Times New Roman",16,"bold")).place(x=20,y=90)
    nombre =            tk.Label(acerca_de,text="JUEGO 2048",               font=("Times New Roman",16)).place(x=330,y=90)
    version_programa =  tk.Label(acerca_de,text="Versión:",                 font=("Times New Roman",16,"bold")).place(x=20,y=120)
    version =           tk.Label(acerca_de,text="Python 3.9.6",             font=("Times New Roman",16)).place(x=330,y=120)
    fecha_de_creacion = tk.Label(acerca_de,text="Fecha de creación:",       font=("Times New Roman",16,"bold")).place(x=20,y=150)
    creacion =          tk.Label(acerca_de,text="10 de octubre del 2021",   font=("Times New Roman",16)).place(x=330,y=150)

    def salir():
        acerca_de.destroy()
        
    botonSalir =        tk.Button(acerca_de,text="SALIR",command=salir,bg="#34ebc3",font=("Times New Roman",12),height=2,width=6)
    botonSalir.place(x= 20,y=200)
    

    

def salir_del_programa():
    respuesta= messagebox.askyesno("Atención", "¿Realmente quiere salir del programa?")
    if respuesta == True:
        pantalla_principal.destroy()

def configuracion():
    acerca_de = tk.Tk()
    acerca_de.title("Configuraciones")
    acerca_de.geometry("800x500")



#Pantalla principal del juego.
#--------------------------------------------------------------------#
pantalla_principal = tk.Tk()  
pantalla_principal.geometry("600x200") 
pantalla_principal.title("JUEGO 2048")  
pantalla_principal.resizable(False,False)  



ventana = tk.Label(pantalla_principal,text = "Menu principal",bg ="#34eb43").pack(fill=tk.X)   

#Barra de Menu
barra_menu = tk.Menu(pantalla_principal)

barra_menu.add_command(label="Jugar",   command=juego2048)

barra_menu.add_cascade(label="Configuracion", command= configuracion)
barra_menu.add_command(label="Ayuda",    command= ayuda)
barra_menu.add_command(label="Acerca de",command= acerca_de)
barra_menu.add_command(label="Salir",    command= salir_del_programa)

pantalla_principal.config(menu=barra_menu)

pantalla_principal.mainloop()


"""
prueba 2
"""