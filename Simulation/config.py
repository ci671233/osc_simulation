class OscSimConfig():
    mode = "REAL_TIME"
    #mode = "VIRTUAL_TIME"
    time_step = 1
    
    engine_name = 'oscsim_engine'
    emission_model_name = 'emission_model'
    
    cal_start = 'calculator_start'
    IDLE = 'IDLE'
    
    distruct_time = 'infinite'
    
class CostModelConfig():
    IDLE = 'IDLE'
    distruct_time = 'infinite'
    model_name = 'cost_model'
    
class EmissionModelConfig():
    PROC = 'PROC'
    IDLE = 'IDLE'
    distruct_time = 'infinite'
    model_name = 'emission_model'