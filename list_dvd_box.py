# -*- coding: utf-8 -*-
"""
creating an list using []
  can hold up to n item 
  can cintain multiple data types
  
  
Created on Mon Mar 15 16:57:18 2021

@author: BB
"""
 


# setting the size of the array to 15 
n=15
DVD = [0 ]*n  

# define dvd
def dvd( name,  year,  director): 
        
    return "DVD"+ " " +name+ "publish in "+" "+str( year) +" "+ "by "+ " " +director           
  
# writing items in to an array 
Incredible =  dvd("The Incredibles", 2004, "Brad Bird")
Avenger =dvd("The Avengers", 2012, "Joss Whedon")   
Lion_king =dvd("The Lion King", 2019, "Jon Favreau")   
DVD[0] = Incredible 
DVD[4] = Avenger
DVD[5] = Lion_king
DVD[0]="Bob"#over written Incredible
#acesing elemetn in array 
DVD[0] 
DVD[4]

# array capacity and length 
    # capacity: number of item it can hold 
count = 0                       # length numbers of items it has
for i in DVD:
    if (i!= 0):
        count = count+1
print("DVD array has a capacity of {} and a length {}.".format(len(DVD),count) )         
# some ckoncept to loook t=for empty list, and adding or deleting form a list 


# insert, delect and search 
'''
insert
    insert a new element at the end of the array
    insert a new elemetn at the begining of the array 
    inserting a new elemetn at given index insde the array 
'''
# inserting an element at end of the array 
     # at any point we know the last elmet of current array using len()
     # we just need to assign new element at the end of the array 
DVD[len(DVD)-1] = dvd("star", 1994, "bao") 
# zero base indexing     
DVD

# defining a new function tkok keep track of invetory
def printArray(array):
    for element in range(0,len( array)):
        print("index",element, "contains", array[element] )
       # print("index",array.index(element) ,"contains",element)
                       # list.index retuens 
printArray(DVD)

# inserting at the start of the array 
    #  move every ement to tht right 
    #  time costly  operationn ,O(N) N is the length of array 
for i in range(len(DVD)):
    if i == len(DVD)-1:
	        break
    DVD[i+1] = DVD[i]
    
printArray(DVD)    


 









# delet the last elemet and inserting at a start of array 

DVD.pop(0)
    # pop first index, defaul is last 
DVD.insert(0, dvd("star ", 1994, " bao"))
    # insert first index, defaul is last 
len(DVD)
DVD

printArray(DVD)


