import subprocess
import json
import time
import re

def get_smsid_termux():
# 执行 termux-sms-list 命令并获取输出
    command = ["termux-sms-list", "-d", "-l", "10", "-n"]
    output = subprocess.check_output(command).decode("utf-8")
    # 解析输出为 JSON 格式
    sms_list = json.loads(output)
    idbox = []
    for i in sms_list:
        if i['number'] == '1068382260198656562':
            idbox.append({'id':i['_id'],'body':i['body']})
    max_item = max(idbox, key=lambda item: item['id'])
    max_body = max_item['body']
    max_id = max_item['id']
    # print(f'{max_id}  {max_body}')
    return int(max_id),max_body


def getsmscode_termux(oldsmsid):
    # 接收发送的信息
    timeout = 60  # 超时时间，单位为秒
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        if elapsed_time > timeout:
            raise TimeoutError("短信获取时长超时60s，程序中断运行")
        print(f">>> 正在获取短信验证码中...当前已等待 {elapsed_time} 秒...", end="\r")
        checksms = get_smsid_termux()
        if checksms[0] > oldsmsid:
            print(f'获取Code成功：{checksms[1]}')
            print(f">>> 获取短信验证码时长为 {elapsed_time} 秒...")
            d = re.findall('(\d+)\(体育馆\)',checksms[1])[0]
            return d

def recive_termux_smscode_main():
    old_sms_id = get_smsid_termux()[0]
    code = getsmscode_termux(old_sms_id)
    return code


