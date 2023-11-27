# termination_manager.py
import signal
import os

class TerminationManager(object):
    def __init__(self):
        self.__set_terminate_handler()

    @staticmethod
    def __set_terminate_handler():
        signal.signal(signal.SIGTERM, TerminationManager.__handler)
        signal.signal(signal.SIGINT, TerminationManager.__handler)

    @staticmethod
    def __handler(sig, frame):
        os._exit(0)