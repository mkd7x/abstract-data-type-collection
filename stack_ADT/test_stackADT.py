from stackADT import Stack
import unittest

class StackADTTestCase(unittest.TestCase):
    
    def test_push_pop_operations(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        expectedOutput = [4,3,2,1]

        tmp_array = []

        while not stack.isEmptyStack():
            tmp_array.append(stack.pop())
        
        self.assertEqual(expectedOutput, tmp_array, "Output doesn't match expected output")

if __name__ == '__main__':
    unittest.main()