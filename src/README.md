# Exercise 01 — Fundamentals of Programming in C

## Objectives
1. **Calculate the area of a square** given the length of its side.
2. **Calculate the volume of a cube** given the length of its side.

This exercise helps practice:
- Standard input and output in C (`scanf`, `printf`).
- Variables and arithmetic operations.
- Basic program organization.

---

## Instructions

1. Create a file named `main.c` in the exercise folder.
2. Write a C program that:
   - Asks the user for the length of the side (integer or decimal).
   - Calculates the area of the square:  
     \[
     \text{Area} = side \times side
     \]
   - Calculates the volume of the cube:  
     \[
     \text{Volume} = side \times side \times side
     \]
   - Prints both results to the screen.

---

## Example of Use

### Input
```
Enter the side length: 5
```

### Output
```
Square area: 25
Cube volume: 125
```

---

## Compilation and Execution

If you are inside the Docker container or VS Code DevContainer:

```bash
gcc main.c -o exercise01
./exercise01
```

---

## Simple Diagram

```
Square (2D)              Cube (3D)

+---------+              +---------+
|         |             /         /|
|         |            +---------+ |
|         |            |         | +
+---------+            |         |/
                       +---------+
```

---

## Reflective Questions

1. What happens if the user enters a decimal number instead of an integer?  
2. How should the program behave if the side length is negative?  
3. Why might `float` or `double` be more useful than `int` for this program?

---

## Author
- Jesús Salvador López Ortega [LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)
- Date: 01/05/2026