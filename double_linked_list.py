#!/usr/bin/env python
#coding:utf-8

class Node(object):
    def __init__(self,value=None,prev=None,next=None):
        self.value,self.prev,self.next=value,prev,next


class CircularDoubleLinkedList(object):
    '''循环双端链表ADT
        多了个循环其实就是把root的prev指向tail节点，串起来
    '''

    def __init__(self,maxsize=None):
        self.maxsize=maxsize
        node=Node()
        node.next,node.prev=node,node
        self.root=node
        self.length=0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self,value):   #O(1)，你发现一般不用for循环的就是O(1)，有限个步骤
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is full')
        node=Node(value=value)
        tailnode=self.tailnode() or self.root

        tailnode.next=node
        node.prev=tailnode
        node.next=self.root
        self.root.prev=node
        self.length+=1

    def appendleft(self,value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is full')
        node=Node(value=value)
        if self.root.next is self.root: #Empty
            node.next=self.root
            node.prev=self.root
            self.root.next=node
            self.root.prev=node
        else:
            node.prev=self.root
            headnode=self.root.next
            node.next=headnode
            headnode.prev=node
            self.root.next=node
        self.length+=1

    def remove(self,node):  #O(1),传入node而不是value，我们就能实现O(1)删除
        '''
        remove
        :param node: #在lru_cache里实际上根据key保存了整个node
        :return:
        '''
        if node is self.root:
            return
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        self.length-=1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode=self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode=curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        '''相比单链表独有的反转遍历'''
        if self.root.prev is self.root:
            return
        curnode=self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode=curnode.prev
        yield curnode


def test_double_link_list():
    dll = CircularDoubleLinkedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    headnode = dll.headnode()
    assert headnode.value == 0
    dll.remove(headnode)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]


if __name__ == '__main__':
    test_double_link_list()

