#!/usr/bin/env python
#coding:utf-8

class Node(object):
    #这里我们root节点默认都是None，所以都给了默认值
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

    def __str__(self):
        '''方便你打出来调试，复杂的代码可能需要断点调试'''
        return '<Node:value:{},next={}>'.format(self.value,self.next)

    __repr__=__str__

class LinkedList(object):
    '''链接表ADT
    [root]-->[node0]--->[node1]--->[node2]
    '''
    def __init__(self,maxsize=None):
        '''
        :param maxsize: int or None,如果是None，无限扩充
        '''
        self.maxsize=maxsize
        self.root=Node() #默认root节点指向Node
        self.tailnode=None
        self.length=0

    def __len__(self):
        return self.length

    def append(self,value): #O(1)
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')
        node=Node(value)  #构造节点
        tailnode=self.tailnode
        if tailnode is None: #还没有append过，length=0,追加到root后
            self.root.next=node
        else:   #否则追加到最后一个节点的后边，并更新最后一个节点是append的节点
            tailnode.next=node
        self.tailnode=node
        self.length+=1

    def appendleft(self,value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')
        headnode=self.root.next
        node=Node(value)
        self.root.next=node
        node.next=headnode
        self.length+=1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        '''遍历从head节点到tail节点'''
        curnode=self.root.next
        while curnode is not self.tailnode: #从第一个节点开始遍历
            yield curnode
            curnode=curnode.next  #移动到下一个节点
        yield curnode

    def remove(self,value): #O(n)
        '''删除包含值的一个节点，将其前一个节点的next指向被查询节点的下一个即可'''

        prevnode=self.root
        for curnode in self.iter_node():
            if curnode.value==value:
                prevnode.next=curnode.next
                if curnode is self.tailnode: #NOTE：注意更新tailnode
                    self.tailnode=prevnode
                del curnode
                self.length-=1
                return 1 #表明删除成功
            else:
                prevnode=curnode
        return -1 #表明删除失败

    def find(self,value):  #O(n)
        '''查找一个节点，返回序号，从0开始'''
        index=0
        for node in self.iter_node(): #我们定义了__iter__,这里就可以用for遍历它了
            if node.value==value:
                return index
            index+=1
        return -1 #没找到

    def popleft(self): #O(1)
        '''删除第一个链表节点'''
        if self.root.next is None:
            raise Exception('Pop from empty LinkedList')
        headnode=self.root.next
        self.root.next=headnode.next
        self.length-=1
        value=headnode.value

        if self.tailnode is headnode:
            self.tailnode=None

        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next=None
        self.length=0

def test_linked_list():
    ll=LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


if __name__ == '__main__':
    test_linked_list()
    test_linked_list_remove()


