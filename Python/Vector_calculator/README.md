## Vector Calculator Script

This Python script defines a vector calculator capable of performing various operations in 2D (\(R^2\)) and 3D (\(R^3\)) vector spaces. It includes operations such as vector addition, subtraction, scalar product, and cross product.

---

### Classes and Features

#### `R2Vector`
Represents a 2D vector with the following features:
- **Attributes**:
  - `x`: The x-component of the vector.
  - `y`: The y-component of the vector.

- **Methods**:
  - `norm`: Computes the Euclidean norm (\(\|v\|\)).
  - `__add__`: Adds two vectors.
  - `__sub__`: Subtracts two vectors.
  - `__mul__`: Computes scalar multiplication or dot product.
  - `__eq__`: Compares two vectors for equality.
  - `__lt__`, `__gt__`, `__le__`, `__ge__`: Compares vector norms.

#### `R3Vector`
Extends `R2Vector` to 3D with an additional component `z`:
- **Method**:
  - `cross`: Computes the cross product of two 3D vectors.

---

## Key Notes

- The script uses Python's special methods (e.g., __add__, __mul__) to enable operator overloading for seamless vector operations.
- The cross method is specific to 3D vectors and uses the standard formula for cross product computation.
- Type checks ensure that operations are performed only between compatible vector types.