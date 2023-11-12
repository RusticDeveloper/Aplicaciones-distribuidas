'''
Este codigo crea un servidor local para permitir la comunicacion
entre el clientes usando theads(hilos) y sockets.
'''

# importacion de librerias necesarias
import socket,threading
# declaracion de variables para enlazar a socket
direccion='127.0.0.1'
puerto=65530
# crea un serviddor TCP/IP para la comunicación
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# asigna una dirección IP y puerto al servidor
servidor.bind((direccion,puerto))
# Habilita al servidor para que reciba coneccion y permanece en estado de escucha
servidor.listen()
# mensaje para saber qque el servidor esta listo
print(f"Servidor listo y escuchando en: {direccion}:{puerto}")
# variables para almacenar los clientes conectados y sus nombres
clientes=[]
nombres=[]
# funcion usada para  enviar mensajes a todos los clientes conectados al servidor
def broadcast(message,_client):
    # recorre todos los clientes conectados al servidor
    for client in clientes:
        # si el cliente es distinto del que envio el mensaje envia en mensaje pasado por parametro
        if client != _client:
            client.send(message)

# funcion que maneja los mensajes enviados desde los clientes
def Handle_msg(client):
    # se ejecuta hasta que existe un error o excepcion
    while True:    
        try:
            # lee el mensaje enviado por el cliente
            mensaje=client.recv(1024)
            # ejecuta la funcion broadcast que muestra envia el mensaje a todos los clientes menos al que envio el mensaje
            broadcast(mensaje,client)
                
        except:
            # obtiene el cliente que envio el mensaje
            index = clientes.index(client)
            # obtiene el nombre del cliente que envio el mensaje
            username=nombres[index]
            # envia el mensaje que el cliente se ha desconectado a todos los demas clientes
            broadcast(f"Chat central: {username} desconectado".encode())
            # elimina el cliente de las lista de clientes y nombres
            clientes.remove(client)
            nombres.remove(username)
            # cierra la conexion con el cliente
            client.close()
            break

# funcion para manejar las conecciones de clientes y el envio de mensajes
def Receive_connections():
    # se ejecuta infinitamente
    while True:
        # espera una nueva coneccion
        client,address=servidor.accept()
        # pide un nombre de usuario al cliente
        client.send("username".encode())
        username=client.recv(1024).decode()
        # agrega el cliente y el nombre de usuario a la lista correspondiente
        clientes.append(client)
        nombres.append(username)
        # muestra los clientes que se conectaron al servidor 
        print(f"{username} se conecto - {str(address)}")
        # envia un mensaje a todos los clientes indicando los clientes que se conectan
        message=f"Chatbot: {username} se unio al chat!".encode()
        broadcast(message,client)
        # envia un mensaje informativo al cliente que se conecto
        client.send("conectado al chat central".encode())
        # crea un hilo para manejar los mensajes del cliente
        thread=threading.Thread(target=Handle_msg,args=(client,))
        thread.start()
# ejecuta la funcion que manejara las conecciones de los clientes y el envio de mensajes entre ellos
Receive_connections()

