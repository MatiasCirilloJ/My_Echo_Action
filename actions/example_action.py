import sys
import time
import os

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, host):
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write('host: ' + host + "\n")
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write(return(True) + '\n')
        #return (True)
