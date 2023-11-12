import pandas as pd
import ast
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates

# CSV 파일 읽기 및 데이터 처리
df = pd.read_csv("simulation_results.csv")
df['Parameters'] = df['Parameters'].apply(ast.literal_eval)
for param in ['material_cost', 'transport_cost', 'labor_cost', 'project_duration', 'quality_index', 'carbon_emission']:
    df[param] = df['Parameters'].apply(lambda x: x.get(param))
df.drop('Parameters', axis=1, inplace=True)

# 각 날짜 및 시나리오별로 어떤 공법이 더 효율적인지 판단
def determine_efficient_method(day, scenario):
    day_scenario_group = df[(df['Day'] == day) & (df['Scenario'] == scenario)]
    max_idx = day_scenario_group['QualityScore'].idxmax()
    return day_scenario_group.loc[max_idx, 'Method']

# 'MoreEfficientMethod' 칼럼 생성
df['MoreEfficientMethod'] = df.apply(lambda row: determine_efficient_method(row['Day'], row['Scenario']), axis=1)

# 히트맵 및 그래프 생성
for scenario in df['Scenario'].unique():
    scenario_df = df[df['Scenario'] == scenario]

    # 히트맵 생성
    heatmap_data = pd.pivot_table(scenario_df, index='Day', columns='MoreEfficientMethod', aggfunc='size', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='viridis', annot=False)
    plt.title(f'More Efficient Method by Day in {scenario} (Heatmap)')
    plt.show()

    # 그래프 생성
    plt.figure(figsize=(12, 8))
    sns.countplot(data=scenario_df, x='Day', hue='MoreEfficientMethod')
    plt.title(f'More Efficient Method by Day in {scenario}')
    plt.xticks([])
    plt.show()