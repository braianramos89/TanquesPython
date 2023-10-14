# Tank Battle Simulator

This Python project simulates a tank battle scenario where two tanks engage in combat. The objective of the simulation is to determine the outcome of the battle, including which tank emerges as the victor.

## Tank Models

### M4 Sherman

- **Armor Thickness:** 51mm
- **Maximum Health Points:** 400
- **Ammunition Types:**
  - **Armor-Piercing (AP) Rounds:**
    - **Penetration:** 92mm
    - **Damage:** 110 points
  - **High-Explosive (HE) Rounds:**
    - **Penetration:** 38mm
    - **Damage:** 250 points

### PzV Panther

- **Armor Thickness:** 85mm
- **Maximum Health Points:** 500
- **Ammunition Types:**
  - **Armor-Piercing (AP) Rounds:**
    - **Penetration:** 135mm
    - **Damage:** 175 points
  - **High-Explosive (HE) Rounds:**
    - **Penetration:** 53mm
    - **Damage:** 350 points

### Future Additions

In the future, we plan to introduce new types of ammunition, specifically Armor-Piercing Discarding Sabot (APDS) rounds, which can penetrate even thicker armor. Additionally, a new tank, the PzVI Tiger, will be added to the simulation with the following characteristics:

- **Armor Thickness:** 100mm
- **Maximum Health Points:** 1100

## Combat Rules

- Each tank can carry any quantity of any ammunition type.
- When a tank fires, it randomly selects a type of ammunition (AP or HE).
- The ammunition penetrates the target tank's armor and inflicts damage based on the type.
- A tank is considered completely destroyed when its health points reach 0.

## How to Use

To use this simulation, you can implement the battle logic in your Python code. The tank classes and their ammunition attributes are provided, allowing you to simulate battles and evaluate the outcomes.

Here's a basic example of how to create and simulate a battle:

```python
from Tank import M4, PzV, Tiger

m4_sherman = M4()
pzv_panther = PzV()
tiger = Tiger()

print(m4_sherman.disparar(pzv_panther))
print(pzv_panther.disparar(m4_sherman))

print(tiger.disparar(m4_sherman))
print(m4_sherman.disparar(tiger))
print(pzv_panther.disparar(tiger))
