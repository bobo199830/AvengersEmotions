from urllib import request
import json
import time
from datetime import datetime
from datetime import timedelta
import  xlwt


# def get_ip_list():
#     url = 'http://www.xicidaili.com/nn/'
#     headers = {
#        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
#     }
#     web_data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(web_data.text, 'lxml')
#     ips = soup.find_all('tr')
#     ip_list = []
#     for i in range(1, len(ips)):
#         ip_info = ips[i]
#         tds = ip_info.find_all('td')
#         ip_list.append(tds[1].text + ':' + tds[2].text)
#     return ip_list

# def get_random_ip():
#     ip_list = get_ip_list()
#     proxy_list = []
#     for ip in ip_list:
#         proxy_list.append(ip)
#     proxy_ip = random.choice(proxy_list)
#     return proxy_ip

# 获取数据，根据url获取
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    if response.getcode() == 200:
        return response.read()
    return None    


# 处理数据
def parse_data(html):
    data = json.loads(html)['cmts']  # 将str转换为json
    comments = []
    for item in data:
        comment = {
            'id': item['id'],
            'nickName': item['nickName'],
            'cityName': item['cityName'] if 'cityName' in item else '',  # 处理cityName不存在的情况
            'content': item['content'].replace('\n', ' ', 10),  # 处理评论内容换行的情况
            'score': item['score'],
            'startTime': item['startTime']
        }
        comments.append(comment)
    return comments


# 存储数据，存储到文本文件
def save_to_txt():
    datalist=[]
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间，从当前时间向前获取
    end_time = '2019-04-24 00:00:00'
    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/248172.json?_v_=yes&offset=0&startTime=' + start_time.replace(
            ' ', '%20')
        html = None
        '''
            问题：当请求过于频繁时，服务器会拒绝连接，实际上是服务器的反爬虫策略
            解决：1.在每个请求间增加延时0.1秒，尽量减少请求被拒绝
                 2.如果被拒绝，则0.5秒后重试
        '''
        try:
            html = get_data(url)
        except Exception as e:
            time.sleep(0.5)
            html = get_data(url)
        else:
            time.sleep(0.1)

        comments = parse_data(html)
        # print(comments)
        start_time = comments[14]['startTime']  # 获得末尾评论的时间
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(
            seconds=-1)  # 转换为datetime类型，减1秒，避免获取到重复数据
        start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')  # 转换为str
        
        for item in comments:
            datalist.append(str(item['id']))
            datalist.append(str(item['nickName']))
            datalist.append(str(item['cityName']))
            datalist.append(str(item['content']))
            datalist.append(str(item['score']))
            datalist.append(str(item['startTime']))
        new_list=[datalist[i:i+6]  for i in range(0,len(datalist),6)]
        i=1
        for list in new_list:
            j=0
            for data in  list:
                sheet1.write(i,j,data)
                j+=1
            i+=1
        book.save('avengers.xls')

if __name__ == '__main__':
    book=xlwt.Workbook()
    sheet1=book.add_sheet('sheet1',cell_overwrite_ok=True)
    heads=[u'id',u'NickName',u'cityName',u'content',u'score',u'startTime']
    ii=0
    for head in heads:
        sheet1.write(0,ii,head)
        ii+=1
    save_to_txt()
