from src.application.response import NavixyResponse
import json

class NavixyController:
    def enviarTramas(self):
        response = NavixyResponse()
        datahash = response.generarHash() 
        dataunidades = response.listarUnidades(datahash)
        print(json.dumps(dataunidades))
        return dataunidades