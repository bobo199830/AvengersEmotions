# AvengersEmotions
本项目实现了爬取关于《复仇者联盟4》（下文简称复联4）的影评数据，由此构建社交网络分析其主要成员的重要程度。通过基于朴素贝叶斯模型的情感分析分析观众对于不同成员的情感态度，由此构建新的情感网络，同样应用节点中心性方法对其进行分析。
## 爬取数据
具体代码可参考maoyan.py文件，在此仅给出一种简单的实现方式。在实际实现时我们需加入代理池等防止被反爬。这里我们获取了102615条影评数据用于后续分析，数据文件详见Film Reviews of Avengers.xlsx。
<br>这里给出构建代理池的一种方法：
```Python
1.	def get_ip_list():  
2.	    url = 'http://www.xicidaili.com/nn/'  
3.	    headers = {  
4.	       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'  
5.	    }  
6.	    web_data = requests.get(url, headers=headers)  
7.	    soup = BeautifulSoup(web_data.text, 'lxml')  
8.	    ips = soup.find_all('tr')  
9.	    ip_list = []  
10.	    for i in range(1, len(ips)):  
11.	        ip_info = ips[i]  
12.	        tds = ip_info.find_all('td')  
13.	        ip_list.append(tds[1].text + ':' + tds[2].text)  
14.	    return ip_list  
15.	  
16.	def get_random_ip():  
17.	    ip_list = get_ip_list()  
18.	    proxy_list = []  
19.	    for ip in ip_list:  
20.	        proxy_list.append(ip)  
21.	    proxy_ip = random.choice(proxy_list)  
22.	    return proxy_ip  
```
## 根据关键词提取不同成员的影评信息
具体代码可参考Keywords.py，其基本原理便是应用正则表达式对其进行匹配，在此不做赘述。
## 构建朴素贝叶斯模型，应用其进行情感分析
具体代码可参考Naive Bayesian model.py，其训练结果如train_model.m所示，后续可通过Python中的joblib直接调用该模型进行预测。其中所用到的停用词列表如stopwordsHIT.txt所示。
## 构建社交网络，分析其特征
通过Python中的Networkx库我们可以非常轻松的构建复杂网络，并通过相关函数计算其度中心性、介数中心性、紧密中心性等从而分析其特征，具体代码可参考Centrality.py。
