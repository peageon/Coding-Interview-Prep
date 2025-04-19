def solution(players, m, k):
    ttlcnt = 0
    servers = [0] * 24
    
    for i in range(len(players)): 
        reqServ = players[i] // m
        if servers[i] < reqServ:
            add = reqServ - servers[i]
            ttlcnt += add
            j = i
            while (j < 24 and j < i + k):
                servers[j] += add
                j += 1
    return ttlcnt
                