import sys
import time
import json
import subprocess

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, id_execution):
        execu = subprocess.check_output("st2 execution get {}".format(id_execution), shell=True)
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write("-----------\n" + execu.decode("utf-8") + "\n" + "-----------\n")
        return (True)
