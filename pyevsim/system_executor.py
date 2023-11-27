# system_executor.py
from collections import deque
from .definition import *
from .default_message_catcher import *
from .system_object import *
from .termination_manager import TerminationManager

class SysExecutor(SysObject, CoreModel):
    def __init__(self, _time_step, _sim_name='default', _sim_mode='VIRTUAL_TIME'):
        CoreModel.__init__(self, _sim_name, ModelType.UTILITY)
        self.global_time = 0
        self.time_step = _time_step
        self.waiting_obj_map = {}
        self.active_obj_map = {}
        self.port_map = {}
        self.simulation_mode = SimulationMode.SIMULATION_IDLE

    def register_entity(self, sim_obj):
        self.waiting_obj_map[sim_obj.get_create_time()].append(sim_obj)

    def simulate(self, _time=Infinite):
        # Simulation logic
        pass