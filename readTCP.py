import socket

def get_messages(sock):
    # Leer primero la longitud como string ASCII terminada en \n
    longitud_str = ""
    print('Dentro de get_messages')
    while True:
        char = sock.recv(13).decode()
        print('CHAR: ', char)
        if char == '\n':
            print('Breaking')
            break
        longitud_str += '\n' + char
        print('longitud: ', longitud_str)

    longitud = int(longitud_str)

    # Ahora leer el número de bytes que indica longitud
    datos = b''
    while len(datos) < longitud:
        chunk = sock.recv(longitud - len(datos))
        print('Chunk::',chunk)
        if not chunk:
            raise ConnectionError("Closed Coonnection by Labview Server")
        datos += chunk

    return datos.decode()

def main():
    HOST = '127.0.0.1'  # Cambia a la IP del servidor LabVIEW
    PORT = 6341         # Cambia al puerto que está usando LabVIEW

    with socket.create_connection((HOST, PORT)) as sock:
        print("Connecting to LabVIEW Server")
        
        while True:
            try:
                mensaje = get_messages(sock)
                print("Data in:", mensaje)
            except ConnectionError as e:
                print("Closed Connection:", e)
                break

if __name__ == "__main__":
    main()

