import threading

import sys
sys.path.append('../')
from myobject import MyObject


class Controller:

    def __init__(self, name="controller"):
        threading.Thread.__init__(self, name=name)
        self.dashboard = None
        self.dispatcher = None
        return

    def start(self):
        '''starts controller'''
        self.log().info('starting controller')
        threading.Thread.start(self)
        return

    def stop(self):
        '''stopping controller'''
        self.log().info('stopping controller')
        return

    def run(self):
        """Controller thread target."""
        self.log().info('running controller')
        self.log().info('controller finished')
        return

    def loop(self):
        """Controller action loop."""
        self.log().info('controller loop')
        return

    def logon(self, name):
        """Handles device logon."""
        self.log().info("'%s' logged on", name)
        return

    def logoff(self, name):
        """Handles device logoff."""
        self.log().info("'%s' logged off", name)
        return

    def send_params(self, name, params):
        """Sends parameters."""
        if not self.dispatcher is None:
            self.dispatcher.send_params(name, params)

        return

    def get_values(self):
        """Retrieves controller's data."""
        return {}

    def set_constraints(self, throughput, makespan):
        """Sets throughput and makespan constraints."""
        return