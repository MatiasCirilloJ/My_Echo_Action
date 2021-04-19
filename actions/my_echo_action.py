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
            f.write(hashlib.md5(f.read()).hexdigest())
        with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "a") as f:
            f.write(message + "\n")
        with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "rb") as f:
            f.write(hashlib.md5(f.read()).hexdigest())
        return (True, message)
