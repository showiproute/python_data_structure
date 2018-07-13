#!/usr/bin/env python
#coding:utf-8

import random

test_seq=list(range(10))
random.shuffle(test_seq)

def bubble_sort(seq):
    n=len(seq)
    for i in range(n):
        print(seq)
        for j in range(n-1-i):
            if seq[j]>seq[j+1]:
                seq[j+1],seq[j]=seq[j],seq[j+1]
    print(seq)

#bubble_sort(test_seq)


def select_sort(seq):
    for i in range(len(seq)):
        index=i
        print(seq)
        for j in range(i+1,len(seq)):
            if seq[index]>seq[j]:
                index=j
        seq[i],seq[index]=seq[index],seq[i]
    print(seq)

#select_sort(test_seq)

def insertion_sort(seq):
    n=len(seq)
    print(seq)
    for i in range(1,n):
        index=i
        value=seq[index]
        while index>0 and value<seq[index-1]:
            seq[index]=seq[index-1]
            index-=1
        seq[index]=value
        print(seq)

insertion_sort(test_seq)






