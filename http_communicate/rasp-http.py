# getmac, requests 라이브러리는 다운로드 필요.

import getmac
import requests, json

# 도착 여부 판단, 이 부분은 하드웨어나 OCR측에서 로직 짜서 구현해줄것. (임시로 만든 변수니까 알아서 변경한 뒤, 하단에 if문만 잘 변경해줄것)
arrived = False
departed = True


# 통신 코드 (car_lincese부분만 OCR 파트가 수정할것)
STATION_NAME = "후문"
MAC_ADDRESS = "FC-AA-14-44-4F-81"#getmac.get_mac_address()
car_license = "12가4519" #해당 부분에 OCR로 추출한 번호판 정보가 들어가도록 해야함

# 서버명은 이후 추가될 예정
SERVER = "http://"
ARRIVED_URL = "/arrived/receive/station"
DEPARTED_URL = "/departed/receive/station"


headers = {"Content-Type": "application/json; charset=utf-8"}

data = {
            "stationName": STATION_NAME, 
            "macAddress" : MAC_ADDRESS,
            "license":car_license
       }
if arrived :
    res = requests.patch(SERVER + ARRIVED_URL, headers=headers, json=data)
    
elif departed :
    res = requests.patch(SERVER + DEPARTED_URL,  headers=headers, json=data)
   
print(res)