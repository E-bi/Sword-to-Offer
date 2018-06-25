class ListNode:
    def __init__(self,data,_next=None):
        self.data =data
        self._next = _next
    def __repr__(self,data):
        return self.data
def findSame(ListNode1,ListNode2):
    head1 = ListNode1.head 
    head2 = ListNode2.head
    while head1 is not None & head2 is not None:
        if head1 == head2:
            return head1
        else:
            head1 = head1._next
            head2 = head2._next


