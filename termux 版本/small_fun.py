import time
import os

# 时间处理函数
def time_deal(timestr):
    time_str = '2022-04-01 ' + timestr
    time_sec = time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')) - 30
    timeArray = time.localtime(time_sec)
    time2 = time.strftime('%H:%M:%S', timeArray)
    return time2

##################################SMS API#######START###########################
def delete_codefile():

    file_path = r"C:\Users\Administrator\code.txt"
    if os.path.exists(file_path):
        # 删除文件
        os.remove(file_path)
        print("Code文件已删除")
    
def readcode():
    file_path = r"C:\Users\Administrator\code.txt"
    if os.path.exists(file_path):
        # 打开文件并读取第一行
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            print("Code：", first_line)
            return first_line
    else:
        return 0

def recive_api_smscode():
    timeout = 60  # 超时时间，单位为秒
    wait_time = 0.1  # 每次等待的时间，单位为秒
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        if elapsed_time > timeout:
            raise TimeoutError("短信获取时长超时60s，程序中断运行")
        print(
            f"   正在获取远程短信验证码中...当前已等待 {elapsed_time} 秒...", end="\r")
        smsCode = readcode()
        if smsCode:
            return smsCode
        else:
            time.sleep(wait_time)
##############################################################################





























