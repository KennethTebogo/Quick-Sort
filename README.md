# Quick Sort Algorithm

This repository contains a Python implementation of the Quick Sort algorithm, which is a popular and efficient sorting algorithm based on the divide-and-conquer paradigm.

## Table of Contents
- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Quick Sort is a comparison-based sorting algorithm that works by dividing the array into smaller sub-arrays based on a pivot element. It then recursively sorts those sub-arrays and combines the results to return the final sorted array.

This implementation is simple and easy to understand, and it's a great starting point for learning how the algorithm works.

## How It Works
Quick Sort follows these steps:
1. **Pivot Selection**: A pivot element is chosen (in this case, the last element of the array).
2. **Partitioning**: The array is partitioned into two sub-arrays — one with elements smaller than the pivot, and the other with elements greater than the pivot.
3. **Recursion**: The same process is recursively applied to both sub-arrays.
4. **Combine**: The sorted sub-arrays and the pivot are combined to form the final sorted array.

## Installation
To use the quick sort implementation, you don't need to install anything special, just a Python environment.

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/kennethtebogo/quick-sort.git
    ```
2. Navigate to the project folder:
    ```bash
    cd quick-sort
    ```
3. Ensure you have Python 3.x installed by checking:
    ```bash
    python --version
    ```

## Usage

You can use the Quick Sort function by calling it in your Python script or interactive session.

```python
from quick_sort import quick_sort

arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
```

## Output
```
Sorted array: [1, 5, 7, 8, 9, 10]
```

## Contributing
If you would like to contribute to this project, feel free to submit a pull request! Please make sure to follow the repository's code style and write tests for new features or bug fixes.

Fork the repository.
-Create a new branch (git checkout -b feature-name).
-Commit your changes (git commit -am 'Add new feature').
-Push to the branch (git push origin feature-name).
-Create a pull request.
