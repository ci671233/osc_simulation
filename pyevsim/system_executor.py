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
        print("Simulation started")
        while self.global_time < _time:
            self.global_time += self.time_step
            print(f"Simulation time: {self.global_time}")

            # 모든 등록된 모델에 대해 상태 업데이트
            for model in self.active_obj_map.values():
                model.time_advance()
                if model.get_req_time() == self.global_time:
                    model.int_trans()
                    model.output()
                    model.set_req_time(self.global_time)
                    
        print("Simulation ended")
        
    def insert_external_event(self, model_name, port_name, event):
        if model_name in self.active_obj_map:
            model = self.active_obj_map[model_name]
            if port_name in model.retrieve_input_ports():
                model.ext_trans(port_name, event)
            else:
                print(f"[ERROR] Port '{port_name}' not found in model '{model_name}'")
        else:
            print(f"[ERROR] Model '{model_name}' not found")