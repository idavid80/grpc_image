from concurrent import futures
import logging

import grpc
import user_pb2 as pb2
import user_pb2_grpc as pb2_grpc
from PIL import Image
import io
import time
import os


def guardarImagen(image_bytes):

    # Guardar imagen en el servidor
    directorio_imagenes = 'imagenes_servidor'
    if not os.path.exists(directorio_imagenes):
        os.makedirs(directorio_imagenes)
        
    timestamp = int(time.time())
    image_path = os.path.join(directorio_imagenes, f'{timestamp}_image.jpg')
    with open(image_path, 'wb') as archivo:
        archivo.write(image_bytes)
        
    return os.path.exists(image_path)


class UserServicer(pb2_grpc.UsuarioServicioServicer):
    def GetUser(self, request, context):
        try:
            usuario = request.name
            print(usuario)
            numero = request.pow
            image_bytes = request.image
            
            guardardo = 'no se ha guardado'
            isSaveImage = guardarImagen(image_bytes)

            if(isSaveImage):
                guardardo = 'guardado correcto'

        # image_bytes = generate_image_data('imagen_8K.jpg')
            image = Image.open(io.BytesIO(image_bytes))
            print(image.size)
            
            
            potencia = numero ** 2  # Calcula el cuadrado del número recibido
            # Construye y devuelve la respuesta al cliente
            return pb2.GetUserReply(message=f'Hola, {usuario}. El cuadrado de {numero} es {potencia}. Dimensión de la imagen es: {image.size}. Guardado: {guardardo}')
            # return pb2.GetUserReply(message=f'Hola, {usuario}. El cuadrado de {numero} es {potencia}')
        except Exception as e:
            print(f"Error al procesar la imagen: {e}")
            context.set_details(f"Error al procesar la imagen: {e}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return pb2.GetUserReply(message="Error al procesar la imagen")

    def ProcessImage(self, request, context):
        
        image_bytes = request.image

        image = Image.open(io.BytesIO(image_bytes))
        width, height = image.size
        num_pixeles = width * height


        isSaveImage = guardarImagen(image_bytes)

        if isSaveImage:
            request = f'La imagen tiene {num_pixeles}. width = {width} * height = {height}.'

        else:
            request = 'Imagen no se ha podido guardar con éxito'

        return pb2.GetUserReply(message=request)
    

    def GetStreamImage(self, request_iterator, context):
      # Recibir la imagen en chunks
        entrada = int(time.time())
        try:        
            executable_data = b''
            i=0
            for request in request_iterator:
                i = i+1
                print(i," chunk")
                logging.info("Received request: %s", request)
            # print(req)
                executable_data += request.image

        except Exception:
            logging.error("Error occurred: %s", Exception)
        guardarImagen(executable_data)



    # Enviar una respuesta final
        salida = int(time.time())
        tiempo = salida - entrada
        respuesta = f"Imagen recibida y guardada: {tiempo}"
        return pb2.GetUserReply(message=respuesta)


    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UsuarioServicioServicer_to_server(UserServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
