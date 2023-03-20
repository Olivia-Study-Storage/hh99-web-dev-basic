import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']
for element in rows:
    gu_name = element['MSRSTE_NM']
    gu_mise = element['IDEX_MVL']
    print(gu_name, gu_mise)