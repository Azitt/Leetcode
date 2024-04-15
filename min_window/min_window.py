def min_window(str1, str2):
    
   # Replace this placeholder return statement with your code
    s1 = list(str1)
    minwindow = ""
    minwindow_len = float("inf")
    k = 0
    index_s2 = 0
    i = 0
    while i <len(s1):
        print ("i",i)
        if s1[i] == str2[index_s2]:
            print("s1[i] ,str2[index_s2]",s1[i],str2[index_s2]) 
            index_s2 += 1              
        if index_s2==len(str2):
           index_s2 -= 1          
           print("index_s2",index_s2)
           for j  in range(i,k-1,-1):
              print("s1[j],str2[index_s2]",s1[j],str2[index_s2])
              if  s1[j] == str2[index_s2]:
                  index_s2 -=1    
              if index_s2 == -1:
                 print("j,i",j,i)
                 if len(s1[j:i+1]) < minwindow_len:
                  minwindow_len = len(s1[j:i+1])  
                  minwindow =  s1[j:i+1]
                  print("minwindow,minwindow_len",minwindow,minwindow_len)
                 k += 1
                 i = k       
                 index_s2 = 0
                 break
        i +=1               
                
    return  ''.join(minwindow) 