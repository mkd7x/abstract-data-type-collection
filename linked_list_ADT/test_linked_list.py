import unittest
from linkedList import ListNode

class LinkedListTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # Create 3 linked nodes
        self.node1 = ListNode(1)
        self.node2 = ListNode(2)
        self.node3 = ListNode(3)
        self.node4 = ListNode(4)
        self.node5 = ListNode(5)

        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node4
        self.node4.next = self.node5

    
    def test_two_nodes(self):
        currentNode = self.node1

        expectedNodeValue = 2

        currentNode = currentNode.next

        self.assertEqual(currentNode.val, expectedNodeValue, "Traversed to node2 and expect value: 2")
    
    def test_get_linked_list_length(self):
        linkedListLength = ListNode.listLength(self.node1)
        expectedListLength = 5

        self.assertEqual(linkedListLength, expectedListLength, "Expected list length of 5 got {linkedListLength}")
    
    def test_get_node_value(self):

        currentNode = self.node1
        
        node4Val = ListNode.getNodeValue(currentNode, 3)
        self.assertEqual(node4Val, 4, "Expected node value of 4 at position 3, got {node4Val}")

        node3Val = ListNode.getNodeValue(currentNode, 2)
        self.assertEqual(node3Val, 3, "Expected node value of 4 at position 2, got {node3Val}")

        node1Val = ListNode.getNodeValue(currentNode, 0)
        self.assertEqual(node1Val, 1, "Expected node value of 4 at position 0, got {node1Val}")

    def test_delete_node(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)

        node1.next = node2
        node2.next = node3

        ListNode.deleteNode(node1, 1)
        newLinkedListLength = ListNode.listLength(node1)

        self.assertEqual(newLinkedListLength, 2, "Deleted node at position 1, expected new linked list length of 2, got {newLinkedListLength}")
    
    def test_insert_node_beginning(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)

        node1.next = node2
        node2.next = node3

        # insert node 4 into position 1
        node4 = ListNode(4)

        ListNode.insertNode(node1, node4, 1)
        newLinkedListLength = ListNode.listLength(node1)

        self.assertEqual(newLinkedListLength, 4, "Expected linked list of length 4 after insertion, got {newLinkedListLength}")
        #self.assertEqual()

    def test_get_linked_list_values(self):
        
        expectedOutput = [1,2,3,4,5]
        actualOutput = ListNode.getLinkedListValues(self.node1)

        self.assertEqual(expectedOutput, actualOutput, "Expected linked list of {expectedOutput} got {actualOutput}")

    def test_create_linked_list_from_array(self):
        inputValues = [1,2,3,4]        
        newListHead = ListNode.createLinkedList(inputValues)

        listValuesOutput = ListNode.getLinkedListValues(newListHead)
        self.assertEqual(listValuesOutput, inputValues, "Input values: {inputValues}, New list values: {listValuesOutput}")

        listValuesLength = ListNode.listLength(newListHead)
        self.assertEqual(listValuesLength, 4, "Expected linked list length of 4, got {listValuesLength}")



if __name__ == '__main__':
    unittest.main()