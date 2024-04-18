import keyboard
from config import Config

settings = Config('./config.toml')
dz_list = settings.get('dz_list')
# 使用默认或者自定义退出按键
ESC_KEY = settings.get('ESC_KEY','ctrl+alt+q')

if dz_list is None:
    print("未找到配置文件中的dz_list(对照列表),请先配置")
    print("例如: dz_list = [['2-8','S008],]")
for dz in dz_list:
    keyboard.add_abbreviation(dz[0],dz[1])
print(f"==============开启监听,输入{ESC_KEY}退出该程序====================")
print("输入对应的数字,再输入空格,可替换")
print("例如:输入 1,再输入空格,可替换为S010")
print("例如:输入 2-8,再输入空格,可替换为S001")
print("========================================================")
keyboard.wait(ESC_KEY)

