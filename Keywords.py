# import jieba
# ss=jieba.cut('好看，剧情也很不错，特效场景和画面都很好，是一场难忘的视觉盛宴，但可能因为是英雄集结，所以部分细节可能被删减，这也可能是漫威电影的收官之作吧，不然钢铁侠和黑寡妇怎么可能会死呢，还是感到有些悲伤的，尤其是黑寡妇死的场景和钢铁侠死的场景，总的来说，这部电影还是让人赞不绝口，大力支持，希望这部影片过后，还能看到漫威的电影吧')
# print("/".join(ss))
# import jieba.analyse
# s="好看，剧情也很不错，特效场景和画面都很好，是一场难忘的视觉盛宴，但可能因为是英雄集结，所以部分细节可能被删减，这也可能是漫威电影的收官之作吧，不然钢铁侠和黑寡妇怎么可能会死呢，还是感到有些悲伤的，尤其是黑寡妇死的场景和钢铁侠死的场景，总的来说，这部电影还是让人赞不绝口，大力支持，希望这部影片过后，还能看到漫威的电影吧"
# for x,w in jieba.analyse.extract_tags(s,withWeight=True):
#     print('%s %s'%(x,w))


import numpy as np
import xlrd
import re
import  xlwt
data = xlrd.open_workbook('avengers.xlsx')
table = data.sheets()[0]
print(table)
# nrows = table.nrows #行数# 
# ncols = table.ncols #列数
# c1=arange(0,nrows,1)
# print(c1) 


start=2  #开始的行
end=102616  #结束的行  # avengers.xls

# start=2  #开始的行
# end=42031  #结束的行  # avengers3.xls

rows=end-start  
list_values=[]
values=[]
ids=[]    
for x in range(start,end):
    row =table.row_values(x)   
    # for i in range(1,7):        
    # print(value)
    ids.append(row[0])        
    values.append(row[3])    
    # list_values.append(values)# 
# print(values)
datamatrix=np.array(list_values)
# print(datamatrix)

# contents=['钢铁侠','托尼','唐尼','三千次','斯塔克','iron','铁人','three thousand'] ironman
# contents=['美国队长','美队','翘臀','盾','九头蛇','hail hydra','举锤子'] captain
# contents=['鹰眼','浪人','hawkeye']
# contents=['寡姐','寡妇','娜塔莎',"斯嘉丽"]
# contents=['绿巨人','浩克','班纳','布鲁斯','Hulk']
# contents=['雷神','锤哥','海总','啤酒肚','发福','双锤']
# contents=['奇异博士','本尼','福尔摩斯','Strange']
# contents=['惊奇队长','惊队']
# contents=['蜘蛛','蜘蛛侠','小蜘蛛','荷兰弟']
# contents=['星云']
# contents=['黑豹','瓦坎达','wakanda']
contents=['浣熊','火箭','兔子']
contents1=['古一']
contents2=['蚁人','antman']
# plot_list = []    # 先声明一个空的列表，用来存储所有包含关键词的句子
data_list=[]
data_list1=[]
data_list2=[]
for kw in contents:
    # pattern = re.compile("'[，。][^，。]*' + kw + '[^，。]*[，。]'")
    pattern = re.compile(kw)
    for i in range(0,len(values)-1):
        # plot_temp = re.findall(pattern, values[i])# 搜索句子，把结果缓存到plot_temp
        if(re.findall(pattern, values[i])):
            data_list.append(ids[i])
            data_list.append(values[i])
            # print(ids[i]+":"+values[i])
            # print(":")
            # print(values[i])
#         plot_list = plot_list + plot_temp    # 把这次搜索结果添加都结果列表中
# print(plot_list)    # 循环搜索完毕就能输出所有结果了
for kw in contents1:
    pattern = re.compile(kw)
    for i in range(0,len(values)-1):
        if(re.findall(pattern, values[i])):
            data_list1.append(ids[i])
            data_list1.append(values[i])
for kw in contents2:
    pattern = re.compile(kw)
    for i in range(0,len(values)-1):
        if(re.findall(pattern, values[i])):
            data_list2.append(ids[i])
            data_list2.append(values[i])
new_list=[data_list[i:i+2]  for i in range(0,len(data_list),2)]
new_list1=[data_list1[i:i+2]  for i in range(0,len(data_list1),2)]
new_list2=[data_list2[i:i+2]  for i in range(0,len(data_list2),2)]
book=xlwt.Workbook()
book1=xlwt.Workbook()
book2=xlwt.Workbook()  
sheet1=book.add_sheet('sheet1',cell_overwrite_ok=True)
sheet2=book1.add_sheet('sheet1',cell_overwrite_ok=True)
sheet3=book2.add_sheet('sheet1',cell_overwrite_ok=True)
heads=[u'id',u'content']
ii=0
for head in heads:
    sheet1.write(0,ii,head)
    ii+=1
i=1
for list in new_list:
    j=0
    for data in  list:
        sheet1.write(i,j,data)
        j+=1
    i+=1
book.save('rocket.xls')
ii=0
for head in heads:
    sheet2.write(0,ii,head)
    ii+=1
i=1
for list in new_list1:
    j=0
    for data in  list:
        sheet2.write(i,j,data)
        j+=1
    i+=1
book1.save('guyi.xls')
ii=0
for head in heads:
    sheet3.write(0,ii,head)
    ii+=1
i=1
for list in new_list2:
    j=0
    for data in  list:
        sheet3.write(i,j,data)
        j+=1
    i+=1
book2.save('antman.xls')