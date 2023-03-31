import requests, json

class NavixyResponse:
    def responseFormarTramas(self):
        pass

    def generarHash(self): 
        payload = {
            'login': 'retransmison@maerskline.com',
            'password': 'maerskline'
        }
        headers = {
            "Content-Type": "application/json",
            "NVX-ISO-DateTime": "true"
        }
        response = requests.post("https://api.us.navixy.com/v2/user/auth?login", data = json.dumps(payload), headers=headers)
        data = response.json()
        return data
    
    def listarUnidades(self, datahash):
        payload = {
            "hash": datahash["hash"]
        }
        headers = {
            "Content-Type": "application/json",
            "NVX-ISO-DateTime": "true"
        }
        response = requests.post("https://api.us.navixy.com/v2/tracker/list", data = json.dumps(payload), headers=headers)
        data = response.json()
        return data