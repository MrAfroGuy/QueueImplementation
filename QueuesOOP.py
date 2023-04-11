class Node: 
    '''stores a queue entry''' 

    def __init__(self, data): 

        self.data = data 

        self.next = None 

class Queue: 

    def __init__(self): 

        '''Set the rear and front pointers to None''' 

        self.front = self.rear = None 

         

    def isEmpty(self): 

        return self.front == None 

     

    def EnQueue(self,item): 

        '''add an item to the queue''' 

        new_Node =Node(item)

        ''' 

        1. assing a variable to  a node instance 

        2. if rear is empty then 

            set the front nad rear to the variable in 1 

           endif 

        3. set the variable in 1 as the next for the rear node 

        4. set the node in 1 as the rear 

         

        ''' 
        if self.rear is None:
            self.front = self.rear = new_Node
        self.rear.next = new_Node
        self.rear = new_Node
     

    def DeQueue(self): 

        '''removes an item from the queue''' 
        temp_Node = self.front
        self.front = temp_Node.next
        if self.front is None:
            self.rear = None

        return temp_Node.data

         

             

    def Peak(self): 

        '''returns item at the head''' 

        return self.front.data 

     

#Testing Code 

def main(): 

    #Testing Code 

    q = Queue() 

    q.EnQueue(10) 

    q.EnQueue(20) 

    q.DeQueue() 

    q.EnQueue(7) 

    q.EnQueue(25) 

    print("QUeue Front: ", str(q.Peak())) 

    print("Queue Rear: ", str(q.rear.data)) 

 