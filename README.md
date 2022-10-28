# TDT4136 (2022) - Assignment 4
Implement a general solver for Constraint Satisfaction Problems (CSP) using backtracking search
- pseudocode: Figure 6.5 (p. 382) from the book

Arc-consistency algorithm AC-3
- pseudocode: Figure 6.3 (p. 374) from the book

The pseudocode references three functions that have not been specified any further in the textbook, namely: 
- `SELECT-UNASSIGNED-VARIABLE`: return any unassigned variable
- `ORDERDOMAIN-VALUES`: any ordering for the given variable is fine
- `INFERENCE`: this is the arc consistency algorithm AC-3

### Resources
- Book: Stuart Russell, Peter Norvig - *Artificial Intelligence: A Modern Approach* (4th Edition) (Pearson Series in Artifical Intelligence) (2020)
<br>ISBN-13: 978-0134610993
- [John Levine: Constraint Satisfaction: the AC-3 algorithm](https://www.youtube.com/watch?v=4cCS8rrYT14)

## Project
In this assignment, you will implement a general solver for Constraint Satisfaction Problems using backtracking search and the arc-consistency algorithm AC-3. You will then use this program to solve Sudoku boards of varying difficulty. A sceleton code for te CSP is provided and it initialises and populates the necessary data structures to represent each CSP instance. 


### Sceleton code
Take a look at the provided code in _Assignment.py_. Create the CSP's by calling `create_sudoku_csp(filename)`. 

### **Important!**
To fully understand how a CSP can be represented, read Chapter 6.1 (Pay attention to the example in 6.1.1). Basically, it can be represented as a tuple, `(X, D, C)`;
- `X`: list of variable names
- `D`: dictionary that associates a variable name with its corresponding list of legal values
- `C`: dictionary that associates a variable name _i_ with another dictionary, where this second dictionary contains the constraints affecting variable _i_. Specifically, the second dictionary associates the name of another variable _j_ (given `i != j`) with an array of legal pairs of values for the pair of variables `(i, j)`.

#### Example: 
TBD

## Implementation
To pass this assignement, your program should solve the four Sudoku boards provided, and the results should be included in your report.

To show that you indeed implemented inference, include the number of times your __BACKTRACK__ function was called, and the number of times your __BACKTRACK__ function returned failure, for each of the four boards.
