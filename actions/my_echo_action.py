import sys
import time
import os
try:
    import hashlib
except:
    os.system("pip3 install hashlib")
    import hashlib
import filecmp

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        try:
            hash1 = hashlib.md5()
            hash1.update("/opt/stackstorm/packs/my_echo_action/actions/logs.txt")
            hash1.digest() # this generates the checksum
            with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "a") as f:
                f.write(message + "\n")
            hash2 = hashlib.md5()
            hash2.update("/opt/stackstorm/packs/my_echo_action/actions/logs.txt")
            hash2.digest() # this generates the checksum
            #time.sleep(10)
            if filecmp.cmp(hash1, hash2):
                with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "a") as f:
                    f.write("True" + "\n")
            else:
                with open("/opt/stackstorm/packs/my_echo_action/actions/logs.txt", "a") as f:
                    f.write("False" + "\n")
            return (True, message)
        except IOError:
            return (False, message)
