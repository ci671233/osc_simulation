# SimulationSetup.py
from pyevsim import SystemSimulator, Infinite
from EmissionModel import EmissionModel

def setup_simulation():
    ss = SystemSimulator()
    ss.register_engine("osc_engine", "REAL_TIME", 1)

    # E1 모델 파라미터 설정 (논문 참조)
    emission_factors_e1 = [(100, 0.25, 0.05), (150, 0.35, 0.02)]
    e1_model = EmissionModel(0, Infinite, "E1", "osc_engine", emission_factors_e1)
    ss.get_engine("osc_engine").register_entity(e1_model)

    # E2 모델 파라미터 설정 (논문 참조)
    emission_factors_e2 = [(1000, 50, 0.207),(500, 100, 0.036)]
    e2_model = EmissionModel(0, Infinite, "E2", "osc_engine", emission_factors_e2)

    ss.get_engine("osc_engine").register_entity(e2_model)

    # E3 모델 파라미터 설정 (논문 참조)
    emission_factors_e3 = [(500, 600, 0.4), (550, 700, 0.5)]
    e3_model = EmissionModel(0, Infinite, "E3", "osc_engine", emission_factors_e3)
    ss.get_engine("osc_engine").register_entity(e3_model)
    
    # E4 모델 파라미터 설정 (논문 참조)
    emission_factors_e4 = [(1000, 500, 0.8), (1100, 600, 0.9)]
    e4_model = EmissionModel(0, Infinite, "E4", "osc_engine", emission_factors_e4)
    ss.get_engine("osc_engine").register_entity(e4_model)
    
    # E5 모델 파라미터 설정 (논문 참조)
    emission_factors_e5 = [(750, 0.3), (850, 0.35)]
    e5_model = EmissionModel(0, Infinite, "E5", "osc_engine", emission_factors_e5)
    ss.get_engine("osc_engine").register_entity(e5_model)

    return ss

def run_simulation():
    ss = setup_simulation()
    ss.get_engine("osc_engine").simulate()