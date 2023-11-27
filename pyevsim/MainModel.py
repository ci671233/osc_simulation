from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite, SysMessage
from EmissionModel import EmissionModel

class MainModel(BehaviorModelExecutor) :
    def __init__(self, instance_time, destruct_time, name, engine_name) :
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Start", 1)
        self.insert_state("WaitForData", 1)

        self.engine = SystemSimulator.get_engine(self.get_engine_name())

        self.insert_input_port("start")
        self.insert_input_port("result")
        self.insert_output_port("model_start")

        self.emissions = [0 for i in range(5)]
        self.ended_models = 0

    def ext_trans(self, port, msg):
        if port == "start" :
            print("main model started")
            emission_factors = [[(100, 0.25, 0.05), (150, 0.35, 0.02)], # E1 모델 파라미터 설정 (논문 참조)
                                [(1000, 50, 0.207),(500, 100, 0.036)], # E2 모델 파라미터 설정 (논문 참조)
                                [(500, 600, 0.4), (550, 700, 0.5)], # E3 모델 파라미터 설정 (논문 참조)
                                [(1000, 500, 0.8), (1100, 600, 0.9)], # E4 모델 파라미터 설정 (논문 참조)
                                [(750, 0.3), (850, 0.35)]] # E5 모델 파라미터 설정 (논문 참조)

            for i in range(len(emission_factors)) :
                emissionmodel = EmissionModel(0, Infinite, f"E{i+1}", "osc_engine", emission_factors[i])
                self.engine.register_entity(emissionmodel)
                self.engine.coupling_relation(self, "model_start", emissionmodel, "start")
                self.engine.coupling_relation(emissionmodel, "result", self, "result")

            self._cur_state = "Start"

        if port == "result" :
            print("result get")
            item = msg.retrieve()
            self.emissions[item[0]] = item[1]
            self.ended_models += 1
            print(f"{self.emissions}")
            if self.ended_models >= 5 :
                print(f"Calculation Ended.")
                for i in range(len(self.emissions)) :
                    print(f"E{i+1} Model Emission : {self.emissions[i]}")
                print(f"Total Emission : {sum(self.emissions)}")
                exit()
            else :
                self._cur_state = "WaitForData"

    def output(self):
        if self.get_cur_state() == "Start" :
            msg = SysMessage(self.get_name(), "model_start")
            return msg
    
    def int_trans(self):
        if self.get_cur_state() == "Start" :
            self._cur_state = "WaitForData"
        elif self.get_cur_state() == "WaitForData" :
            self._cur_state = "WaitForData"