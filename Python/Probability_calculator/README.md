# Hat Drawing and Probability Experiment

## Overview
This program simulates an experiment to calculate the probability of drawing a specific combination of colored balls from a hat. It includes the `Hat` class for managing the contents of the hat and the `experiment` function to simulate multiple experiments.

---

## Code Explanation

### 1. Hat Class
#### **Initialization (`__init__`)**
- Takes keyword arguments where keys are ball colors and values are their counts.
- Creates a `contents` list where each color appears as many times as its count.

#### **Draw Method (`draw`)**
- Removes a specified number of balls from the `contents` list randomly.
- If the number of balls to draw exceeds the available balls, all balls are drawn.

### 2. Experiment Function
#### **Inputs**
- `hat`: An instance of the `Hat` class.
- `expected_balls`: A dictionary specifying the colors and quantities of balls to check for.
- `num_balls_drawn`: The number of balls to draw in each experiment.
- `num_experiments`: The total number of experiments to simulate.

#### **Process**
- Copies the hat to avoid altering the original during each experiment.
- Converts `expected_balls` into a flat list for comparison.
- Simulates drawing `num_balls_drawn` balls from the hat copy.
- Checks if all the `expected_balls` are present in the drawn balls.
- Increments the success count if the condition is met.

#### **Output**
- Returns the probability of success as a float.

## Execution

### Hat Object Creation
A `Hat` object is initialized with:
- 6 black balls
- 4 red balls
- 3 green balls

### Experiment Simulation
The `experiment` function simulates:
- **2000 experiments** in total.
- **5 balls** are drawn in each experiment.
- The goal is to draw **at least 2 red balls** and **1 green ball**.

### Output
The function calculates and returns the **probability of success** for the specified conditions.
