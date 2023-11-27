# main.py
from pyevsim import Infinite, SystemSimulator
from MainModel import MainModel

if __name__ == "__main__":
    ss = SystemSimulator()
    engine = ss.register_engine("osc_engine", "REAL_TIME", 1)
    engine.insert_input_port("start")

    mainmodel = MainModel(0, Infinite, "MainModel", "osc_engine")
    engine.register_entity(mainmodel)
    engine.coupling_relation(None, "start", mainmodel, "start")

    engine.insert_external_event("start", None)

    engine.simulate()