import sys
import time
import json
import subprocess

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, host):
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write('host: ' + host + "\n")
        execution = subprocess.check_output("st2 execution list -n 1 -j", shell=True)
        id_ = json.loads(execution)[0]["id"]
        execu = subprocess.check_output("st2 execution get {}".format(id_), shell=True)
        with open("/opt/stackstorm/packs/example_pack/actions/logs.txt", "a") as f:
            f.write("-----------\n" + execu.decode("utf-8") + "\n" + "-----------\n")
        return (True, execution)
