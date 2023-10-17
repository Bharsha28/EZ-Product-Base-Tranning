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
    def median(self):
        temp=self.head
        c=0
        while temp:
            c+=1
            temp=temp.next
        temp=self.head
        i=0
        if c%2!=0:
            c=c//2
            while (i<c):
                temp=temp.next
                i+=1
            print("\nmedian",temp.data)
        elif c%2==0:
             n=c//2
             m=n+1
             temp1=self.head
             while(i<n-1):
                 temp1=temp1.next
                 i+=1
             print("median:",temp1.data,temp1.next.data,end=" ")      
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
    def reverse(self):
        curr=self.head
        prev=None
        next1=None
        while(curr!=None):
            next1=curr.next
            curr.next=prev
            prev=curr
            curr=next1
        self.head=prev
        temp=self.head
        while temp.next!=None:
                print(temp.data,end=" -> ")
                temp=temp.next
        else:
            print(temp.data)

obj=singlell()
obj.create()
obj.display()
obj.median()
print()
obj.reverse()