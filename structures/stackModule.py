import listModule as lm

#Implementing a stack using a singly linked list (WIP)
class Stack:
    #Initialization
    #creates a stack with a linked list node with value head
    #a size param keeps track of the number of nodes on the stack
    def __init__(self):
        self.head = lm.linkedListNode("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        returnable = ""
        while cur:
            returnable += str(cur.value) + " -> "
            cur = cur.next
            return returnable[:-3]
    
    #pushing a new node to the top of the stack
    def push(self, value):
        pushedNode= lm.linkedListNode(value)
        pushedNode.next = self.head.next
        self.head.next = pushedNode
        self.size +=1

    #popping the top node off a stack
    def pop(self):
        if (self.size == 0):
            raise Exception("Exception: can not pop node from an empty stack.")
        removedNode = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return removedNode.value

#testStack = Stack()
#for i in range (0,3):
#    testStack.push(i)
#    print(f"{testStack}")
#print("")
#testStack.pop()
#testStack.pop()
#print(f"{testStack}")
