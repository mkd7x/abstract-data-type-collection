
class ListNode():
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def createLinkedList(cls, inputArray: list):
        
        headNode = cls(inputArray[0])
        currentNode = headNode

        for index in range(1, len(inputArray)):
            currentNode.next = cls(inputArray[index])
            currentNode = currentNode.next
        
        return headNode


    
    @staticmethod
    def listLength(listHead) -> int:
        
        currentNode = listHead
        count = 0

        while (currentNode != None):
            count += 1
            currentNode = currentNode.next
        
        return count

    @staticmethod
    def insertNode(listHead, newNode, position):

        currentNode = listHead
        count = 0

        while(count != position):
            currentNode = currentNode.next
            count += 1
        
        newNode.next = currentNode.next
        currentNode.next = newNode

    @staticmethod
    def getNodeValue(listHead, position) -> int:
        
        currentNode = listHead
        count = 0

        while(count != position):
            currentNode = currentNode.next
            count += 1
        
        return currentNode.val

    @staticmethod
    def deleteNode(listHead, position):
        currentNode = listHead
        count = 0

        while(count < position):
            currentNode = currentNode.next
            count += 1
        
        prevPositionNode = currentNode
        currentNode = currentNode.next
        
        if currentNode.next == None:
            prevPositionNode.next = None
        else:
            prevPositionNode.next = currentNode.next
    
    @staticmethod
    def getLinkedListValues(listHead) -> list:

        currentNode = listHead
        nodeValues = []

        while (currentNode != None):
            nodeValues.append(currentNode.val)
            currentNode = currentNode.next
        
        return nodeValues
    