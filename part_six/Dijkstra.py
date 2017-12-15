"""
@jetou
@date : 2017/12/14
@algorithms: Dijkstra
"""
def Dijkstra(G, w, s=999):
    book = set()
    minv = w

    dis = dict((k, s) for k in G.keys())
    dis[w] = 0

    while len(book) < len(G):
        book.add(minv)
        for i in G[minv]:
            if dis[minv] + G[minv][i] < dis[i]:
                dis[i] = dis[minv] + G[minv][i]


        new = s

        for j in dis.keys():
            if j in book: continue
            if dis[j] < new:
                new = dis[j]
                minv = j
    return dis

G = {1:{1:0,    2:1,    3:12},
     2:{2:0,    3:9,    4:3},
     3:{3:0,    5:5},
     4:{3:4,    4:0,    5:13,   6:15},
     5:{5:0,    6:4},
     6:{6:0}}

dis = Dijkstra(G,1)
print dis

