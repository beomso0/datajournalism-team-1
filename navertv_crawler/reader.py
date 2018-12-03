#%%
import json
import pandas as pd

#json 그냥 읽어오기
# json_data = []
# with open(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\navertv_crawler\navertv_mudo_2017.json", encoding = 'utf-8') as file:
#     data = file.readlines()
#     for d in data:
#         json_data.append(json.loads(d))
# mudo_2017 = json_data[0]

#pandas로 읽어오기
data = pd.read_json(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\navertv_crawler\navertv_nahonja_2017.json", orient='records', encoding = 'utf-8')
data