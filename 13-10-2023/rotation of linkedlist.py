class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
    def create(self):
        for i in range(1,11):
            new=Node(i)
            if self.head is None:
                self.head=new
            else:
                temp=self.head
                while(temp.next!=None):
                    temp=temp.next
                temp.next=new
    def rotate(self,k):
        temp=self.head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        length=c
        counter=length-k-1
        while counter!=0:
            temp=temp.next
            counter-=1
        temp_curr=temp
        temp=temp.next
        temp_curr.next=None
        while temp is not None:
            temp_curr=temp.next
            temp.next=self.head
            self.head=temp
            temp=temp_curr
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
        
obj=singlell()
obj.create()
obj.display()
k=int(input())
obj.rotate(k)
obj.display()