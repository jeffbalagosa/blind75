# Blind75 LeetCode Coding Challenges

Welcome to my repository for practicing the **Blind75 LeetCode Coding Challenges**. This repo is a personal project aimed at improving my problem-solving skills and preparing for technical interviews. Each problem is solved with a focus on clarity, efficiency, and comprehensive testing.

## Project Structure

The repository is organized into folders based on problem categories. Each category contains subfolders for individual problems. Each problem folder includes the following files:

- **`instructions.md`**: Contains the problem description and requirements.
- **`problem.py`**: The Python implementation of the solution.
- **`solution.md`**: Explanation of the solution, including the approach and complexity analysis.
- **`test.py`**: Unit tests to validate the solution using `unittest`.

### Example Folder Structure
```plaintext
arrays_and_hashing
├── contains_duplicate
│   ├── instructions.md
│   ├── problem.py
│   ├── solution.md
│   └── test.py
├── product_of_array_except_self
│   ├── instructions.md
│   ├── problem.py
│   ├── solution.md
│   └── test.py
bit_manipulation
├── number_of_1_bits
│   ├── instructions.md
│   ├── problem.py
│   ├── solution.md
│   └── test.py
```

## Testing

Each problem is rigorously tested using Python's built-in `unittest` framework. Below is an example of a test for the **Product of Array Except Self** problem:

```python
import unittest
from problem import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_productExceptSelf(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_productExceptSelf_2(self):
        self.assertEqual(
            self.solution.productExceptSelf([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24]
        )

if __name__ == "__main__":
    unittest.main()
```

To run the tests, execute the following command:

```bash
python -m unittest discover -s <folder_name> -p "test.py"
```

## Categories Covered

The repository currently includes the following categories:

- **Arrays and Hashing**
- **Bit Manipulation**
- **Intervals**
- **Linked Lists**
- **Trees**
- **Two Pointers**

## Goals

- Master the **Blind75** problems by solving them step-by-step.
- Write clean and efficient code.
- Document and test every solution comprehensively.
- Enhance understanding of algorithms and data structures.

## How to Use

Feel free to clone the repository and use it for your own learning. Contributions are welcome if you'd like to improve the solutions or add additional test cases.

```bash
git clone <repo_url>
cd blind75
```

## Notes

- This repository is a work in progress, and more problems will be added over time.
- For questions or feedback, feel free to reach out!
