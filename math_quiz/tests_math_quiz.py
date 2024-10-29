import unittest
from math_quiz import createRandomNumber, chooseRandomOperation, performOperation


class TestMathGame(unittest.TestCase):

    def testCreateRandomNumber(self):
        # Test if random numbers generated are within the specified range.
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = createRandomNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Random number {rand_num} is out of bounds [{min_val}, {max_val}]")

    def testChooseRandomOperation(self):
        # Test if the chosen operation is one of the expected operations.
        operations = ['+', '-', '*']
        for _ in range(100):  # Test a large number of random selections
            op = chooseRandomOperation()
            self.assertIn(op, operations, f"Chosen operation {op} is not valid.")

    def testPerformOperation(self):
        # Test the performOperation function with various test cases.
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (2, 0, '+', '2 + 0', 2),
            (2, 0, '-', '2 - 0', 2),
            (2, 0, '*', '2 * 0', 0),
            (3, 4, '+', '3 + 4', 7),
            (3, 4, '-', '3 - 4', -1),
            (3, 4, '*', '3 * 4', 12)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, result = performOperation(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Expected problem '{expected_problem}', but got '{problem}'")
            self.assertEqual(result, expected_answer, f"Operation {num1} {operator} {num2} returned {result}, expected {expected_answer}")

if __name__ == "__main__":
    unittest.main()
