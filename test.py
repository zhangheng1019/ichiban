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


def do_task():
    l = [
        '深圳市龙华区观湖街道松元厦社区福楼村32 - 1栋',
        '深圳市龙华区观澜镇大和村14栋',
        '深圳市龙华区富泉新村北区H8栋',
        '深圳市龙华区金侨花园6栋',
        '深圳市龙华民治东龙新村1区26栋',
        '深圳市龙华区富泉新村一区4巷',
        '深圳市龙华民丰路龙悦居2期6栋',
        '深圳市布吉桂芳园',
        '深圳市龙华区观兰镇桂花第二市场29栋',
        '深圳市龙岗区坂田街道祥龙花园7栋',
        '深圳市龙华区水斗新村九巷三栋',
        '深圳市罗湖区莲塘街道莲花社区名俊豪庭',
        '深圳市坂田街道天景山庄西区22栋',
        '深圳市龙华区龙华街道玉翠新村A区162 - 2栋',
        '深圳市龙华区龙华街道玉翠新村A区162 - 2栋',
        '深圳市龙岗区布吉桂芳园',
        '广东省深圳市龙岗区坂田街道岗头新围仔新梅8巷',
        '深圳市龙华新区三联社区弓村十五巷一栋',
        '深圳市龙岗区 金地名峰',
        '深圳市龙岗区坂田街道岗头路50号',
        '深圳市龙岗区布吉镇百合星城',
        '深圳市宝安区石岩街道办上屋新村41栋',
    ]
    res = []
    s_addr = '深圳市龙华区宇威商流E城'
    s_jwd = get_JWcode(s_addr)
    for e_addr in l:
        time.sleep(1)
        print('===================e_addr:', e_addr)
        e_jwd = get_JWcode(e_addr)
        url1 = 'http://api.map.baidu.com/direction/v2/driving?origin=%s,%s&destination=%s,%s' \
               '&ak=%s' % (s_jwd[1], s_jwd[0], e_jwd[1], e_jwd[0], "tqVYV4fb2DH0q9MSqUoxXpk5DWmUysmT")
        url2 = 'http://api.map.baidu.com/direction/v2/transit?origin=%s,%s&destination=%s,%s' \
               '&ak=%s' % (s_jwd[1], s_jwd[0], e_jwd[1], e_jwd[0], "tqVYV4fb2DH0q9MSqUoxXpk5DWmUysmT")
        r1 = requests.get(url1, headers=headers)
        r2 = requests.get(url2, headers=headers)
        print('到try了')
        print('r1.json():', r1.json())
        print('r2.json():', r2.json())
        try:
            duration1 = r1.json()['result']['routes'][0]['duration']
            duration2 = r2.json()['result']['routes'][0]['duration']
            dis = r2.json()['result']['routes'][0]['distance'] // 1000
            minutes_car = duration1 // 60  # 秒转分钟单位
            minutes_bus = duration2 // 60  # 秒转分钟单位
            res.append((minutes_bus, minutes_car, dis))
        except Exception as e:
            res.append((0, 0, 0))
        # print('打车大约需要%d分钟，公交大约需要%d分钟' % (minutes_car, minutes_bus))
        print('================l:', l)
        print('----------------res:', res)
    with open('艺隆.txt', 'w') as file_object:
        file_object.write('%s%s' % (l, res))

do_task()