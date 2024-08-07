import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame

pygame.init() #---> Traigo todas las herramientas de pygame

#------------------------------------------------------------------------------------------#
# Crear pantalla

pantalla = pygame.display.set_mode((1280,900)) #---> Declaro el tamanio de la pantalla

#------------------------------------------------------------------------------------------#
# Titulo e icono

# Titulo
pygame.display.set_caption('Dragon Lore Dan Proyect')

# Icono
icono = pygame.image.load('Practices\\Practice10\\icono.png')
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load('Practices\\Practice10\\ocean.jpeg')
# Redimensiono la imagen
fondo_redimensionado = pygame.transform.scale(fondo,(1280,900))

#------------------------------------------------------------------------------------------#
# Musica

mixer.music.load('Practices\\Practice10\\cancion.mp3')
mixer.music.play(-1)

#------------------------------------------------------------------------------------------#
# Jugador

# Imagen del jugador
img_jugador = pygame.image.load('Practices\\Practice10\\dragon.png')

# Redimensiono la imagen
img_jugador_redimensionada = pygame.transform.scale(img_jugador,(150,150))

# Ubicacion y variables del jugador
jugador_x = 590
jugador_y = 700
jugador_x_cambio = 0

# Funcion del jugador
def jugador(x,y):
    pantalla.blit(img_jugador_redimensionada, (x,y))

#------------------------------------------------------------------------------------------#
# Enemigos

img_enemigo_redimensionada = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

# Imagen del enemigo
img_enemigo = pygame.image.load('Practices\\Practice10\\dragon rojo.png')

# Ubicacion y variables del enemigo
for e in range(cantidad_enemigos): 
    img_enemigo_redimensionada.append(pygame.transform.scale(img_enemigo,(150,150)))
    enemigo_x.append(random.randint(0,1130))
    enemigo_y.append(random.randint(0,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Funcion del enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo_redimensionada[ene], (x,y))

#------------------------------------------------------------------------------------------#
# Disparos

# Imagen del disparo
img_disparo = pygame.image.load('Practices\\Practice10\\bola de fuego.png')

# Redimensiono la imagen
img_disparo_redimensionada = pygame.transform.scale(img_disparo,(75,75))

# Ubicacion y variables del disparo
disparo_x = 0
disparo_y = 700
disparo_x_cambio = 0
disparo_y_cambio = 2
disparo_visible = False

# Funcion del disparo
def disparo(x,y):
    global disparo_visible
    disparo_visible = True
    pantalla.blit(img_disparo_redimensionada, (x + 37.5,y))

#------------------------------------------------------------------------------------------#
# Colisiones

def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2)+ math.pow(y_1-y_2,2))
    if distancia < 37.5:
        return True
    else:
        return False

#------------------------------------------------------------------------------------------#
# Puntaje

puntaje = 0
fuente = pygame.font.Font('Practices\\Practice10\\textfont.ttf',32)
texto_x = 10
texto_y = 10

def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    pantalla.blit(texto,(x,y))

#------------------------------------------------------------------------------------------#

# Final de juego
fuente_final = pygame.font.Font('Practices\\Practice10\\textfont.ttf',64)

def texto_final():
    mi_fuente_final = fuente_final.render('Game Over',True,(255,255,255))
    pantalla.blit(mi_fuente_final,(640,500))


#------------------------------------------------------------------------------------------#
# Loop del juego

se_ejecuta = True
while se_ejecuta:
    
    # Agregar color de fondo
    pantalla.fill((0, 0, 0))
    # Agregar un fondo para el terreno
    #pantalla.blit(fondo_redimensionado,(0,0))

    # Traigo todos los eventos de pygame
    for evento in pygame.event.get():
        
        # Evento para el boton cruz de la ventana
        if evento.type == pygame.QUIT:
            se_ejecuta = False #---> Le asigno el valor para terminar el loop del juego

        # Evento de presion de tecla
        if evento.type == pygame.KEYDOWN:
            
            if evento.key == pygame.K_LEFT: #---> Tecla flecha izquierda
                print('flecha izquierda presionada')
                jugador_x_cambio = -1 #---> Le asigno cambio de valor a la presion de tecla
            
            if evento.key == pygame.K_RIGHT: #---> Tecla flecha derecha
                print('flecha derecha presionada')
                jugador_x_cambio = 1 #---> Le asigno cambio de valor a la presion de tecla
            
            if evento.key == pygame.K_SPACE:
                if not disparo_visible:
                    disparo_x = jugador_x
                    disparo(disparo_x,disparo_y)
                    sonido_disparo = mixer.Sound('Practices\\Practice10\\bola de fuego.mp3')
                    sonido_disparo.play()
        #Evento de soltar tecla
        if evento.type == pygame.KEYUP:
            
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                print('la flecha se solto')
                jugador_x_cambio = 0

    
    # Declarando limites del jugador en la ventana
    if jugador_x <= -30:
        jugador_x = 0
    if jugador_x >= 1160:
        jugador_x = 1130
    
    # Modificar ubicacion jugador
    jugador_x += jugador_x_cambio
    jugador(jugador_x,jugador_y)

    for e in range(cantidad_enemigos):
    
        # Modificar ubicacion enemigo
        enemigo_x[e] += enemigo_x_cambio[e]
        enemigo(enemigo_x[e],enemigo_y[e],e)
        
        # Perder
        if enemigo_y[e] > 650:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 2000
            texto_final()
            break

        # Declarando limites del enemigo en la ventana
        if enemigo_x[e] <= -30:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] >= 1160:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # Verificar colision
        colision = hay_colision(enemigo_x[e],enemigo_y[e],disparo_x,disparo_y)
        if colision:
            disparo_y = 700
            disparo_visible = False
            puntaje += 50
            print(puntaje)
            enemigo_x[e] = random.randint(0,1130)
            enemigo_y[e] = random.randint(0,200)
            sonido_colision = mixer.Sound('Practices\Practice10\dragon muere.mp3')
            sonido_colision.play()

    # Movimiento disparo
    if disparo_y <= -75:
        disparo_y = 700
        disparo_visible = False

    if disparo_visible:
        disparo(disparo_x,disparo_y)
        disparo_y -= disparo_y_cambio

    # Mostrar puntaje
    mostrar_puntaje(texto_x,texto_y)

    # Actualizar ventana
    pygame.display.update()