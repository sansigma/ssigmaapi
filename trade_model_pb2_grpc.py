# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import trade_model_pb2 as trade__model__pb2


class OrderBookStreamApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOrderBook = channel.unary_stream(
        '/sansigmaprotos.OrderBookStreamApi/GetOrderBook',
        request_serializer=trade__model__pb2.AssetPair.SerializeToString,
        response_deserializer=trade__model__pb2.OrderBook.FromString,
        )


class OrderBookStreamApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOrderBook(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OrderBookStreamApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOrderBook': grpc.unary_stream_rpc_method_handler(
          servicer.GetOrderBook,
          request_deserializer=trade__model__pb2.AssetPair.FromString,
          response_serializer=trade__model__pb2.OrderBook.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sansigmaprotos.OrderBookStreamApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class OrderBooksApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOrderBooks = channel.unary_stream(
        '/sansigmaprotos.OrderBooksApi/GetOrderBooks',
        request_serializer=trade__model__pb2.OrderBooksRequest.SerializeToString,
        response_deserializer=trade__model__pb2.OrderBooks.FromString,
        )


class OrderBooksApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOrderBooks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OrderBooksApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOrderBooks': grpc.unary_stream_rpc_method_handler(
          servicer.GetOrderBooks,
          request_deserializer=trade__model__pb2.OrderBooksRequest.FromString,
          response_serializer=trade__model__pb2.OrderBooks.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sansigmaprotos.OrderBooksApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))