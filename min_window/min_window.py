def min_window(str1, str2):
 s2len = len(str2)
 index_str1 ,index_str2= 0, 0
 min_sub_len = float("inf")
 min_seq = ""
 while index_str1 < len(str1):
    if str1[index_str1] ==str2[index_str2]:
        index_str2 += 1
        if index_str2 == s2len:
           start,end = index_str1,index_str1
           index_str2 -= 1
           while index_str2 >=0:
               if str1[start] == str2[index_str2]:
                    index_str2 -=1
               start -= 1
           start += 1
           if (end - start) < min_sub_len:
               min_sub_len = end - start
               min_seq = str1[start:end+1]
           index_str1 = start
           index_str2 = 0
    index_str1 += 1 
 return min_seq 

if __name__ == '__main__':
 str1 = "abcdebdde"
 str2 = "bde"
 print(min_window(str1, str2))  