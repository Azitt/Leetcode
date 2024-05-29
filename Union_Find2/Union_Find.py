## Accounts Merge ####################
from union_findclass import *
from collections import defaultdict
def accounts_merge(accounts):
    uf = UnionFind(len(accounts))
    email_mapping = {}
    for i ,account in enumerate(accounts):
        emails = account[1:]
        for email in emails:
            if email in email_mapping:
                if account[0] != accounts[email_mapping[email]][0]:
                    return
                uf.union(email_mapping[email],i)
            email_mapping[email] = i 
    merged_account = defaultdict(list)
    for email, id in email_mapping.items():
        merged_account[uf.find(id)].append(email) 
    final_merged = []
    for parent, emails in merged_account.items():
       final_merged.append([accounts[parent][0]]+sorted(emails)) 
    return final_merged                 
        
accounts = [["Emma", "emma@mail.com", "emma_work@mail.com"], ["Bob", "bob_home@mail.com", "bob123@mail.com"], ["Emma", "emma_art@mail.com", "emma_work@mail.com"], ["Bob", "bob321@mail.com"]]
print(accounts_merge(accounts)) ##natalie

## Minimize Malware Spread ################
from collections import defaultdict
from union_findclass_malware import *
def min_malware_spread(graph, initial):
    uf = UnionFind(len(graph))
    # since the graph is nxn
    length = len(graph)
    for i in range(length):
        for j in range(length):
            if graph[i][j]:
              uf.union(i,j)
    
    infected = defaultdict(int)
    
    for x in initial:
        infected[uf.find_parent(x)] += 1
    
    maximum_size, candidate_node = 0, min(initial)
    
    for i in initial:
        infection_count = infected[uf.find_parent(i)]
        component_size = uf.rank[uf.find_parent(i)]

        if infection_count != 1:
            continue
        
        if component_size > maximum_size:
            maximum_size = component_size
            candidate_node = i
        elif component_size == maximum_size and i < candidate_node:
            candidate_node = i
    return candidate_node    
                 
        

graph = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
initial = [1, 2] 
print(min_malware_spread(graph, initial))  

## Evaluate Division #################
 