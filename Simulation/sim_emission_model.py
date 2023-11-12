from pyevsim import BehaviorModelExecutor, Infinite, SysMessage
from config import *
import time

class EmissionModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, engine):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
        
        self.engine = engine
        
        self.init_state(EmissionModelConfig.IDLE)
        self.insert_state(EmissionModelConfig.IDLE, Infinite)
        self.insert_state(EmissionModelConfig.PROC, 1)
        
        self.insert_input_port("calculator_start")
        self.insert_input_port("process_in")
        self.insert_output_port("process_out")
    
    def ext_trans(self, port, msg):
        if port == "calculator_start":
            self._cur_state = EmissionModelConfig.PROC
        
        elif port == "process_in":
            data = msg.retrieve()
            print(f"[EMISSION MODEL] : {data}")
            self._cur_state = EmissionModelConfig.PROC
        

    # Internal Transition
    
    def int_trans(self):
        if self._cur_state == EmissionModelConfig.IDLE:
            self._cur_state = EmissionModelConfig.IDLE
            
        elif self._cur_state == EmissionModelConfig.PROC:
            self._cur_state = EmissionModelConfig.PROC
            

    # Output Function
    
    def output(self):
        if self._cur_state == EmissionModelConfig.PROC:
            print("[EMISSION MODEL][IN] : Processing!")
            
            
            message = SysMessage(self.get_name(), "process_out")
            message.insert("From Emission = Hello")
            
            return message
        
        elif self._cur_state == EmissionModelConfig.IDLE:
            pass
    
    
# # GHG 배출 계수 및 기타 상수 (논문에서 제공된 값 사용)
# ghg_electricity_factor = {'North': 0.9803, 'East': 0.8367, 'South': 0.9489, 'Middle': 1.0297, 'Northeast': 1.0852, 'Northwest': 1.0001}
# transportation_ghg_factor = {'Truck': 0.207, 'Train': 0.036, 'Ship': 0.035}  # kg CO2-e/ton km

# # 배출량 계산 함수 (E1부터 E5까지)
# def calculate_E1(materials):
#     # materials: {'material_name': {'quantity': float, 'emission_factor': float, 'waste_factor': float}}
#     total_E1 = sum([m['quantity'] * m['emission_factor'] * (1 + m['waste_factor']) for m in materials.values()])
#     return total_E1

# def calculate_E2(materials, distance, transportation_method):
#     # distance: float, transportation_method: string
#     total_E2 = sum([m['quantity'] * distance * transportation_ghg_factor[transportation_method] / 1000 for m in materials.values()])
#     return total_E2

# def calculate_E3(waste, distance):
#     # waste: float (total amount of waste in tons), distance: float (km)
#     return waste * distance * transportation_ghg_factor['Truck'] / 1000

# def calculate_E4(prefab_components, distance):
#     # prefab_components: float (total amount in tons), distance: float (km)
#     return prefab_components * distance * transportation_ghg_factor['Truck'] / 1000

# def calculate_E5(resource_usage):
#     # resource_usage: {'type': {'amount': float, 'emission_factor': float}}
#     total_E5 = sum([r['amount'] * r['emission_factor'] / 1000 for r in resource_usage.values()])
#     return total_E5

# # 예시 사용자 입력
# materials = {
#     'Concrete': {'quantity': 1000, 'emission_factor': 0.120, 'waste_factor': 0.025},
#     # 추가 재료 및 해당 데이터 입력
# }
# resource_usage = {
#     'Diesel': {'amount': 5000, 'emission_factor': 2.617},
#     'Electricity': {'amount': 10000, 'emission_factor': 0.9489},
#     # 추가 자원 및 해당 데이터 입력
# }

# # GHG 배출량 계산
# E1 = calculate_E1(materials)
# E2 = calculate_E2(materials, 50, 'Truck')  # 예시: 50km 거리, 트럭 운송
# E3 = calculate_E3(200, 20)  # 예시: 폐기물 200톤, 20km 거리
# E4 = calculate_E4(300, 70)  # 예시: 프리팹 구성요소 300톤, 70km 거리
# E5 = calculate_E5(resource_usage)

# # 총 GHG 배출량 출력
# total_ghg = E1 + E2 + E3 + E4 + E5
# print(f"총 GHG 배출량: {total_ghg} 톤 CO2-e")