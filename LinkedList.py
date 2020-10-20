class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        pass

    def append(self,pos):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = pos
        else:
            self.head = pos
        pass

    def insert(self,node,index):
        if self.head and index > 1:
            counter = 0
            current = self.head
            while current.next and counter < index:
                if counter == index - 1:
                    node.next = current.next
                    current.next = node
                    break
                counter =+ 1
        elif index == 1:
            node.next = self.head
            self.head = node 

    def delete(self,index):
         if self.head and index > 1:
            counter = 1
            current = self.head
            previous = None

            while current:
                
                if counter == index:
                    previous.next = current.next
                    break

                previous = current
                current = current.next
                counter += 1
         
         elif index == 1:
            self.head = self.head.next
        
    
    def print(self):
         
        if self.head:
            current = self.head
            while current:
                print(current.value," -> ",end="")
                current = current.next
            print("\n")
        else:
            print("No Node")

        pass

    


L = LinkedList()
    
while True:
    print("\nMENU\n  \t1)Append \t2)Insert \t3)Delete \t4)Print \t5)Exit\n")
    choice = int(input())

    if choice in range(1,3):
        print("Enter the Node : ",end="")
        e = Node(int(input()))

        if choice == 2:
            print("Enter the position at which Node is to be Inserted : ",end="")
            pos = int(input())
            L.insert(e,pos)
        elif choice == 1:
            L.append(e)
    
    elif choice == 3:
        print("Enter the position at which Node is to be deleted : ",end="")
        pos = int(input())
        L.delete(pos)
    
    elif choice == 4:
        L.print()
    
    else:
        break



