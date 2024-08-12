import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar el mic y devolver el audio como texto

def transformar_audio_en_texto():

    # almacenar recognizer en variable

    r = sr.Recognizer()

    # configurar microfono

    with sr.Microphone() as origen:

        # tiempo de espera

        r.pause_threshold = 0.8

        # informar que comenzo la grabacion

        print('Ya puedes hablar')

        # guardar lo que escuche como audio

        audio = r.listen(origen)

        try:
            # buscar en google lo que escucho

            pedido = r.recognize_google(audio, language = 'es-ar')

            # prueba de que pudo ingresar

            print('Dijiste: '+ pedido)

            # devolver pedido

            return pedido

        # caso de no poder devolver resultado

        except sr.UnknownValueError:

            # prueba de no comprension del audio

            print('Ups, no pude entender lo que dijiste')

            # devolver error

            return 'Sigo esperando'

        # En caso de no resolver el pedido

        except sr.RequestError:

            # prueba de que no comprendio el audio

            print('Ups, no hay servicio')

            # devolver error

            return 'Sigo esperando'

        # Error inesperado

        except:

            # prueba de que no comprendio el audio
            
            print('Ups, algo a salido mal')

            # devolver error

            return 'Sigo esperando'

# Funcion para que el asistente pueda ser escuchado

def hablar(mensaje):

    # encender el motor de pyttsx3

    engine = pyttsx3.init()

    # pronunciar mensaje

    engine.say(mensaje)
    engine.runAndWait()

# Informar el dia de la semana

def pedir_dia():

    # crear variable con datos de hoy

    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana

    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombre de dias

    calendario = {0:'Lunes',1:'Martes',2:'Miercoles',3:'Jueves',4:'Viernes',5:'Sabado',6:'Domingo'}

    # decir el dia de la semana

    hablar(f'Hoy es {calendario[dia_semana]}')

# Informar hora

def pedir_hora():

    # crear variable con datos de hora

    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)

    # decir la hora

    hablar(hora)

# Funcion saludo inicial

def saludo_inicial():

    # crear variable con datos de hora

    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'

    # decir saludo

    hablar(f'{momento}. Soy Elena. En que te puedo ayudar?')

# Funcion central del asistente

def pedir_cosas():

    # activar saludo inicial

    saludo_inicial()

    while True:

        # activar el microfono y guardar el pedido en un string

        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto. Estoy abriendo YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Perfecto. Ya estoy abriendo tu navegador')
            webbrowser.open('https://')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f'Esto es lo que encontre en Wikipedia: {resultado}')
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Rocanrrol bebe. Ya lo reproduzco')
            pywhatkit.playonyt(pedido)
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL','amazon':'AMZN','google':'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue
        elif 'ciérrate' or 'adiós' or 'chau' in pedido:
            hablar('Hasta luego')
            break
        
pedir_cosas()