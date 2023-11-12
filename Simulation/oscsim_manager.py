from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from .cost_model import CostModel
from emission_model import *
import json
from config import *

class OscSim():
    def __init__(self):
        self.ss = SystemSimulator()
        self.ss.register_engine(OscSimConfig.engine_name, OscSimConfig.mode, OscSimConfig.time_step)
        self.oscsim_engine = self.ss.get_engine(OscSimConfig.engine_name)
        
        self.oscsim_engine.insert_input_port(OscSimConfig.cal_start)
        self.oscsim_engine.insert_input_port(OscSimConfig.IDLE)
        
        cost_model = CostModel(0, Infinite, CostModelConfig.model_name, OscSimConfig.engine_name, self.oscsim_engine)
        emission_model = EmissionModel(0, Infinite, EmissionModelConfig.model_name, OscSimConfig.engine_name, self.oscsim_engine)
        # Create model
        
        
        self.oscsim_engine.coupling_relation(emission_model, "process_out", cost_model, "process_in")
        # self.oscsim_engine.coupling_relation(emission_model, "process_out", cost_model, "process_in")
        
        
        
    def get_engine(self):
        return self.oscsim_engine
    
    def start_engine(self) -> None:
        self.oscsim_engine.insert_external_event(OscSimConfig.cal_start, OscSimConfig.cal_start)
        self.oscsim_engine.simulate()