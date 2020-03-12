

# 链表
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# def rev(link):
#     if link is None or link.next is None:
#         return link
#     pre = link
#     cur = link.next
#     pre.next = None
#     while cur:
#         temp = cur.next
#         cur.next = pre
#         pre = cur
#         cur = temp
#     return pre
#
#
# if __name__ == '__main__':
#     link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
#     print('===========================', link.next.data)
#     root = rev(link)
#     print('链表反转：', root)
#     while root:
#         print(root.data)
#         root = root.next


# def ReverseList(head):
#     # write code here
#     if not head or not head.next:
#         return head
#     print('开始运行递归内函数')
#     NewHead = ReverseList(head.next)
#     print('结束运行递归内函数')
#     print('head：', head.data)
#     head.next.next = head
#     head.next = None
#     print(NewHead.data, NewHead.next)
#     return NewHead
#
#
# head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
# res = ReverseList(head)


# 深浅拷贝
# from copy import copy, deepcopy
# a = [0, 1, [2, 3, 4]]
# b = copy(a)
# c = deepcopy(a)
# print('a改变前== b:', b, 'c:', c)
# a[2][1] = 5
# print('a改变后== b:', b, 'c:', c)


# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)


# 协程
# from greenlet import greenlet
#
#
# def test1():
#     print('已经切换到1')
#     print(12)
#     print('准备切换到2')
#     gr2.switch()
#     print('已经切换到1')
#     print(34)
#     print('准备切换到2')
#     gr2.switch()
#
#
# def test2():
#     print('已经切换到2')
#     print(56)
#     print('准备切换到1')
#     gr1.switch()
#     print('已经切换到2')
#     print(78)
#
#
# gr1 = greenlet(test1)  # 启动一个协程
# gr2 = greenlet(test2)
# gr1.switch()  # 手动切换


import gevent

from urllib import request
import gevent, time
from gevent import monkey

monkey.patch_all()  # 把当前程序的所有的io操作给我单独的做上标记


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
    page = open('url.html', 'wb')
    page.write(data)
    page.close()


urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/']
time_start = time.time()
for url in urls:
    f(url)
print("同步cost", time.time() - time_start)
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost", time.time() - async_time_start)


