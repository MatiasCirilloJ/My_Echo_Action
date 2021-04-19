import sys
import time

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        try:
            with open("/opt/stackstorm/packs/My_Echo_Action/actions/logs.txt", "a") as f:
                f.write(message + "\n")
            time.sleep(10)
            with open("/opt/stackstorm/packs/My_Echo_Action/actions/logs.txt", "a") as f:
                f.write("Listoo" + "\n")
            return (True, message)
        except IOError:
            return (False, message)
