#listModule.py
#This module is a part of the extraDataStructures repository
#Currently, this module contains classes for linked list nodes (classes linkedListNode and doublyLinkedListNode), a singly linked list (class linkedList), and a doublyLinkedList
#Written by: William Shultz
#Initial Upload: January 20, 2022
#Last Updated: January 21, 2022
"""
TO-DO:
        - Create class for Circular Linked List
"""
class linkedListNode:
    #class for individual node pieces. 
    #Each node containt a data value and a pointer to the next node (if it exists)
    #Currently houses no methods and is used only for the singly linked list
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        nextValue = self.next
        if type(nextValue) == type(None):
            nextValueString = 'None'
        else:
            nextValueString = nextValue.value
        return (f"value-{str(self.value)}".ljust(20) + f"next-{str(nextValueString)}".rjust(20))

class doublyLinkedListNode(linkedListNode):
    #a child class of the linkedListNode
    #This node only contains one additional attribute along with the standard linkedLisNode attributes: self.previous
    def __init__(self, value):
        super().__init__(value)
        self.previous = None
    
    def __str__(self) -> str:
        prevValue = self.previous
        if type(prevValue) == type(None):
            prevValueString = 'None'
        else:
            prevValueString = prevValue.value
        nextValue = self.next
        if type(nextValue) == type(None):
            nextValueString = 'None'
        else:
            nextValueString = nextValue.value
        return (f"value-{str(self.value)}".ljust(20)+f"previous-{str(prevValueString)}".center(20)+f"next-{str(nextValueString)}".rjust(20))

class linkedList:
    #class for a singly linked list (node)->(node)->(node)->None
    #CLASS ATTRIBUTES: head
    #SPECIAL METHODS: __init__(self,head=None)->None | __str__(self)->str
    #OTHER METHODS: prepend(self,nodeValue)->None | append(self,nodeValue)->None | insertAfter(self,nodeValue,targetNodeValue)->None | remove(self,targetNodeValue)->None

    def __init__(self, head=None) -> None:
        #creates a new singly linked list. If no head is given, it's an empty list, otherwise, it makes a list and assigns the head value to the given node
        self.head = head

    def __str__(self) -> str:
        #string returnable for the given linked list
        curNode = self.head
        if curNode == None:
            return "None"
        if curNode.next == None:
            return str(curNode.value)
        listOfValues = []
        while curNode != None:
            listOfValues.append(str(curNode.value))
            curNode = curNode.next
        return "->".join(listOfValues)

    def prepend(self, nodeValue) -> None:
        #Places a new node in front of the linked list head and makes that node the new head
        newNode = linkedListNode(nodeValue)
        newNode.next = self.head
        self.head = newNode

    def append(self, nodeValue) -> None:
        #goes to the end of the list and inserts a new node to that list
        if self.head == None:
            self.head = linkedListNode(nodeValue)
            return
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = linkedListNode(nodeValue)
        
    def insertAfter(self, nodeValue, targetNodeValue) -> None:
        #inserts a new node after the target node in a given linked list. Raises exceptions if list is empty or missing target node
        if self.head == None:
            raise Exception("Exception: This list is empty - can not find target.")
        curNode = self.head
        while curNode != None:
            if curNode.value == targetNodeValue:
                node = linkedListNode(nodeValue)
                node.next = curNode.next
                curNode.next = node
                return
            curNode = curNode.next
        raise Exception("Exception: Unable to find target node in given list.")

    def remove(self, targetNodeValue):
        #removes a node with value targetNodeValue from the linked List self
        if self.head == None:
            raise Exception("Exception: list is currently empty - unable to remove node.")
        if self.head.value == targetNodeValue:
            self.head = self.head.next
            return
        previousNode = self.head
        curNode = self.head
        while curNode != None:
            if curNode.value == targetNodeValue:
                previousNode.next = curNode.next
                curNode.next = None
                return
            previousNode = curNode
            curNode = curNode.next
        raise Exception("Exception: targetNode not found in linked list - unable to remove node.")

class doublyLinkedList(linkedList):
    def __init__(self, head=None) -> None:
        super().__init__(head=None)
        return
    def __str__(self) -> str:
        #string returnable for the given DLL
        curNode = self.head
        if curNode == None:
            return "None"
        if curNode.next == None:
            return str(curNode.value)
        listOfValues = []
        while curNode != None:
            listOfValues.append(str(curNode.value))
            curNode = curNode.next
        return "<->".join(listOfValues)

    def prepend(self, nodeValue) -> None:
        #Places a new node in front of the linked list head and makes that node the new head (links previous head to new head node as well)
        newNode = doublyLinkedListNode(nodeValue)
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
    
    def append(self, nodeValue) -> None:
        #goes to the end of the list and inserts a new node to that list (links the new node to the previous end node for DLLs)
        if self.head == None:
            self.head = doublyLinkedListNode(nodeValue)
            return
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        newNode = doublyLinkedListNode(nodeValue)
        curNode.next = newNode
        newNode.previous = curNode
    
    def insertAfter(self, nodeValue, targetNodeValue) -> None:
        #inserts a new node after the target node in a given linked list. Raises exceptions if list is empty or missing target node
        if self.head == None:
            raise Exception("Exception: This list is empty - can not find target.")
        curNode = self.head
        while curNode != None:
            if curNode.value == targetNodeValue:
                #create the new node
                newNode = doublyLinkedListNode(nodeValue)
                #the .next value of the new node = the curNode.next value
                newNode.next = curNode.next
                #the .previous value of the new node = the curNode value
                newNode.previous = curNode
                #the .previous of of the node after current node = the new node value
                nodeAfterCurNode = curNode.next
                nodeAfterCurNode.previous = newNode
                #the .next value of the curNode = new Node 
                curNode.next = newNode
                return
            curNode = curNode.next
        raise Exception("Exception: Unable to find target node in given list.")

    def remove(self, targetNodeValue):
        #removes a node with value targetNodeValue from the linked List self
        if self.head == None:
            raise Exception("Exception: list is currently empty - unable to remove node.")
        if self.head.value == targetNodeValue:
            self.head = self.head.next
            return        
        curNode = self.head
        while curNode != None:
            if curNode.value == targetNodeValue:
                #Removing the node ("alan") :           ("Janet") <--> ("alan") <--> ("Marge")
                #Janet.next will be Marge
                #Marge.previous will be Janet
                previousNode = curNode.previous
                afterNode = curNode.next
                previousNode.next = afterNode
                afterNode.previous = previousNode
                return
            previousNode = curNode
            curNode = curNode.next
        raise Exception("Exception: targetNode not found in linked list - unable to remove node.")

