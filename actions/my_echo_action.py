import sys
import time
import os
try:
    import hashlib
except:
    os.system("pip3 install hashlib")
    time.sleep(15)
    import hashlib
import filecmp

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        
        with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "rb") as f:
            h1 = hashlib.md5(f.read()).hexdigest()
        with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "rb") as f:
            h2 = hashlib.md5(f.read()).hexdigest()
        with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "a") as f:
            f.write(message + "\n")
        with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "rb") as f:
            h3 = hashlib.md5(f.read()).hexdigest()
            
        if h1 == h2:
            print("h1 y h2 iguales\n")
        if h1 == h3:
            print("h1 y h3 iguales\n")
        if h2 == h3:
            print("h2 y h3 iguales\n")
            
        h4 = hashlib.md5(message).hexdigest()
        time.sleep(10)
        h5 = hashlib.md5(message).hexdigest()
        if h4 == h5:
            print("no cambia el mensaje")
        return (True, message)
