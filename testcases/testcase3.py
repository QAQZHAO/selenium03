# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from lib.ShowapiRequest import ShowapiRequest

# https://www.showapi.com/apiGateway/view/?apiCode=184&pointCode=4
# r = ShowapiRequest("http://route.showapi.com/184-4","用户名","密码" )
# r.addFilePara("image", "test.png")
# r.addBodyPara("typeId", "34")
# r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
# res = r.post()
# result = res.test
# print(result)
# body = res.json()['showapi_res_body']
# print(body['Result'])
# print(res.text) # 返回信息


#http://www.ttshitu.com/user/index.html
import base64
import json
import requests

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

if __name__ == "__main__":
    img_path = r"D:\06_study\PycharmProjects\my_Selenium_project\test.png"
    result = base64_api(uname='QAQXIAOBU', pwd='Zhao16388', img=img_path, typeid=3)
    print(result)