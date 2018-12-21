def check(list, val):
    for X in list:
        if val>= X: 
            return False 
    return True 
list =[10, 20, 30, 40, 50, 60] 
val = 3
if(check(list, val)): 
    print"Yes"
else: 
    print"No"
  
val = 50 
if(check(list, val)): 
    print"Yes"
else: 
    print"No"
