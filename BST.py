#!/usr/bin/python

class Node: 
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	def get(self):
		return self.val
	def set(self, val):
		self.val = val
	def isLeaf(self):
		return self.left is None and self.right is None
		
class BST: 
	### Simple implementation of Binary search Tree. 
	### may get unbalanced according to delete and/or insert sequence. 
	def __init__(self):
		self.root = None 
	def setRoot(self, val):
		self.root = Node(val)
	def insert(self, val):
		if self.contains(val):
			#Node already Exists
			return False 
		if self.root is None:
			self.setRoot(val)
		else:
			return self.insertNode(self.root, val)
		return True 
	def insertNode(self, node, val):
		# Assume Val does not exists
		if node.val < val:
			if node.right is None:
				node.right = Node(val)
			else:
				self.insertNode(node.right, val)
		else:
			if node.left is None:
				node.left = Node(val)
			else:
				self.insertNode(node.left, val)
	def contains(self, val):
		return self.containsNode(self.root, val)
	def containsNode(self, node, val):
		if node is None:
			return False 
		elif node.val == val:
			return True
		elif node.val > val:
			return self.containsNode(node.left, val)
		else:
			return self.containsNode(node.right, val)	
	def levelOrder(self):
		if self.root is None: 
			print "Tree is Empty!"
			return 
		self.print_LEVEL_Order([self.root])
		print "DONE"
	def print_LEVEL_Order(self, q):
		if len(q) == 0:
			return 
		node = q.pop();
		if node is None:
			return 
		print node.val,
		if node.left is not None:
			q.append(node.left)
		if node.right is not None:
			q.append(node.right)
		self.print_LEVEL_Order(q)
	def preOrder(self):
		if self.root is None:
			print "Tree is Empty!"
			return 
		self.print_PRE_Order(self.root)
		print "."
	def print_PRE_Order(self, node):
		if node is None:
			return 
		print node.val ,
		self.print_PRE_Order(node.left)
		self.print_PRE_Order(node.right)
	def postOrder(self):
		if self.root is None:
			print "Tree is Empty!"
			return 
		self.print_POST_Order(self.root)
		print "."
	def print_POST_Order(self, node):
		if node is None:
			return 
		self.print_POST_Order(node.left)
		self.print_POST_Order(node.right)
		print node.val,
	def print_IN_Order(self, node):	
		if node is None:
			return 
		self.print_IN_Order(node.left)
		print node.val, 
		self.print_IN_Order(node.right)
	def InOrder(self):
		if self.root is None:
			print "Tree is Empty!"
			return 
		self.print_IN_Order(self.root)
		print "."
	def getSmallest(self):
		if self.root is None:
			print "Tree is Empty"
			return -1 
		return self.findSmallest(self.root)
	def findSmallest(self, node):
		if node.left is None:
			return node.val
		return self.findSmallest(node.left)
	def getLargest(self):
		if self.root is None:
			print "Tree is Empty"
			return -1 
		return self.findLargest(self.root)
	def findLargest(self, node):
		if node.right is None:
			return node.val
		return self.findLargest(node.right)
	def isEmpty(self):
		return self.root is None
	def delete(self, val):
		if self.isEmpty():
			print "Tree is Empty"
			return False 
		tempRoot = Node(-1)
		tempRoot.left = self.root
		return self.deleteNode(tempRoot, self.root, val)
					 
	def deleteNode(self, parent, cur, val):
		if cur is None:
			return False   
		if cur.val < val:
			return self.deleteNode(cur, cur.right, val)
		elif cur.val > val:
			return self.deleteNode(cur, cur.left, val)		
		else:
			print "NODE IS FOUND"
			if cur.left is not None and cur.right is not None:
				newVal = self.findLargest(cur.left)
				cur.val = newVal
				self.deleteNode(cur, cur.left, newVal)
			elif parent.left is not None and parent.left.val == cur.val:
				if cur.left is not None:
					parent.left = cur.left
				else:
					parent.left = cur.right
			elif parent.left is not None and parent.right.val == cur.val:
				if cur.left is not None:
					parent.right = cur.left
				else:
					parent.right = cur.right
		return True
	def isValidTree(self, root):
		if root.isLeaf():
			return True
		if root.left is not None and root.val <= root.left.val:
			return False 
		
		
		
			
			
				
		
		
	