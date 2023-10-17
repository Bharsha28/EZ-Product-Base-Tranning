class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
    def create(self):
        n=int(input("size"))
        for i in range(n):
            x=int(input())
            new=Node(x)
            if self.head is None:
                self.head=new
            else:
                temp=self.head
                while(temp.next!=None):
                    temp=temp.next
                temp.next=new
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                    print(temp.data,end="")
                    temp=temp.next

obj=singlell()
obj.create()
obj.display()