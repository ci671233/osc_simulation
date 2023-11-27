# EmissionModel.py
from pyevsim import BehaviorModelExecutor, SysMessage, Infinite

class EmissionModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, emission_factors):
        super(EmissionModel, self).__init__(instance_time, destruct_time, name, engine_name)
        self.emission_factors = emission_factors
        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("ACTIVE", 1)
        self.insert_input_port("start")
        self.insert_output_port("result")

        print(f"{self.get_name()} Initialized")

    def ext_trans(self, port, msg):
        print(f"External transition in {self.get_name()}")
        if port == "start":
            self._cur_state = "ACTIVE"

    def int_trans(self):
        print(f"Internal transition in {self.get_name()}")
        if self._cur_state == "ACTIVE":
            self._cur_state = "IDLE"

    def output(self):
        print(f"Calculating emissions for model {self.get_name()}")  # 진행 상황 출력
        # 온실가스 배출량 계산
        msg = SysMessage(self.get_name(), "result")
        emission_data = 0
        if self.get_name() == "E1":
            # 자재 온실가스 배출 모델(E1) 계산 로직
            msg.insert(0)    
            emission_data = sum(mj * fjb * (1 + ej) for mj, fjb, ej in self.emission_factors)
        
        elif self.get_name() == "E2":
            # 운송 온실가스 배출 모델(E2) 계산 로직
            msg.insert(1)
            emission_data = sum(mj * ljm * fkt / 1000 for mj, ljm, fkt in self.emission_factors)
            
        elif self.get_name() == "E3":
            # 폐기물 온실가스 배출 모델(E3) 계산 로직
            msg.insert(2)
            emission_data = sum(ws * llw * fkt / 1000 for ws, llw, fkt in self.emission_factors)

        elif self.get_name() == "E4":
            # 조립식 부품 온실가스 배출 모델(E4) 계산 로직
            msg.insert(3)
            emission_data = sum(p * lp * fkt / 1000 for p, lp, fkt in self.emission_factors)

        elif self.get_name() == "E5":
            # 장비 및 기술 온실가스 배출 모델(E5) 계산 로직
            msg.insert(4)
            emission_data = sum(rr * fnv / 1000 for rr, fnv in self.emission_factors)
        print(emission_data)
        msg.insert(emission_data)
        return msg