#definition.py
from enum import Enum

Infinite = float("inf")

class AttributeType(Enum):
    ASPECT = 1
    RUNTIME = 2
    UNKNOWN_TYPE = -1

    @staticmethod
    def resolve_type_from_str(name):
        if name.upper() == "ASPECT":
            return AttributeType.ASPECT
        elif name.upper() == "RUNTIME":
            return AttributeType.RUNTIME
        else:
            return AttributeType.UNKNOWN_TYPE

    @staticmethod
    def resolve_type_from_enum(enum):
        if enum == AttributeType.ASPECT:
            return "ASPECT"
        elif enum == AttributeType.RUNTIME:
            return "RUNTIME"
        else:
            return "UNKNOWN"

class SimulationMode(Enum):
    SIMULATION_IDLE = 0
    SIMULATION_RUNNING = 1
    SIMULATION_TERMINATED = 2
    SIMULATION_PAUSE = 3
    SIMULATION_UNKNOWN = -1

class ModelType(Enum):
    BEHAVIORAL = 0
    STRUCTURAL = 1
    UTILITY = 2

class CoreModel(object):
    def __init__(self, _name, _type):
        self._type = _type
        self._name = _name
        self._input_ports = []
        self._output_ports = []

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def insert_input_port(self, port):
        self._input_ports.append(port)

    def retrieve_input_ports(self):
        return self._input_ports

    def insert_output_port(self, port):
        self._output_ports.append(port)

    def retrieve_output_ports(self):
        return self._output_ports

    def get_type(self):
        return self._type

class SingletonType(object):
    def __call__(self, cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls.__instance