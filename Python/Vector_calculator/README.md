# vector_calculator
This is a 2 and 3 dimensionnal vector calculator script, can process vector comparison, addition, substraction, scalar product, cross product by modifying operator processing.

This script is an OOP project, made to facilitate vectors calculations. The script give the basis for 2 and 3 dimensions vectors calculations, but can easily be updated to perform calculation on more dimensions by adding new child class (similar to R3Vector class)

It works by modifying back processing of operator on this object, changing the initial behavior of *, +, -, >, >=, <, <=, == and != operators to directly apply them to the class instances.
