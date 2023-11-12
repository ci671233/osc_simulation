import simpy
import random
import pandas as pd

# 프로젝트 시나리오 및 파라미터 설정
scenarios = {
    'UrbanLarge': {
        'OSC': {'material_cost': (70, 350), 'carbon_emission': (10, 80)},
        'Traditional': {'material_cost': (150, 600), 'carbon_emission': (100, 300)}
    },
    'SuburbanSmall': {
        'OSC': {'material_cost': (90, 400), 'carbon_emission': (20, 100)},
        'Traditional': {'material_cost': (170, 650), 'carbon_emission': (120, 350)}
    }
}

# 공통 파라미터
common_parameters = {
    "transport_cost": (50, 300),
    "labor_cost": (150, 400),
    "project_duration": (30, 120),
    "quality_index": (1, 10)
}

def calculate_quality_score(method, parameters):
    if method == 'OSC':
        quality_score = parameters['quality_index'] * 6  # OSC의 품질 지수에 더 큰 가중치
        carbon_penalty = parameters['carbon_emission'] / 200  # OSC의 탄소 배출에 대한 페널티 감소
    else:
        quality_score = parameters['quality_index'] * 3
        carbon_penalty = parameters['carbon_emission'] / 100

    cost_penalty = (parameters['material_cost'] + parameters['transport_cost'] + parameters['labor_cost']) / 1500  # 비용 페널티 감소
    score = max(0, quality_score - cost_penalty - carbon_penalty)
    return score




# 시뮬레이션 실행 함수
def construction_simulation(env, scenario, method, results):
    while True:
        # 시나리오 및 공법에 맞는 파라미터 선택
        scenario_params = scenarios[scenario][method]
        parameters = {param: (scenario_params if param in scenario_params else common_parameters)[param] for param in set(scenario_params) | set(common_parameters)}
        # 파라미터 값 선택
        selected_parameters = {param: random.uniform(*parameters[param]) for param in parameters}
        quality_score = calculate_quality_score(method, selected_parameters)
        results.append((env.now, scenario, method, quality_score, selected_parameters))
        yield env.timeout(1)

# 시뮬레이션 환경 설정 및 실행
env = simpy.Environment()
results = []
for scenario in scenarios:
    for method in ['OSC', 'Traditional']:
        env.process(construction_simulation(env, scenario, method, results))
env.run(until=500)

# 결과 데이터 저장
df = pd.DataFrame(results, columns=['Day', 'Scenario', 'Method', 'QualityScore', 'Parameters'])
df.to_csv("simulation_results.csv", index=False)