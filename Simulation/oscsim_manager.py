from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from sim_cost_model import CostModel
from sim_emission_model import EmissionModel
from sim_osc_model import OscModel
import json
from config import *

class OscSim():
    def __init__(self):
        self.ss = SystemSimulator()
        self.ss.register_engine(OscSimConfig.engine_name, OscSimConfig.mode, OscSimConfig.time_step)
        self.oscsim_engine = self.ss.get_engine(OscSimConfig.engine_name)
        
        self.oscsim_engine.insert_input_port(OscSimConfig.cal_start)
        self.oscsim_engine.insert_input_port(OscSimConfig.IDLE)
        
        cost_model = CostModel(0, Infinite, CostModelConfig.model_name, \
            OscSimConfig.engine_name, self.oscsim_engine)
        emission_model = EmissionModel(0, Infinite, EmissionModelConfig.model_name, \
            OscSimConfig.engine_name, self.oscsim_engine)
        osc_model = OscModel(0, Infinite, OscModelConfig.model_name, \
            OscSimConfig.engine_name, self.oscsim_engine)        
        # Create model
        
        self.oscsim_engine.register_entity(emission_model)
        self.oscsim_engine.register_entity(cost_model)
        self.oscsim_engine.register_entity(osc_model)
        
        self.oscsim_engine.coupling_relation(None, OscSimConfig.cal_start, emission_model, OscSimConfig.cal_start)
        self.oscsim_engine.coupling_relation(emission_model, "process_out", cost_model, "process_in")
        self.oscsim_engine.coupling_relation(emission_model, "process_out", osc_model, "process_in")
        self.oscsim_engine.coupling_relation(cost_model, "process_out", emission_model, "process_in")
        self.oscsim_engine.coupling_relation(osc_model, "process_out", emission_model, "process_in")
        # self.oscsim_engine.coupling_relation(emission_model, "process_out", cost_model, "process_in")
        
        
        
    def get_engine(self):
        return self.oscsim_engine
    
    def start_engine(self) -> None:
        self.oscsim_engine.insert_external_event(OscSimConfig.cal_start, OscSimConfig.cal_start)
        self.oscsim_engine.simulate()