
def intervals_intersection(list_a, list_b):
 out = []
 i,j = 0,0
 while i < len(list_a) and j < len(list_b):
    start = max(list_a[i][0],list_b[j][0])
    end = min(list_a[i][1],list_b[j][1])
    if start <= end:
        out.append([start,end])
    if end == list_a[i][1] and end== list_b[j][1]:
        i += 1
        j += 1 
    elif end == list_a[i][1]:
        i += 1
    else:
        j += 1           
 return out

if __name__ == '__main__':
    list_a = [[1,4],[5,6],[7,9]]
    list_b  = [[3,5],[6,7],[8,9]]
    print(intervals_intersection(list_a, list_b))      
        