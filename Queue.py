class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        pass

    def Enqueue(self,pos):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = pos
        else:
            self.head = pos
        pass



    def Dequeue(self):

            self.head = self.head.next
        
    
    def print(self):
         
        if self.head:
            current = self.head
            while current:
                print(current.value," -- ",end="")
                current = current.next
            print("\n")
        else:
            print("No Node")

        pass

    


Q = LinkedList()
    
while True:
    print("\nMENU\n  \t1)Enqueue \t2)Dequeue \t3)Print \t4)Exit\n")
    choice = int(input())

    if choice == 1:
        print("Enter the Node : ",end="")
        Q.Enqueue(Node(int(input())))

    if choice == 2:
        Q.Dequeue()
    
    elif choice == 3:
        Q.print()

    elif choice == 4:
        break



