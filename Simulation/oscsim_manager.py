from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from cost_model import CostModel
from emission_model import EmissionModel
import json
from config import *

class OscSim():
    def __init__(self):
        self.ss = SystemSimulator()
        self.ss.register_engine(OscSimConfig.engine_name, OscSimConfig.mode, OscSimConfig.time_step)
        self.oscsim_engine = self.ss.get_engine(OscSimConfig.engine_name)
        
        self.oscsim_engine.inset_input_port(OscSimConfig.cal_start)
        self.oscsim_engine.inset_input_port(OscSimConfig.IDLE)
        
        cost_model = CostModel(0, CostModelConfig.distruct_time, CostModelConfig.model_name, OscSimConfig.engine_name, self.oscsim_engine)
        emission_model = EmissionModel(0, EmissionModelConfig.distruct_time, EmissionModelConfig.model_name, OscSimConfig.engine_name, self.oscsim_engine)
        
    def get_engine(self):
        return self.oscsim_engine
    
    def start_engine(self) -> None:
        self.oscsim_engine.insert_external_event(OscSimConfig.cal_start, OscSimConfig.cal_start)
        self.oscsim_engine.simulate()