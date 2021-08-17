from Queue import MyQueue
from Stack import MyStack
# from boiler_plate import *


class DepthFirstOrder:

    def __init__(self, digraph):
        self.marked = [False for _ in range(digraph.vertices)]
        self.pre = MyQueue()
        self.post = MyQueue()
        self.reverse_post = MyStack()

        for vertex in range(digraph.vertices):
            if not self.marked[vertex]:
                self.dfs(digraph, vertex)

    def dfs(self, digraph, vertex):
        if self.marked[vertex]:
            return
        self.pre.enqueue(vertex)
        self.marked[vertex] = True
        neighbours = digraph.adj(vertex)
        for neighbour in neighbours:
            if not self.marked[neighbour]:
                self.dfs(digraph, neighbour)
        self.post.enqueue(vertex)
        self.reverse_post.push(vertex)

    def preorder(self):
        return self.pre

    def postorder(self):
        return self.post

    def reverse_postorder(self):
        return self.reverse_post


# Code to test various orders
# obj = DepthFirstOrder(g)
# rev_order = obj.reverse_postorder().stack_list
# print(rev_order)
#
# pre = obj.preorder().queue_list
# print(pre)
#
# post = obj.postorder()
# print(post.queue_list)

