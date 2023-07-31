import requests
import time

url = "http://127.0.0.1:6101/step1/userAgent/createWeId"
num_requests = 1000  # 发送100次请求
total_time = 0
succ=0
print("调用API: {}   共{}次".format(url, num_requests))
for _ in range(num_requests):
    start_time =int(time.time() * 1000)
    response = requests.post(url, headers={"accept": "*/*"})
    end_time = int(time.time() * 1000)

    if response.status_code == 200:
        succ+=1
        elapsed_time = end_time - start_time
        total_time += elapsed_time

average_time = total_time*1.0 / num_requests
print("成功调用：{}次" .format(succ))
print("共耗时：{}ms"  .format(total_time))
print("调用createWeId成功的平均时间{:.2f}ms".format(average_time))