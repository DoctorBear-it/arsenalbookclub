import pandas as pd
import json

excel_data_df = pd.read_excel("../../app/src/lib/data/ratings.xlsx")
json_record = excel_data_df.to_json(orient="records")
json_record_dict = json.loads(json_record)
with open("../../app/src/lib/data/ratings.json", "w") as json_file:
    json.dump(json_record_dict, json_file)


excel_data_df_1 = pd.read_excel("../../app/src/lib/data/fixtures.xlsx")
json_record_1 = excel_data_df_1.to_json(orient="records")
json_record_dict_1 = json.loads(json_record_1)
with open("../../app/src/lib/data/fixtures.json", "w") as json_file_1:
    json.dump(json_record_dict_1, json_file_1)
