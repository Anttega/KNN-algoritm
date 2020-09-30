import pandas as pd
from collections import defaultdict
import csv

df_count_st = pd.read_csv('data/metro_count_station.csv')

df_drink = pd.read_csv('data/data.csv')


df_drink['напиток'].replace('Кофе', 1, inplace=True)# заменяем кофе на 1
df_drink['напиток'].replace('Чай', 0, inplace=True)# заменяем чай на 0


dict_drink = defaultdict(int)
for k, v in zip(df_drink['станция'], df_drink['напиток']):
    dict_drink[k] = v

KNN = 3
result_dict = defaultdict()

for station in df_count_st.columns[1:]:
    df = df_count_st.sort_values(by=[str(station)])
    r_mean = 0
    if station in dict_drink:
        if dict_drink[station] == 0:
            result_dict[station] = 'Чай'
        if dict_drink[station] == 1:
            result_dict[station] = 'Кофе'
        continue
    for i, k in zip(df[df.columns[0]], range(KNN)):
        r_mean += dict_drink[i]
    if r_mean > 0.5:
        result_dict[station] = 'Кофе'
    elif r_mean == 0.5:
        KNN += 1
    else:
        result_dict[station] = 'Чай'



with open ('data/result.csv', 'w') as file:
    for key, value in result_dict.items():
        writer = csv.writer(file)
        writer.writerow([key, value])