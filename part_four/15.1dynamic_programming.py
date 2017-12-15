
f1 = []
f2 = []
l1 = []
l2 = []

def fastest_way(a1, a2, e, t1, t2, x, n):
    f1.append(e[0] + a1[0])
    f2.append(e[1] + a2[0])

    for j in range(1, n):
        if f1[j - 1] + a1[j] <= f2[j - 1] + t2[j-1] + a1[j]:
            f1.append(f1[j - 1] + a1[j])
            l1.append(1)
        else:
            f1.append(f2[j-1] + t2[j-1] + a1[j])
            l1.append(2)

        if f2[j-1] + a2[j] <= f1[j-1]+t1[j-1] + a2[j]:
            f2.append(f2[j - 1] + a2[j])
            l2.append(2)
        else:
            f2.append(f1[j - 1] + t1[j - 1] + a2[j])
            l2.append(1)
    if f1[n-1] + x[0] <= f2[n-1] + x[1]:
        f = f1[n-1] + x[0]
        l = 1
    else:
        f = f2[n-1] + x[1]
        l = 2

    return f,l

def print_stations(l_dict, l, n):
    i = l
    print "line", i, ", station", n
    for j in range(1, n)[::-1]:
        i = l_dict.get("l"+str(i))[j-1]
        print "line", i, ", station", j


a1 = [7, 9, 3, 4, 8, 4]
a2 = [8, 5, 6, 4, 5, 7]
e = [2, 4]
x = [3, 2]
t1 = [2, 3, 1, 3, 4]
t2 = [2, 1, 2, 2, 1]

f, l = fastest_way(a1, a2, e, t1, t2, x , 6)
print f1, f2 , f, l1, l2, l
l_dict = {'l1':l1, 'l2':l2}
print_stations(l_dict, l, 6)


