import grpc
import logging
import user_pb2 as pb2
import user_pb2_grpc as pb2_grpc
import os
import time


def generar_datos_imagen(nombre_archivo):
    """
    Carga una imagen desde el archivo y la convierte en bytes.
    """
    try:
        ruta_imagen = f'./image/{nombre_archivo}'
        with open(ruta_imagen, 'rb') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: La imagen {nombre_archivo} no existe en la ruta especificada.")
        return None

""" 
# Eliminado porque el .GetUser ha sido modificado en el archivo user.proto
def enviar_solicitud_usuario(stub, nombre_usuario, numero):
   
    # Envía una solicitud GetUser al servidor.
    

    try:
        solicitud = pb2.GetUserRequest(name=nombre_usuario, pow=numero)
        respuesta = stub.GetUser(solicitud)
        print("Respuesta del servidor:", respuesta)
    except grpc.RpcError as e:
        print(f"Error durante la solicitud GetUser: {e.details()}")
"""

def procesar_imagen(stub, nombre_usuario, numero, nombre_archivo):
    """
    Envía una imagen para ser procesada por el servidor.
    """
    try:
        datos_imagen = generar_datos_imagen(nombre_archivo)
        if datos_imagen is None:
            return
        solicitud = pb2.GetUserRequest(name=nombre_usuario, pow=numero, image=datos_imagen)
        respuesta = stub.ProcessImage(solicitud)
        print("Respuesta del servidor al procesar imagen:", respuesta)
    except grpc.RpcError as e:
        print(f"Error durante la solicitud ProcessImage: {e.details()}")


def dividir_datos_en_chunks(data, tamanio_chunk=4096):
    """
    Divide los datos en chunks para el streaming.
    """
    for i in range(0, len(data), tamanio_chunk):
        yield pb2.GetImage(image=data[i:i + tamanio_chunk])


def procesar_imagen_streaming(stub, nombre_archivo):
    """
    Envía una imagen al servidor en chunks utilizando streaming.
    """
    try:
        inicio = int(time.time())
        datos_imagen = generar_datos_imagen(nombre_archivo)
        if datos_imagen is None:
            return
        stub.GetStreamImage(dividir_datos_en_chunks(datos_imagen))
        fin = int(time.time())
        print(f"Tiempo de procesamiento por streaming: {fin - inicio} segundos")
    except grpc.RpcError as e:
        print(f"Error durante el streaming de imagen: {e.details()}")


def main():
    """
    Punto de entrada principal del cliente gRPC.
    """
    # Configurar el canal y el stub
    canal = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.UsuarioServicioStub(canal)

    logging.basicConfig()

    # Ejecutar las diferentes funcionalidades
   #  enviar_solicitud_usuario(stub, nombre_usuario="David", numero=3, nombre_archivo="elephant.jpg")
    procesar_imagen(stub, nombre_usuario="David", numero=3, nombre_archivo="elephant.jpg")
    
    try:
        procesar_imagen_streaming(stub, nombre_archivo="elephant.jpg")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == '__main__':
    main()
