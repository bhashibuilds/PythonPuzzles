# Factorial 

def factorial(n):
    # Base case: n = 0 or 1
    # The base case is 0 or 1 because those are the final most simplest cases that can be used for recursive steps 
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)

# Reverse Linked List 
# Given the beginning of a singly linked list head, reverse the list and return the new beginning of the list 
# Definition for singly-linked list. Basically just reverse the list and give that list 

# If the initial linked list has 0-1-2-3-4 we are trying to switch it to 4-3-2-1-0 the starting head is 0
# But we will change the direction of it so that instead of pointing to 1, 0 will be pointing to null =, 1 will be pointing to 0, and 4 will 
# be pointing to 3 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
    
    # In the iterative answer for this question 
    # We have a singly linked list None -> 1 -> 2 -> 3 -> 4 -> 5 -> None 
    # If we are trying to reverse it then we must change each pointer and then go through the list and continue to change the pointers
    # The base case first of all is to see if we have a curr node and a curr.next node because if there are no values in the list then how can we have 
    # any iteration, and also if there is only 1 number in the singly linked list then also what can we iterate. 

    # The first thing we must do is make node 1 point to null, but if we make node 1 point to null we are losing connection to node 2 and we are abandoning everything
    # so before we make it point to node 2 we must store node 2 in a variable called next node so that it can hold those values 

    # First make a variable for next node
    # Then make the curr point to prev (null)

    # Now we successfully made 1 node reversed we have 1 <- 2, 3, -> 4, -> 5 at this point 
    # we now must make 3 point to 2 , 3 is currently pointing to 4 so we must do n_node = curr.next 
    # Before me make 3 point to 2 we must make 4 an individual node 
    # then we make 4 into a next node and we change the pointer to 3, we must remember that each digit only has 1 pointer to it, it is a singly linked list 
    # we must also move the prev node +1 each time we do the operation 

    def reverseListIteration(self, head):
        prev, curr = None, head # we have a prev node set to null and a curr node set to the input head we are given 

        while curr: # while we even have a current input , when it becomes None 
            next = curr.next # we set the next node and store it so it has a connection
            # we are making a next node because we are removing the pointer from 2 -3 to 2 -1 
            curr.next = prev
            prev = curr
            curr = next
        return prev # we return the prev node which is now head


