import pandas as pd
from collections import defaultdict
from statistics import mean


df_count_st = pd.read_csv('metro_count_station.csv')
# print(len(df_count_st.columns))
df_drink = pd.read_csv('data.csv')
# df_drink.columns = ['станция', 'напиток']
# print(df_drink)

df_drink['напиток'].replace('Кофе', 1, inplace=True)# заменяем кофе на 1
df_drink['напиток'].replace('Чай', 0, inplace=True)# заменяем чай на 0

# print(df_drink)
dict_drink = defaultdict(int)
for k, v in zip(df_drink['станция'], df_drink['напиток']):
    dict_drink[k] = v
print(dict_drink)

KNN = 3
for station in df_count_st.columns[1:]:
    # ds = df_count_st[station].sort_values(ascending=True)
    df = df_count_st.sort_values(by=[str(station)])
    # print('!!!!'+ station + '!!!')
    # print(df[df.columns[0]])
    res = 0
    for i, k in zip(df[df.columns[0]], range(KNN)):
        # res = 0

        # print(dict_drink[i])

        res += dict_drink[i]
        # print(res/KNN)
    if res >= 0.5:
        print(station+ '-----> Кофе')
    else:
        print(station + '-----> Чай')



