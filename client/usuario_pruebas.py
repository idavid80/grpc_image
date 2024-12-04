import grpc
import logging
import user_pb2 as pb2
import user_pb2_grpc as pb2_grpc
import os
import time

def powUsuario(stub):
    
    # Datos de usuario y número
    usuario = "David"
    numero = 3
    
    imagen = generate_image_data('elephant.jpg')
    # Creación del mensaje de solicitud
    
    solicitud = pb2.GetUserRequest(name=usuario, pow=numero, image=imagen)
    # Llamada al método GetUser del servidor y recepción de la respuesta
    
    # solicitud = pb2.GetUserRequest(name=usuario, pow=numero)
    respuesta = stub.GetUser(solicitud)
    
    # Impresión de la respuesta del servidor
    print("Respuesta del servidor:", respuesta)


def generate_image_data(nombre_archivo):
    # Aquí deberías cargar tu imagen y convertirla en bytes
    path_imagen = f'./image/{nombre_archivo}'
    with open(path_imagen, 'rb') as archivo:
        imagen = archivo.read()
    return imagen


def ProcesarImagen(stub):
    
    # Datos de usuario y número
    usuario = "David"
    numero = 3
    imagen = generate_image_data('elephant.jpg')
    # Creación del mensaje de solicitud
    solicitud = pb2.GetUserRequest(name=usuario, pow=numero, image=imagen)
    # envio_imagen = pb2.GetImage(image=imagen)
    # Llamada al método GetUser del servidor y recepción de la respuesta
    respuesta = stub.ProcessImage(solicitud)
    print("Proceso Imagen:", respuesta)

    
def send_image_chunks(data):
    # chunk_size = 1024
    chunk_size = 4096
    for i in range(0, len(data), chunk_size):
        yield pb2.GetImage(image=data[i:i+chunk_size])

def ProcesarImagenStream(stub):
    entrada = int(time.time())
    # Opcion 1
    nombre_archivo = 'elephant.jpg'
    data = generate_image_data(nombre_archivo)   

    stub.GetStreamImage(send_image_chunks(data))

    salida = int(time.time())
    final = salida - entrada
    print(f'Tiempo ProcesarImagenStream: {final} = {salida} - {entrada}')
    
    # print(f'Respuesta del servidor: {response.message}')
    
        # Streaming de solicitudes al servWidor
        # stub.GetStreamImage(iter([request]))

        # print("Enviado")


def main():
    # Conexión al servidor gRPC
    entrada = int(time.time())
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.UsuarioServicioStub(channel)

    logging.basicConfig()
    powUsuario(stub)

  
    ProcesarImagen(stub)
    
    try:
        ProcesarImagenStream(stub)
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
   

    salida = int(time.time())
    final = salida - entrada
    print(f'Main: {final}  = {salida} - {entrada}')


if __name__ == '__main__':
    main()



    


