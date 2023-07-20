import requests
import json

# def get_data():

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"

params = {
    "Authorization":"CWB-6991B53F-ABFF-4CFE-A16D-4E689066F1DE",
    "format":"JSON",
    "locationName": "新北市",
}
response = requests.get(url, params=params)

# print(response.text) #跟官方取得的json資料一樣
# print(response.status_code)

if response.status_code == 200:
    data = json.loads(response.text)

    location = data["records"]["location"][0]["locationName"]

    weather_elements = data["records"]["location"][0]["weatherElement"]

    start_time = weather_elements[0]["time"][0]["startTime"]

    end_time = weather_elements[0]["time"][0]["endTime"]

    weather_stat = weather_elements[0]["time"][0]["parameter"]["parameterName"] # 天氣狀況
    rain_pos = weather_elements[1]["time"][0]["parameter"]["parameterName"] # 下雨機率
    min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"] # 最低溫度
    confort = weather_elements[3]["time"][0]["parameter"]["parameterName"] # 舒適度
    max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"] # 最高溫度

    print(weather_stat,rain_pos,confort,max_tem) #testing
else:
    print("error:cannot get data")