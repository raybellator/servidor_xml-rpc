import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8000', allow_none=True)
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
with SimpleXMLRPCServer (('localhost',8080), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    class MyFuncs:
        def add(self,a,b,c):
            return s.add(a,b,c)
        def show(self):
            my_list = json.loads(s.show())
            return my_list
        def get(self,name):
            return s.get(name)
        def delete(self, name):
            return s.delete(name)
    server.register_instance(MyFuncs())
    server.serve_forever()
