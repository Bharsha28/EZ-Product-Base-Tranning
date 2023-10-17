class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
        for i in range(1,11):
            new=Node(i)
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
            while temp:
                if temp.next==None:
                    print(temp.data)
                else:
                    print(temp.data,end=" -> ")
                temp=temp.next
    def delectafter_before(self,value):
        #incomplete
        temp=self.head.next
        prev=self.head
        if temp.data==value:
            print("before does not exit")
        else:
            temp=self.head.next
            while(temp.next.data!=value):
                temp=temp.next
                prev=prev.next
            prev.next=temp.next
            temp=temp.next
            temp.next=temp.next.next
    def insert_after(self,after_value,value):
        temp=self.head
        c=0
        while(temp.data!=after_value):
            temp=temp.next
            c+=1
        new=Node(value)
        new.next=temp.next
        temp.next=new
        if c==0:
            new=Node(value)
            temp.next=new
obj=singlell()
obj.display()
obj.delectafter_before(5)
obj.display()
obj.insert_after(8,100)
obj.display()

