#Definir el valor actual del Euro al Dólar con respecto al peso mexicano
tipo_de_cambio_eur_a_mxn = 23.70 #en un caso mas realista habría que consumir info de la actualidad
tipo_de_cambio_usd_a_mxn = 20.75

#Solicitar al usuario el tipo de conversión (Euro a Mex o Dólar a Mex)

tipo_de_conversión = input("ingrese la moneda origen para la conversión (Eur/USD): ")

#Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("ingrese el monto a convertir: "))

#Realizar la conversión utilizando el tipo de cambio correspondiente
 # #Mostrar el resultado de la conversión al usuario
 
if tipo_de_conversión.upper() == "EUR" :
    resultado = monto_a_convertir * tipo_de_cambio_eur_a_mxn
    print("el resultado de la conversación de Eur a MXN es: " , resultado)
elif tipo_de_conversión.upper() == "USD" :
     resultado = monto_a_convertir * tipo_de_cambio_usd_a_mxn
     print("el resultado de la conversación de USD a MXN es: " , resultado)
else: 
     print("No está disponible el tipo de conversión actualmente")



# #Mostrar el resultado de la conversión al usuario