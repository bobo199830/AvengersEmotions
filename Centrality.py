import networkx as nx
import pandas as pd
import xlrd
import xlwt
data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[0]
print(table)
start=2  #开始的行
end=31479 #结束的行  # avengers.xls
rows=end-start
ids=[]
ids1=[]
values=[]
sentiment=[]
for x in range(start,end):
    row =table.row_values(x)    
    ids.append(row[0])
    ids1.append(row[1])
    values.append(row[2])
G=nx.Graph()
G.add_nodes_from(['CA','antman','ironman','heibao','nvwu','hawkeye','starword','Hulk','Marvel','rocket','Strange','Thor','Spider','xingyun','guyi','Loki','widow','groot'])
for i in range(0,len(ids)-1):
    G.add_node(ids[i])
    G.add_edge(ids[i],ids1[i],weight=values[i])
print(nx.transitivity(G))
closeness=nx.closeness_centrality(G)
betweenness=nx.betweenness_centrality(G)
keys=sorted(betweenness.items(),key=lambda item:item[0],reverse=True)
betweenness=sorted(betweenness.items(),key=lambda item:item[1],reverse=True)
closeness=sorted(closeness.items(),key=lambda item:item[1],reverse=True)
print("closeness: ", closeness)
print("betweenness: ", betweenness)