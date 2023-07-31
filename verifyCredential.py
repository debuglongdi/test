# -*- coding: utf-8 -*-
import requests
import time
import json
path="./credential/"
star_num=5000
times=1000
def getCredential():
    url = "http://127.0.0.1:6101/step3/createCredential"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json"
    }

    data = {
        "claimData": {
            "age": 32,
            "name": "1",
            "gender": "F"
        },
        "cptId": 1001,
        "issuer": "did:weid:1010:0xc3d10a6a51bdfd9d286ecda951b1591f4df54693"
    }
    num_requests = times
    total_time = 0
    succ=0
    print("调用API: {}   共{}次".format(url, num_requests))
    num=star_num
    for _ in range(num_requests):
        start_time =int(time.time() * 1000)
        # //这样每次生成的credential都不同
        data["claimData"]["name"]=str(num)
        response = requests.post(url, headers=headers, data=json.dumps(data))
        end_time = int(time.time() * 1000)

        if response.status_code == 200:
            # print(response.text)
            filename=str(num)+".json"
            json_data = json.loads(response.text)
            json_data=json_data["result"]
            credential_json={
                "credential":json_data
            }
            write_data=json.dumps(credential_json)
            # 将formatted_json保存到文件中
            with open(path+filename, "w") as file:
                file.write(write_data)
            succ+=1
            num+=1
            elapsed_time = end_time - start_time
            total_time += elapsed_time

def verify():
    url = "http://127.0.0.1:6101/step1/verifyCredential"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json"
    }

    num_requests = times
    total_time = 0
    succ=0
    print("调用API: {}   共{}次".format(url, num_requests))
    num=star_num
    for _ in range(num_requests):
        start_time =int(time.time() * 1000)
        # //读取credential
        filename=str(num)+".json"
        with open(path+filename, 'r') as file:
            data = json.load(file)    
        num+=1
        response = requests.post(url, headers=headers, data=json.dumps(data))
        end_time = int(time.time() * 1000)

        if response.status_code == 200:
            res_json=json.loads(response.text)
            if(res_json["result"]==True):
                succ+=1
                elapsed_time = end_time - start_time
                total_time += elapsed_time

    average_time = total_time*1.0 / num_requests
    # print(average_time)
    print("成功调用：{}次" .format(succ))
    print("共耗时：{}ms"  .format(total_time))
    print("调用createWeId成功的平均时间{:.2f}ms".format(average_time))


# getCredential()
verify()


