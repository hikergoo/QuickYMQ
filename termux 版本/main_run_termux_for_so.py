import sys
import os
import datetime

# 获取当前文件所在的文件夹路径
current_folder = os.path.dirname(os.path.abspath(__file__))
# 将当前文件夹路径添加到 sys.path
sys.path.append(current_folder)

from Bbadminton_intranet_20230601 import BNU_Badminton_intranet_apply

# 日期设置 默认预约3天后的
date_num = 3
date = (datetime.datetime.now() + datetime.timedelta(days=date_num)).strftime('%Y-%m-%d')
mybook = BNU_Badminton_intranet_apply('20学号','密码',['5925','5927'],date,'07:30:00','',0,0)
mybook.main_task()

# ['5925','5927'] 为场地代码，网站附录里面有