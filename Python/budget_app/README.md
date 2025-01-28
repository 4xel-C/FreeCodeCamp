# Budget Category Tracker

This project defines a `Category` class to manage budgeting and visualizes spending through a bar chart. Users can perform actions like depositing, withdrawing, transferring funds between categories, and generate a spending chart.

---

## Features

### Class: `Category`
The `Category` class manages individual budget categories. 

#### Attributes:
- `category`: The name of the category.
- `ledger`: A list tracking transactions as dictionaries (`amount` and `description`).
- `withdraws`: A cumulative sum of all withdrawals in the category.

#### Methods:
- `__init__(category)`: Initializes a budget category.
- `__str__()`: Returns a formatted string representation of the category ledger and balance.
- `deposit(amount, description="")`: Adds a deposit to the category ledger.
- `withdraw(amount, description="")`: Withdraws an amount if sufficient funds are available. Updates the withdrawal total.
- `transfer(amount, category)`: Transfers funds to another category.
- `get_balance()`: Calculates the current balance of the category.
- `check_funds(amount)`: Verifies if enough funds are available for a transaction.

### Function: `create_spend_chart(categories)`
Generates a bar chart showing the percentage of total withdrawals for each category.

---

## Code Explanation

### Key Concepts

#### Object-Oriented Programming (OOP)
- Classes and methods encapsulate functionality for each budget category.
- Instances of `Category` maintain separate ledgers.

#### Transaction Management
- Deposits and withdrawals update the ledger and the total balance.
- Transfers handle inter-category fund movements.

#### Visualization
- A bar chart represents spending as percentages across categories.

---

### Flow
1. Create categories with deposits and withdrawals.
2. Use `transfer()` to move funds between categories.
3. Call `create_spend_chart()` for a graphical summary.
