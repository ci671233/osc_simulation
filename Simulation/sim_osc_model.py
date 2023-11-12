from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite, SysMessage
import json
from config import *

class OscModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, engine):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
        
        self.engine = engine
        
        self.init_state(OscModelConfig.IDLE)
        self.insert_state(OscModelConfig.IDLE, Infinite)
        self.insert_state(OscModelConfig.PROC, 1)
        
        self.insert_input_port("process_in")
        self.insert_output_port("process_out")
    
    def ext_trans(self, port, msg):
        if port == "process_in":
            data = msg.retrieve()
            print(f"[OSC MODEL : ]{data}")
            self._cur_state = OscModelConfig.PROC

    # Internal Transition
    
    def int_trans(self):
        if self._cur_state == OscModelConfig.IDLE:
            self._cur_state = OscModelConfig.IDLE
            
        elif self._cur_state == OscModelConfig.PROC:
            self._cur_state = OscModelConfig.IDLE
                

    # Output Function
    
    def output(self):
        if self._cur_state == OscModelConfig.PROC:
            message = SysMessage(self.get_name(), "process_out")
            message.insert("hello from osc!")
            return message
        
        elif self._cur_state == OscModelConfig.IDLE:
            pass

# # 비용 계산 함수
# def calculate_construction_cost(area, material_cost, labor_cost, additional_cost):
#     return area * (material_cost + labor_cost + additional_cost)

# # 프리팹 건축 및 전통 건축에 대한 비용 상수 (논문에서 제공된 값 사용)
# # 예시 값은 논문의 데이터를 기반으로 합니다.
# prefab_material_cost_per_m2 = 792.45  # Yuan/m2
# prefab_labor_cost_per_m2 = 275.29  # Yuan/m2
# prefab_additional_cost_per_m2 = 221.31  # Yuan/m2

# traditional_material_cost_per_m2 = 576.46  # Yuan/m2
# traditional_labor_cost_per_m2 = 307.79  # Yuan/m2
# traditional_additional_cost_per_m2 = 224.29  # Yuan/m2

# # 예시 사용자 입력
# construction_area = 1000  # m2

# # 비용 계산
# total_cost_prefab = calculate_construction_cost(construction_area, prefab_material_cost_per_m2, prefab_labor_cost_per_m2, prefab_additional_cost_per_m2)
# total_cost_traditional = calculate_construction_cost(construction_area, traditional_material_cost_per_m2, traditional_labor_cost_per_m2, traditional_additional_cost_per_m2)

# #
