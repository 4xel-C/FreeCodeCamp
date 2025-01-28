## Projectile Motion Simulation

### Overview
This Python program simulates the motion of a projectile considering initial speed, height, and launch angle. It calculates the projectile's trajectory, generates a table of coordinates, and displays a graph of the trajectory.

---

### Constants
- **Gravitational Acceleration**: 9.81
- **Projectile Marker**: `∙`
- **X-Axis Marker**: `T`
- **Y-Axis Marker**: `⊣`

---

### Classes

#### `Projectile`
Represents the projectile and performs trajectory calculations.

- **Attributes**:
  - `speed`: Initial speed (\(m/s\)).
  - `height`: Launch height (\(m\)).
  - `angle`: Launch angle (\(°\)).

- **Key Methods**:
  - `calculate_all_coordinates`: Returns a list of all (x, y) trajectory points.
  - `__calculate_displacement`: Computes the total horizontal displacement.
  - `__calculate_y_coordinate`: Calculates the vertical position \(y\) for a given \(x\).

---

#### `Graph`
Handles visualization of the projectile's trajectory.

- **Key Methods**:
  - `create_coordinates_table`: Outputs a table of all trajectory points.
  - `create_trajectory`: Constructs an ASCII graph of the trajectory.

---

### Simulation Details

The program initializes a projectile with:
- **Speed**: \(10 \, \text{m/s}\)
- **Height**: \(3 \, \text{m}\)
- **Angle**: \(45°\)

It calculates:
1. The trajectory coordinates.
2. The total displacement.
3. An ASCII graph of the trajectory.

---

