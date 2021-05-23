import requests
import random
import numpy as np
from time import sleep, time

def find_string(s, st, ed):
    if (st in s) and (ed in s):
        if st == '':
            tmp = s
        else:
            tmp = s[(s.find(st) + len(st)):]
        if ed == '':
            return tmp
        elif ed in tmp:
            s = tmp[:(tmp.find(ed))]
            return s
        else:
            return ''
    else:
        return ''


def reg_run(app_id,cookie):
    headers = {
        'authority': 'developers.facebook.com',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'viewport-width': '1030',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cookie': cookie,
    }


    url = f'https://developers.facebook.com/apps/{app_id}/roles/test-users/'
    stt1 = len(requests.get(url,headers=headers).text.rsplit('/apps/async/test-users/permissions/dialog/?app_id='))
    res = requests.get('https://mbasic.facebook.com/',headers=headers)
    fb_dtsg = find_string(str(res.text).replace("'",'"'), '<input type="hidden" name="fb_dtsg" value="', '"')
    jazoest = find_string(str(res.text).replace("'",'"'), '<input type="hidden" name="jazoest" value="', '"')
    data = {
    'jazoest':jazoest,
    'fb_dtsg': fb_dtsg,
    'count': '1',
    'platform_version': 'v10.0',
    'age': '18',
    'language': 'en-US',
    '__a': '1',
    '__csr': '',
    '__req': 'a',
    '__beoa': '0',
    'dpr': '1',
    }
    response = requests.post(f'https://developers.facebook.com/apps/async/test-users/create/?app_id={app_id}', headers=headers, data=data)
    if len(response.text) > 1000:
        stt2 = len(requests.get(url,headers=headers).text.rsplit('/apps/async/test-users/permissions/dialog/?app_id='))
        out_stt = stt2 - stt1
        uid = requests.get(url,headers=headers).text.rsplit('/apps/async/test-users/permissions/dialog/?app_id=')[out_stt].split('test_user_id=')[1].rsplit('"')[0]
        return uid,jazoest,fb_dtsg,app_id,cookie


def change_run(uid,jazoest,fb_dtsg,app_id,cookie,name,password):
    headers = {
        'authority': 'developers.facebook.com',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'viewport-width': '1030',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cookie': cookie,
            }
    data = {
    'jazoest': jazoest,
    'fb_dtsg': fb_dtsg,
    'name': name,
    'password': password,
    'confirm_password': password,
    '__a': '1',
    '__csr': '',
    '__req': 'a',
    '__beoa': '0',
    'dpr': '1'
    }

    requests.post(f'https://developers.facebook.com/apps/async/test-users/edit/?app_id={app_id}&test_user_id={uid}', headers=headers, data=data)
    return f'{name}|{uid}|{password}'




#----------------------------------------------------------------- Menu Setting ----------------------------------------------------------------
app_id = '1177159079395798'
name = 'hoang cao '
password = 'okok9999'
cookie = 'c_user=100061448881318; _fbp=fb.1.1621761874750.1826353106; spin=r.1003840870_b.trunk_t.1621764846_s.1_v.2_; datr=F0SqYLH-WVXVkZdDWjUiU08w; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1621789529777%2C%22v%22%3A1%7D; sb=xo6qYEi2Wa5Eh1Yypz_L8rSm; xs=3%3AN-v06aj2D7KiCQ%3A2%3A1618842843%3A-1%3A6264%3A%3AAcWaq67U2Zm57LMZGHMYI5B4Jn45cxhMdnQkC4srqvY; fr=13H5JpbW06PYv2vPm.AWWiIv0_AbzAzUcrPhtqEp7_-RM.BgqqYK.Zk.AAA.0.0.BgqqYK.AWVNZbt6cco; wd=1158x763; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC4yMTIgU2FmYXJpLzUzNy4zNg%3D%3D; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F90.0.4430.212%20Safari%2F537.36;  wd=1030x969'

#----------------------------------------------------------------- Run --------------------------------------------------------------------
so_luong = 10000
for i in range(so_luong):
    uid,jazoest,fb_dtsg,app_id,cookie = reg_run(app_id,cookie)
    acc = change_run(uid,jazoest,fb_dtsg,app_id,cookie,name,password)
    print(i+1,acc)
    open('done.txt','a+',encoding='utf-8').write(acc+'\n')
print('done')
