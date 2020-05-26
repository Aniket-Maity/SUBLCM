# -*- coding: utf-8 -*-
"""
Created on Tue May 26 07:24:55 2020

@author: Aniket Maity
"""



def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
def getValidSubarray(l):
    #l = [2, 7, 3, 9, 4] 
      
    num1 = l[0] 
    num2 = l[1] 
    lcm = find_lcm(num1, num2) 
    product = 1
    for i in range(len(l)):
        product = product*l[i]
    if(len(l)>2):
        for i in range(2, len(l)): 
            lcm = find_lcm(lcm, l[i]) 
          
    if(product==lcm):
        return len(l)
    else:
        return 0
    
        

def sub_lists(list1): 
  
    # store all the sublists  
    sublist = [[]] 
      
    # first loop  
    for i in range(len(list1) + 1): 
          
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
              
            # slice the subarray  
            sub = list1[i:j] 
            sublist.append(sub)
    return sublist

def main():
    T = int(input())
    finalOutput = []
    while(T>0):
        output = []
        sublist = []
        T-=1
        N = int(input())
        a=list(map(int,input().split()))
        sublist = sub_lists(a)
        for i in range(len(sublist)):
            if (len(sublist[i])>1):
                #print(sublist[i])
                output.append(getValidSubarray(sublist[i]))
        finalOutput.append(max(output))
    for i in range(len(finalOutput)):
        if(finalOutput[i]!=0):
            print(finalOutput[i])
        else:
            print(-1)
    
    
    
if __name__== '__main__':
    
    try:
        main()
    except:
        pass    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    