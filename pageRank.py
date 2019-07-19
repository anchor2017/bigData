#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:24:39 2019

@author: anchor
"""

import networkx as nx
                                                                                                                                
filename = 'web-Google2.txt'
G=nx.DiGraph()
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head,tail)

pr=nx.pagerank(G,alpha=0.85)

for node, pageRankValue in pr.items():
    print("%d,%.4f" %(node,pageRankValue))

#图像显示
import matplotlib.pyplot as plt

layout=nx.spring_layout(G)
plt.figure(1)
nx.draw(G, pos=layout, node_size=[x * 6000 for x in pr.values()],node_color='m',with_labels=True)
plt.show()




