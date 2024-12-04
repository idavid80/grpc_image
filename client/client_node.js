var PROTO_PATH = __dirname + '/../protos/user.proto';
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
const fs = require('fs');

// Suggested options for similarity to existing grpc.load behavior
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
// The protoDescriptor object has the full package hierarchy
var usuario = protoDescriptor.user;

client = new usuario.UsuarioServicio('localhost:50051', grpc.credentials.createInsecure());

// Ruta de la imagen a enviar
const imagePath = './image/elephant.jpg'; // Cambia esto por la ruta de tu imagen

// Leer la imagen como un buffer
const imageBuffer = fs.readFileSync(imagePath);

var peticion = {name: "Pepe", pow: 3, image: generarImagen('elephant.jpg')};

var imagen = {image: generarImagen('elephant.jpg')}

function generarImagen(nombre_archivo){
  const imagePath = `./image/${nombre_archivo}`;
  const imagen = fs.readFileSync(imagePath);
  return imagen;
}
/*
client.GetUser(peticion, function(err, req) {
  if (err) {
    console.log("Error", err)
  } else {
    console.log("Node:", req)
  }
});

client.ProcessImage(imagen, function(err, req) {
    if (err) {
      console.log("Error", err)
    } else {
      console.log("imagen:", req)
    }
  });
*/
  function generarChunks(data, chunkSizes){
    const chunks = [];

    for(let i = 0; i < data.length; i+= chunkSizes){
      chunks.push(data.slice(i, i + chunkSizes))
    }
    return chunks;
  }

  function crearStreamData() {
    const entrada = Date.now()
    const chunkSizes = 4096;
    imagen = generarImagen('elephant.jpg')
    imagenChunk = generarChunks(imagen,chunkSizes)
    const call = client.GetStreamImage((error, response) => {
      if(error) {
        console.log('Error en conexion call:', error);
        return;
      }
      console.log('Respuesta servidor:', response);
    })

    imagenChunk.forEach(chunk => {
      call.write({ image: chunk });
    });
    call.end();
    const salida = Date.now()
    console.log("tiempo JS:", salida-entrada, " = ", entrada, "-", salida)
  }


  crearStreamData();
  