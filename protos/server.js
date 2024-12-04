const grpc = require('@grpc/grpc-js');
const services = require('./generated_code/greet_grpc_pb');
const messages = require('./generated_code/greet_pb');

function greet(call, callback) {
  const reply = new messages.GreetResponse();
  reply.setGreeting('Hello, ' + call.request.getName());
  callback(null, reply);
}

function main() {
  const server = new grpc.Server();
  server.addService(services.GreeterService, { greet: greet });
  server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
    server.start();
    console.log('Server started on port 50051');
  });
}

main();
