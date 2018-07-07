#!/usr/bin/env python
#coding:utf-8

from array import array #python提供的比较原始的array类

arr=array('u','asdf')
print(arr[0],arr[1],arr[2])

#实现定长的Array ADT省略了边界检查等

class Array(object):
    def __init__(self,size=32):
        self._size=size
        self._items=[None]*size
        self._index=-1

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index]=value

    def __len__(self):
        return self._size

    def clear(self,value=None):
        for i in range(len(self._items)):
            self._items[i]=value

#    def __iter__(self):
#        for item in self._items:
#            yield item
    def __iter__(self):
        return self

    def __next__(self):
        self._index+=1
        if self._index>=self._size-1:
            raise StopIteration
        else:
            return self._items[self._index]

def test_array():
    a=Array()
    for i in range(32):
        a[i]=i
    assert a[0]==0
    assert len(a)==32
    for item in a:
        print(item)

test_array()
