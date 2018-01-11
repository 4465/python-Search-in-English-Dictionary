#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'a test module'

_author_="xianfeng"

f=open("文件/《英汉汉英词典》.txt")

goal=input("请输入你要查找的单词:")
#b=raw_imput("请输入你要查找的单词:")
line_num=0
words=[]

i=0
for line in f:
    line_num+=1
    words[i]=line
    i+=1
    

def search(goal):
    for i in range(line_num):
       word=words[i].strip().split()     #type(word)->list
       if(goal==words[0]):
           print("您所要查找的单词已经找到！")
           for j in range(len(words)):
               print(words[j]+" ",end="")
               break

if __name__=='__main__':
    search(goal)




        




    