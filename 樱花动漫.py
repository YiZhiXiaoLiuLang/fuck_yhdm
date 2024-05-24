import requests
from m3u8download import download as m3u8
use_host="SD2资源"
def szy(url,mode='text'):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    res=requests.get(url,headers=headers)
    if mode=='text':
        return res.text
    if mode=='json':
        return res.json()
def download(ep,anime_id):
    global use_host
    #https://yhdmoe.com/myapp/_get_ep_plays?ep=EP7&anime_id=20245909
    #EP7:第7集
    #anime_id=20245909：动漫的id
    urll='https://yhdmoe.com/myapp/_get_ep_plays?ep=EP'+str(ep)+'&anime_id='+str(anime_id)
        
    
    json1=szy(urll,mode='json')
    #[0]:第一个播放源
    #名字：json1['result'][0]['name']+'mp4'
    #id：json1['result'][0]['id']
    for i in json1['result']:
        #名字：i['name']+'mp4'
        #id：i['id']
        #播放源：i["src_site_tag"]
        print(i['name'],i["src_site_tag"],i['id'])
        if(i["src_site_tag"]==use_host):
            urlid=int(i['id'])
    urll=szy("https://yhdmoe.com/myapp/_get_raw?id="+str(urlid))
    print(urll)
    #m3u8.M3u8Download("https://v11.fentvoss.com/sdv11/202404/07/P0rN0z3njh3/video/index.m3u8","1.mp4")
    
    m3u8d=m3u8.M3u8VideoDownloader(m3u8_url=urll,video_name=json1['result'][0]['name']+'mp4')
    print("download start")
    m3u8d.start()
for i in range(1,7):
    download(i,20245909)
