import grpc

from ProtoOut.notes_pb2_grpc import NoteServiceStub
# from ProtoOut.notes_pb2 import Empty, NoteList, Note
import ProtoOut.notes_pb2

# print dir(grpc.)
channel = grpc.insecure_channel('localhost:51001')
stub = NoteServiceStub(channel)

request =  ProtoOut.notes_pb2.Empty()

# print dir(stub)

noteList = stub.List(request)

print "*"*100
print noteList
print "*"*100