class OscSimConfig():
    mode = "REAL_TIME"
    #mode = "VIRTUAL_TIME"
    time_step = 1
    
    engine_name = 'oscsim_engine'
    emission_model_name = 'emission_model'
    
    cal_start = 'calculator_start'
    IDLE = 'IDLE'
    
    distruct_time = float("inf")
    
class CostModelConfig():
    IDLE = 'IDLE'
    distruct_time = float("inf")
    model_name = 'cost_model'
    
class OscModelConfig():
    IDLE = 'IDLE'
    PROC = 'PROC'
    distruct_time = float("inf")
    model_name = 'osc_model'    
    
class EmissionModelConfig():
    PROC = 'PROC'
    IDLE = 'IDLE'
    distruct_time = float("inf")
    model_name = 'emission_model'