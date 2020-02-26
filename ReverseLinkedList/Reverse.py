# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    #Input: 1->2->3->4->5->NULL
    #Output: 5->4->3->2->1->NULL
                                    
    #inoutput: null<-1<-2<-3<-4<-5
    prevNode = None
                                                                                                    
    while head is not None:                                                                                                                        
        curr = head                                                                                                           
        head = head.next
        curr.next = prevNode
        prevNode =   curr          
    return prevNode
