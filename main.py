import requests
import json

val = input("ЯКА ВАЛЮТА?")
date = input("ЯКА ДАТА")
a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date={date}&json")

if a.status_code == 200:
    data = json.loads(a.text)
    print(data[0]["txt"], data[0]["rate"])