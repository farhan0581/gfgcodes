# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html#fig-linkedlist

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None
		self.end = None

	def isempty(self):
		return self.head == None

	def add(self, value):
		node = Node(value)
		node.next = self.head
		self.head = node

	def printlist(self):
		while True:
			if self.head == None:
				break
			print self.head.data
			self.head = self.head.next
			



	def getEvenOdd(self):
		even = LinkedList()
		odd = LinkedList()
		while True:
			if self.head == None:
				break
			if self.head.data % 2 == 0:
				print self.head.data
				print '----------------'
				if even.head == None:
					even.head = self.head
					even.end = self.head
				else:
					even.end.next = self.head
					even.end = self.head


			elif self.head.data % 2 != 0:
				print self.head.data
				print '......................'
				if odd.head == None:
					odd.head = self.head
					odd.end = self.head
				else:
					odd.end.next = self.head
					odd.end = self.head

			self.head = self.head.next
		even.printlist()
		return even, odd



class Node(object):
	"""base node class , the building blocks of linked list"""
	def __init__(self, data):
		self.data = data
		self.next = None

	def setvalue(self, data):
		self.data = data

	def getvalue(self):
		return self.data

	def getnext(self):
		return self.next

	def setnext(self, next):
		self.next = next

mylist = LinkedList()
even = LinkedList()
odd = LinkedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
even, odd=mylist.getEvenOdd()
# even.printlist()
# odd.printlist()

		