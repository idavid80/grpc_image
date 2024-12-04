# Conexiones GRPC

protoc -I=. proto/user.proto --js_out=import_style=commonjs:. --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.

protoc --plugin=protoc-gen-grpc-web=C:/ruta/a/tu/ejecutable/protoc-gen-grpc-web.exe -I=. src/proto/user.proto --js_out=import_style=commonjs:. --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.


## Dependencias

> python -m pip install grpcio-tools

> npm install google-protobuf @grpc/proto-loader 

## Crear archivos con las clases y métodos generados desde el archivo .proto

Definimos el archivo .proto a corde con nuestras necesidades. Una vez finalizamos generamos 3 archivos que son los que nos van a permitir establecer las conexiones y ejecutar las funciones desde el cliente o el servidor. Para ello ejecutamos el siguiente script

> python -m grpc_tools.protoc -I protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/user.proto


details = "Received message larger than max (948300311 vs. 4194304)"

## NODEJS

> npm install -g protoc-gen-grpc
> npm install grpc google-protobuf @grpc/proto-loader
> npm install @grpc/grpc-js   

> protoc-gen-grpc --js_out=import_style=commonjs,binary:./cliente/ --grpc_out=./cliente --proto_path ./proto/ ./proto/order_data.proto
> 
--grpc-web_out=import_style=commonjs,mode=grpcwebtext:$OUT_DIR
# Conexiones seguras
    # Conexión segura al servidor gRPC
    credentials = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel('localhost:50051', credentials)
    stub = pb2_grpc.UsuarioServicioStub(channel)

## Notas
responses = stub.GetStreamImage(iter([request]))

iter([request]): Esto crea un iterador que genera un único elemento, que es nuestro objeto GetImage. En gRPC, los métodos que aceptan streams esperan iteradores, por lo que necesitamos envolver nuestro objeto GetImage en un iterador.


## Importar imagen desde el archivo
from imagen_pb2 import Imagen

# Canal gRPC
channel = grpc.insecure_channel('localhost:50051')

# Stub del servicio
stub = Imagen.ImagenStub(channel)

# Imagen a enviar
imagen = Imagen()
imagen.nombre = 'imagen.jpg'

# usar pathlib

> ruta_archivo = Path(__file__).parent / 'archivo.jpg'


## Mejorar definción archivo .proto
syntax = "proto3";

package imagen;

message Imagen {
  bytes data = 1;
  string nombre = 2;
}


### Imagen a enviar
imagen = Imagen()
imagen.nombre = 'imagen.jpg'

### Envío de la imagen por streaming
with open('imagen.jpg', 'rb') as f:
  for chunk in f.read(4096):
    imagen.data = chunk
    stub.EnviarImagenStreaming(imagen)


