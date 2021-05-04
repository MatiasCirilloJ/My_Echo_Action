import sys
import time
import os

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, rhost, host):
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write('rhost: ' + rhost + '|' + 'host: ' + host + "\n")
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write(return(True) + '\n')
        #return (True)
