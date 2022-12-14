import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from tinydb import TinyDB, Query
# Construcao do banco de dados
db = TinyDB('aluno.json')
User = Query()
# Construçao do Servidor
# Restringindo em um path particular
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
# Criando o servidor
with SimpleXMLRPCServer (('localhost',8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    # Registrando uma  instância
    class MyFuncs:
        def add(self,x,y,z):
            itens = {'nome':x,'curso':y,'periodo':z}
            return db.insert(itens)
        def show(self):
            dados = json.dumps(db.all())
            return dados
        def get(self,name):
            dados = json.dumps(db.search(User.nome == name))
            lista = json.loads(dados)
            return lista
        def delete(self, name):
            return db.remove(User.nome == name)
    server.register_instance(MyFuncs())
    server.serve_forever()