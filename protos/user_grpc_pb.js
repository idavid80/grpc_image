// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var user_pb = require('./user_pb.js');

function serialize_user_GetAllReply(arg) {
  if (!(arg instanceof user_pb.GetAllReply)) {
    throw new Error('Expected argument of type user.GetAllReply');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_user_GetAllReply(buffer_arg) {
  return user_pb.GetAllReply.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_user_GetImage(arg) {
  if (!(arg instanceof user_pb.GetImage)) {
    throw new Error('Expected argument of type user.GetImage');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_user_GetImage(buffer_arg) {
  return user_pb.GetImage.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_user_GetImageReply(arg) {
  if (!(arg instanceof user_pb.GetImageReply)) {
    throw new Error('Expected argument of type user.GetImageReply');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_user_GetImageReply(buffer_arg) {
  return user_pb.GetImageReply.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_user_GetUserReply(arg) {
  if (!(arg instanceof user_pb.GetUserReply)) {
    throw new Error('Expected argument of type user.GetUserReply');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_user_GetUserReply(buffer_arg) {
  return user_pb.GetUserReply.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_user_GetUserRequest(arg) {
  if (!(arg instanceof user_pb.GetUserRequest)) {
    throw new Error('Expected argument of type user.GetUserRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_user_GetUserRequest(buffer_arg) {
  return user_pb.GetUserRequest.deserializeBinary(new Uint8Array(buffer_arg));
}


// The greeting service definition.
var UsuarioServicioService = exports.UsuarioServicioService = {
  // Sends a greeting
getUser: {
    path: '/user.UsuarioServicio/GetUser',
    requestStream: false,
    responseStream: false,
    requestType: user_pb.GetUserRequest,
    responseType: user_pb.GetUserReply,
    requestSerialize: serialize_user_GetUserRequest,
    requestDeserialize: deserialize_user_GetUserRequest,
    responseSerialize: serialize_user_GetUserReply,
    responseDeserialize: deserialize_user_GetUserReply,
  },
  processImage: {
    path: '/user.UsuarioServicio/ProcessImage',
    requestStream: false,
    responseStream: false,
    requestType: user_pb.GetUserRequest,
    responseType: user_pb.GetUserReply,
    requestSerialize: serialize_user_GetUserRequest,
    requestDeserialize: deserialize_user_GetUserRequest,
    responseSerialize: serialize_user_GetUserReply,
    responseDeserialize: deserialize_user_GetUserReply,
  },
  getStreamImage: {
    path: '/user.UsuarioServicio/GetStreamImage',
    requestStream: true,
    responseStream: false,
    requestType: user_pb.GetImage,
    responseType: user_pb.GetUserReply,
    requestSerialize: serialize_user_GetImage,
    requestDeserialize: deserialize_user_GetImage,
    responseSerialize: serialize_user_GetUserReply,
    responseDeserialize: deserialize_user_GetUserReply,
  },
  imageStreamReply: {
    path: '/user.UsuarioServicio/ImageStreamReply',
    requestStream: true,
    responseStream: true,
    requestType: user_pb.GetImage,
    responseType: user_pb.GetImageReply,
    requestSerialize: serialize_user_GetImage,
    requestDeserialize: deserialize_user_GetImage,
    responseSerialize: serialize_user_GetImageReply,
    responseDeserialize: deserialize_user_GetImageReply,
  },
  getUserBidiStream: {
    path: '/user.UsuarioServicio/GetUserBidiStream',
    requestStream: true,
    responseStream: true,
    requestType: user_pb.GetUserRequest,
    responseType: user_pb.GetAllReply,
    requestSerialize: serialize_user_GetUserRequest,
    requestDeserialize: deserialize_user_GetUserRequest,
    responseSerialize: serialize_user_GetAllReply,
    responseDeserialize: deserialize_user_GetAllReply,
  },
};

exports.UsuarioServicioClient = grpc.makeGenericClientConstructor(UsuarioServicioService);
