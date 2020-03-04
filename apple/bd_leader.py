# encoding:utf-8
import requests
import webbrowser
import random
import time

from django.http import JsonResponse

ak_list = ["tqVYV4fb2DH0q9MSqUoxXpk5DWmUysmT", "PY6pILKGRoOZNxUGStlYyzMzHkVjmcoi"]
ak = random.choice(ak_list)  # 随机选一个ak
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://restapi.amap.com/'
}


# 根据地点获取经纬度
def get_JWcode(addr):
    url = 'https://api.map.baidu.com/geocoding/v3/?address=%s&output=json&ak=%s' % (addr, random.choice(ak_list))
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            loc_info = r.json()["result"]["location"]
            lng = loc_info['lng']
            lat = loc_info['lat']
            return lng, lat
        except Exception as e:
            print("get_JWcode()函数捕获到错误：", e)
            return None
    else:
        print("status_code ========>", r.status_code)
        return None


# 根据经纬度获取地址(纬度在前，经度在后)
def get_place(lat, lng):
    url = 'http://api.map.baidu.com/geocoder?location=%s,%s&coord_type=gcj02&output=json&src=一品轩物流平台' % (lat, lng)
    r = requests.get(url, headers=headers)
    address = r.json()['result']['formatted_address']
    return address


# 根据地点获取路线长度和时间
def get_route(s_addr=None, e_addr=None):
    url = 'http://api.map.baidu.com/direction?origin=%s&destination=%s&mode=driving&output=json' \
          '&src=一品轩物流平台' % (s_addr, e_addr)
    r = requests.get(url, headers=headers)
    try:
        distance = r.json()['routes'][0]['dist']
        duration = r.json()['routes'][0]['duration']
        return distance, duration
    except Exception as e:
        print("get_route()函数捕获到错误：", e)
        return None


# 打开地图导航查看路线
def open_map(s_addr=None, e_addr=None):
    url = 'http://api.map.baidu.com/direction?origin=%s&destination=%s&mode=driving&region=中国&output=html' \
          '&src=一品轩物流平台' % (s_addr, e_addr)
    webbrowser.open(url)


# 菜单选择
while True:
    # print('ak：', ak)
    print('''
        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        ------------ 1.根据地址查询经纬度 --------------
        ------------ 2.根据经纬度查询地址 --------------
        ------------ 3.根据地点查询路线长度和时间 ------
        ------------ 4.根据地点查看导航路线 ------------
        ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    ''')
    action = input('请输入操作前面的代号来选择操作：')
    if action:
        if action == '1':
            address = input('请输入要查询的地址（地点越详细经纬度越准确）：')
            if get_JWcode(address):
                lng, lat = get_JWcode(address)
                print('经度: %s\n纬度：%s' % (lng, lat))
            else:
                print('get_JWcode()函数遇见错误，未查找到地址。请重试')
        elif action == '2':
            lat = input('请输入要查询的纬度：')
            lng = input('请输入要查询的经度：')
            if get_place(lat, lng):
                address = get_place(lat, lng)
                print('经度:%s，纬度:%s。对应的地址是：%s' % (lng, lat, address))
            else:
                print('get_place()函数遇见错误，未查找到地址。请重试')
        elif action == '3':
            start_address = input('请输入导航路线的起点：')
            end_address = input('请输入导航路线的终点：')
            if get_route(start_address, end_address):
                distance, duration = get_route(start_address, end_address)
                dis = float(distance) / 1000  # 米转为千米单位
                dis = round(dis, 1)
                minutes = duration // 60  # 秒转分钟单位
                print('全程距离约：%skm，大约需要%d分钟' % (dis, minutes))
            else:
                print('get_route()函数遇见错误，未查找到地址。请重试')
        elif action == '4':
            start_address = input('请输入导航路线的起点：')
            end_address = input('请输入导航路线的终点：')
            if open_map(start_address, end_address):
                open_map(start_address, end_address)
        else:
            print('》》》》》请按照要求输入选项前面的序号。《《《《《')
    else:
        print('》》》》》您似乎没输入任何东西！《《《《《')
