class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        pass

    def push(self,pos):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = pos
        else:
            self.head = pos
        pass



    def pop(self):
        if self.head:
            previous = None
            current = self.head
            while current:
                if current.next == None:
                    previous.next = None
                    break
                
                previous = current
                current = current.next
        
    
    def print(self):
         
        if self.head:
            current = self.head
            while current:
                print(current.value," | ",end="")
                current = current.next
            print("\n")
        else:
            print("No Node")

        pass

    


S = LinkedList()
    
while True:
    print("\nMENU\n  \t1)Push \t2)Pop \t3)Print \t4)Exit\n")
    choice = int(input())

    if choice == 1:
        print("Enter the Node : ",end="")
        S.push(Node(int(input())))    
    
    elif choice == 2:
        S.pop()
    
    elif choice == 3:
        S.print()
    
    else:
        break



