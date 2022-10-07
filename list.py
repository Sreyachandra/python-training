list=['a','b','c','d']                                                   
print(list[0])                                                                                  #a
print(list[1])                                                                                  #b                                                      
    • print(list[2])                                                                            #c
print(list[3])                                                                                  #d
print(len(list))                                                                                #4
a=[1,"sreya",3.14,["mark",4,6,[200,201]],20]
print(a[3][0])                                                                                  #mark
#for in list
list=[1,2,3,4]
sum=0
for num in list:
  sum+=num
print(sum)                                                                                       #10
#IIN in list
list=['apple','banana']
if 'apple' in list:
 print('yes')                                                                                    #yes
#range in python
list=['apple','banana','orange']
for i in range(len(list)):
 print(list[i])                                                                                  #apple
                                                                                                 #banana
                                                                                                 #orange
#while in list
list=['apple','banana','orange']
i=0
while i<len(list):
 print(list[i])
 i=i+1                                                                                          #apple
                                                                                                #banana
                                                                                                #orange
#list methods
list=['apple','banana','orange']
list.insert(2,'cherry')
print(list)                                                                                     #[‘apple’,’banana’,’cherry’,’orange’]
list=['apple','banana','orange']
list.append('jack fruit')                                         
print(list)                                                                                     #[‘apple’,’banana’,’orange’,’jack fruit’]
list=['apple','banana','orange']
list.reverse()
print(list)                                                                                     #[‘orange’,’banana’,’apple’]
list=[4,7,1,3]
list.sort()
print(list)                                                                                     #[1,3,4,7]
list=[4,7,1,3]
print(list.pop(0))                                                                              #4
#slicing in list
names=['akshaya','mark','noel','arya']
b=names[0:2]
print(b)                                                                                       #[‘akshaya’,’mark’]
c=names[2: ]                                                                                   #[‘noel’,’arya’]
names[1]=’anu’                                                                                 #replace the second item in names with ‘anu’

