import sys
import time
import os

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, host):
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write('host: ' + host + "\n")
        execution = os.system("st2 execution list -n 1 -j")
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write("-----------\n" + str(execution) + "\n" + "-----------\n")
        return (True)
