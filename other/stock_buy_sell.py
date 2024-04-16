 
p = [7,1,5,3,6,4]
profit = 0
sell,buy = 1,0
for sell in range(1,len(p)):
      
 if p[sell] > p[buy] :
   profit = max(profit,(p[sell] - p[buy])) 
 else:
     buy=sell  
print(profit)          