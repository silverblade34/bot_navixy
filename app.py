import time
from src.infrastructure.controller import NavixyController

def main():
    try:
        while True:
            navCL = NavixyController()
            resp = navCL.enviarTramas()
            print(resp)
            time.sleep(60)
    except Exception as err:
        print(err)

main()