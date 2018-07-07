#!/usr/bin/env python
#coding:utf-8

class Bag(object):
    def __init__(self,maxsize=10):
        self.maxsize=maxsize
        self._items=list()
        self.index=-1

    def add(self,item):
        if len(self._items)>self.maxsize:
            raise Exception("Full")
        self._items.append(item)

    def remove(self,item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self._items)-1:
            raise StopIteration
        else:
            self.index+=1
            return self._items[self.index]

#    def next(self):
#        self.index+=1
#        if self._items==[]:
#            raise StopIteration()
#        return self._items[self.index]

#    def __iter__(self):
#        for item in self._items:
#            yield item

def test_bag():
    bag=Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag)==3

    bag.remove(3)
    assert len(bag)==2


    for i in bag:
        print(i)

if __name__=='__main__':
    test_bag()
