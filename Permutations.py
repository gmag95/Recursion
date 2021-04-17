#!/usr/bin/env python
# coding: utf-8

number=None

#data validation for the number given by the user

while isinstance(number, int)==False or number<0:
    try:
        entry=input("Insert a natural number")
        number = int(entry)
    except:
        continue

#the number given is split in a list of digits

my_list=list(entry)

#this set contains the list of all the possible numbers that result from the permutation of the inital one

output=set()

def perm(myrange, payload):

    #this is a DFS algorithm based on two lists: myrange contains the digits still to examine, payload those that were already examined

    global output
    
    if len(myrange)==1:

        #if a valid number was found changing the order of the initial number's digits, add it to the output set
        
        payload.append(myrange[0])
        if payload[0]!='0':
            output.add(''.join(payload))
        return True
    
    for x in range(len(myrange)):
        
        #a digit is removed from myrange and put in payload

        temp_pos=x
        temp_val=myrange[x]
        payload.append(myrange[x])
        myrange.pop(x)

        #the recursive function is called
        
        perm(myrange, payload)

        #backtracking part of the algorithm
        
        myrange.insert(temp_pos, temp_val)
        payload=payload[:-len(myrange)]
        
perm(my_list, [])

print(output)