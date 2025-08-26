import datetime
import random
import unicodedata

def limpiar_texto(texto):
    # Quita tildes
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                    if unicodedata.category(c) != 'Mn')
    # Quita signos de interrogación y exclamación
    texto = texto.replace('?', '').replace('¡', '').replace('!', '')
    return texto.lower()



# Palabras prohibidas
prohibidas = ["bomba", "drogas", "hackear", "arma", "nuclear"]

# Respuestas al saludo
respuestas_hola = [
    "¡Hola! 😀 ¿En qué puedo ayudarte?",
    "¡Hey! ¿Qué más, parcero? 😎",
    "¡Buenas! ¿Listo para trabajar? 💻",
    "¡Qué tal! 🚀"
]

# Lista de chistes
chistes = [
    "¿Cuál es el café más peligroso del mundo? El ex-preso ☕😂",
    "¿Qué le dice una impresora a otra? ¿Esa hoja es tuya o es una impresión mía? 🖨️🤣",
    "¿Por qué la computadora fue al médico? ¡Porque tenía un virus! 💻🤒"
]

print("👾 Bienvenido a Minibot! (escribe 'salir' para terminar)")
while True:
    R = input("Tú: ")
    R_limpio = limpiar_texto(R)

    if R_limpio == "salir":
        print("👋 Adiós, gracias por usar Minibot!")
        break

    elif "eres una ia" in R_limpio or "que eres" in R_limpio:
        print("Sí, soy Minibot, una IA creada por MagsaOS y también para ayudarte con preguntas, cálculos y chistes etc")


    
    
    
    
    
    # Filtro de seguridad
    elif any(p in R for p in prohibidas):
        print("🚫 Esa pregunta va en contra de nuestras políticas de uso.")

    # Calculadora
    elif R.startswith("calcular"):
        operacion = R[9:]
        try:
            resultado = eval(operacion)
            print(" El resultado es:", resultado)
        except:
            print(" Hubo un error en la operación")

    # Saludos
    elif "hola" in R:
        print(random.choice(respuestas_hola))

    # Respuestas a sí/no
    elif R in ["si", "sí"]:
        print("👍 Perfecto, dime qué necesitas: calcular, chiste, hora, fecha…")
    elif R == "no":
        print("👌 Está bien, aquí estaré si me necesitas.")

            # Hora (cualquier frase con "hora")
    elif "hora" in R:
        ahora = datetime.datetime.now().strftime("%I:%M %p")  # 12h con AM/PM
        print("⏰ La hora actual es:", ahora)

    # Fecha (cualquier frase con "fecha" o "día")
    elif "fecha" in R or "dia" in R or "día" in R:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        print("📅 Hoy es:", fecha)



    # Agradecimientos
    elif "gracias" in R or "thank" in R:
        print(" De nada, para eso estoy.")

    # Chistes 
    elif "chiste" in R or "haz un chiste" in R or "cuéntame un chiste" in R or "dime un chiste" in R:
        print(random.choice(chistes))

    # Responder si es una IA
    elif "eres una ia" in R or "eres un ia" in R or "qué eres" in R:
        print("Sí, soy Minibot, una IA creada por MagsaOS y tambien para ayudarte con preguntas, calculos y chistes.")
 
    
    
    # No entendido
    else:
        print("🤔 No entendí tu mensaje, estoy aprendiendo...")
