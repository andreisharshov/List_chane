#!/usr/bin/env python
# coding: utf-8


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.prev = None
        self.tail = None
    
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value, end = ' ')
            node = node.next
        print()
    
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
    
    def add_in_head(self, item): 
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            node = self.head
            self.head = item
            item.next = node
            node.prev = item
    
    def remove_one(self, val): #удаление одного узла по значению
        node = self.head     
        
        if self.head.value == val:
            self.head = node.next
        else:
            while node is not None:
                if node.value == val:
                    p = node.prev
                    p.next = node.next
                    n = node.next
                    n.prev = p
                    break                                     
                node = node.next
    
    
    def find(self, val):#поиск всех узлов
        a = []
        i = 1
        node = self.head
        while node is not None:
            if node.value == val:
                a.append(i)
                
            i += 1
            node = node.next
        return a[0]
    
    def insert_node(self, val_n, ins_n): #вставка после заданного узла
        n = Node(ins_n)
        node = self.head
        
        while node is not None:
            if node.value == val_n:
                z = node.next
                node.next = n
                n.prev = node
                n.next = z
                z.prev = n
                break
            else:
                node = node.next
    
s_list = LinkedList2()

import random

for i in range(20):
    
    x = Node(random.randint(1,9))
    s_list.add_in_tail(x)

s_list.print_all_nodes()
s_list.add_in_head(Node(99))
s_list.print_all_nodes()
s_list.remove_one(3)
s_list.print_all_nodes()
print(s_list.find(8))
s_list.insert_node(5, 100)
s_list.print_all_nodes()





