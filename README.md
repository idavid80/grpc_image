# Conexiones gRPC

Este proyecto implementa un cliente-servidor utilizando **gRPC**, con ejemplos en Python y Node.js. Además, se incluyen métodos para el envío y recepción de imágenes y manejo de flujos bidi-direccionales (Bidirectional Streams).

## Requisitos

### Python
- **Dependencias:**

```bash
python -m pip install grpcio-tools
```

### Node.js
- **Dependencias:**

```bash
npm install google-protobuf @grpc/proto-loader
npm install grpc google-protobuf @grpc/proto-loader
npm install @grpc/grpc-js
```

### Definición del Archivo .proto
Define el archivo .proto acorde a las necesidades del proyecto.
Genera los archivos necesarios para las conexiones 

El archivo user.proto define los servicios y mensajes para las operaciones gRPC utilizadas.

#### Definición del Archivo
```proto
syntax = "proto3";

option java_multiple_files = true;
option java_package = "io.grpc.examples.helloworld";
option java_outer_classname = "HelloWorldProto";
option objc_class_prefix = "HLW";

package user;

// Servicio para manejo de usuarios
service UsuarioServicio {
  // Obtiene información de un usuario
  rpc GetUser (GetUserRequest) returns (GetUserReply) {}

  // Procesa una imagen
  rpc ProcessImage (GetUserRequest) returns (GetUserReply) {}

  // Recibe imágenes como flujo
  rpc GetStreamImage (stream GetImage) returns (GetUserReply) {}

  // Envía y recibe imágenes como flujo bidi-direccional
  rpc ImageStreamReply (stream GetImage) returns (stream GetImageReply) {}

  // Comunicación bidi-direccional para usuarios
  rpc GetUserBidiStream (stream GetUserRequest) returns (stream GetAllReply) {}
}

// Solicitud para obtener información de un usuario
message GetUserRequest {
  string name = 1;
  int32 pow = 2;
  bytes image = 3;
}

// Respuesta con información de un usuario
message GetUserReply {
  string message = 1;
}

// Solicitud y respuesta para manejo de imágenes
message GetImage {
  bytes image = 1;
}

message GetImageReply {
  string message = 1;
}

// Respuesta general para flujos bidi-direccionales
message GetAllReply {
  string name = 1;
  int32 pow = 2;
  bytes image = 3;
}
```
#### Servicios Disponibles

- **GetUser**: Envía un mensaje con el nombre y recibe una respuesta con un mensaje.
- **ProcessImage**: Procesa una imagen enviada como parte de la solicitud.
- **GetStreamImage**: Recibe un flujo de imágenes como stream.
- **ImageStreamReply**: Comunicación bidi-direccional para envío y recepción de imágenes.
- **GetUserBidiStream**: Comunicación bidi-direccional para solicitudes y respuestas relacionadas con usuarios.

#### Generación de Archivos desde el Archivo .proto

**Python**
Genera los archivos de Python:

```bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. user.proto
```
**Node.js**
Genera los archivos del cliente Node.js:
```bash
protoc -I . --js_out=import_style=commonjs:. --grpc_out=grpc_js:. user.proto
```

### Ejemplo de Cliente gRPC en Python

#### Archivo: client_user.py
Este archivo implementa un cliente gRPC que utiliza el método GetUser. Este archivo es un ejemplo muy básico de conexiones grpc.

**Uso**
Asegúrate de tener bien configurada la ruta de la imagen.
Asegúrate de que el servidor está corriendo.
Ejecuta el cliente desde la carpeta client:
```bash
python client_user.py
```

#### Archivo: usuario.py
Este archivo implementa un cliente gRPC para interactuar con un servidor definido mediante un archivo .proto. Proporciona funcionalidad para enviar y recibir datos a través de los métodos del servicio gRPC, incluyendo:

1. Envío de datos de texto (string):
Permite realizar solicitudes básicas con texto, como nombres o mensajes, utilizando el método GetUser.

2. Envío de imágenes completas:
Envía imágenes en un único mensaje, convirtiéndolas previamente a bytes, y las procesa en el servidor mediante el método ProcessImage.

3. Envío de imágenes por chunks (fragmentos):
Divide imágenes grandes en fragmentos (chunks) para transmitirlas eficientemente mediante el método GetStreamImage.

4. Gestión de múltiples métodos del servidor:
El cliente utiliza diferentes técnicas para probar y validar la interacción con todos los métodos definidos en el archivo .proto, asegurando compatibilidad y funcionalidad.

El archivo está diseñado para demostrar cómo manejar flujos de datos variados (textuales y binarios) en un cliente gRPC, incluyendo ejemplos avanzados de streaming bidireccional y procesamiento por partes. Esto lo hace ideal para casos de uso que requieren manejar grandes volúmenes de datos o imágenes en tiempo real.

**Uso**
Asegúrate de tener bien configurada la ruta de la imagen.
Asegúrate de que el servidor está corriendo.
Ejecuta el cliente desde la carpeta client:
```bash
python ./usuario.py
```
#### Archivo: usuario_prueba.py
Este archivo es muy parecido al archivo anterior, pero sin mejoras de código.

### Ejemplo de Cliente gRPC en Node.js
Archivo: client_node.js
Este archivo implementa un cliente gRPC para enviar imágenes y manejar flujos.

**Uso**
Asegúrate de tener bien configurada la ruta de la imagen.
Asegúrate de que el servidor está corriendo.
Configura la ruta de la imagen en la variable imagePath.
Ejecuta el cliente desde la carpeta client:
```bash
node client_node.js
```

### Conexión Segura al Servidor gRPC
**Python**
```python
import grpc

# Conexión segura
credentials = grpc.ssl_channel_credentials()
channel = grpc.secure_channel('localhost:50051', credentials)

# Stub del servicio
stub = pb2_grpc.UsuarioServicioStub(channel)
```
**Uso**
Asegúrate de tener bien configurada la ruta de la imagen.
Asegúrate de que el servidor está corriendo.
Ejecuta el servidor desde la carpeta server:
```bash
python ./server_user.py 
```

**Node.js**

1. Genera las clases del cliente:

```bash
protoc-gen-grpc --js_out=import_style=commonjs,binary:./cliente/ \
--grpc_out=./cliente --proto_path ./proto/ ./proto/order_data.proto
```

2. Agrega compatibilidad con gRPC-Web:

```bash
--grpc-web_out=import_style=commonjs,mode=grpcwebtext:$OUT_DIR
```
**Uso**
Para este proyecto se descartó utilizar un servidor node.

### Mejoras a Considerar
- Definir mensajes .proto para manejar errores específicos.
- Utilizar módulos como pathlib para manejar rutas de archivos dinámicamente.

## Contribuciones

Espero que esta información te sea útil para iniciar con gRPC en tu proyecto. 😊