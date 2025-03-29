# goit-algo2-hw-02
The repository for the 2nd GoItNeo Design and Analysis of Algorithms homework

### Task 1: Optimization of the 3D printer queue in a university laboratory
Utilize the input data as a list of printing tasks, including the following information in each task: ID, model volume, priority, and printing time.

#### Requirements:
Execute the optimize_printing function, which will:

- Consider the importance of each task.
- Models can be printed in groups.
- Verify the quantity and volume restrictions.
- Determine how long printing will take overall.
- Give back the best printing order.
- Print the ideal printing sequence and the total time needed to finish all the activities.

#### Results:
{'print_order': ['M1', 'M2', 'M3'], 'total_time': 270}

### Task 2: Finding the k-th Smallest Element
Create a software that determines the best method to cut a rod in order to maximize profit. Two strategies must be put into practice: tabulation and recursion with memoization.

#### Requirements:
- Price[i] is the price of the rod of length i+1, and the input is the array of prices and the rod's length.
- Finding the best way to cut the rod is essential to maximizing profits.
- Put both dynamic programming strategies into practice.
- Provide the best cutting strategy and the highest possible profit.

#### Results:
Testing rod length: 5, Prices: [2, 5, 7, 8, 10]
Memoization: (12, [1, 2, 2])
Tabulation: {'max_profit': 12, 'cuts': [1, 2, 2], 'number_of_cuts': 2}

Testing rod length: 3, Prices: [1, 3, 8]
Memoization: (8, [3])
Tabulation: {'max_profit': 8, 'cuts': [3], 'number_of_cuts': 0}

Testing rod length: 4, Prices: [3, 5, 6, 7]
Memoization: (12, [1, 1, 1, 1])
Tabulation: {'max_profit': 12, 'cuts': [1, 1, 1, 1], 'number_of_cuts': 3}


