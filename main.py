def reversed_list( values ) :


	############# DO NOT CHANGE ANYTHING BELOW #############
	initial_list = LinkedList()
	for value in values:
		initial_list.insert(value)
	reversed_list = initial_list.reverse_list()

	return reversed_list.as_list()
	############# DO NOT CHANGE ANYTHING ABOVE #############

class Node:
	def __init__(self, data):
		self.value = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, value):
		"""
		Append the value to the end of the Linked List.
		"""
		node = Node(value)
		if self.head == None:
			self.head = node
		else:
			next_node = self.head
			while next_node.next is not None:
				next_node = next_node.next
			next_node.next = node 

	def reverse_list(self):
		"""
		Reverse Linked List and return new reversed Linked List.
		"""
		reversed_list = LinkedList()
		currentNode = self.head
		prevNode = None
		nextNode = None


		while currentNode is not None:
			nextNode = currentNode.next
			currentNode.next = prevNode
			prevNode = currentNode
			currentNode = nextNode
		
		reversed_list.head = prevNode
		return reversed_list

		# if self.head == Node:
			
		# 	return None
		# return reversed_list

	def as_list(self):
		"""
		Convert Linked List to a list while preserving the order of the Linked List.
		"""
		linked_list_as_list = []
		next_node = self.head
		while next_node is not None:
			linked_list_as_list.append(next_node.value)
			next_node = next_node.next
		return linked_list_as_list



if __name__ == "__main__":
    print(reversed_list([1,4,7,8,1,5,6]))
