# Práctica: Determinar si un número es par

## Objetivo

Desarrollar un programa en lenguaje C que determine si un número entero ingresado por el usuario es par o impar, haciendo uso de una **función definida por el alumno**.

---

## Descripción del problema

Se debe crear un programa en C que lea un número entero desde la entrada estándar y determine si dicho número es **par**.

La lógica para determinar si el número es par **no debe estar en `main`**, sino en una función independiente.

---

## Especificaciones obligatorias

Tu programa **debe cumplir con todas** las siguientes especificaciones:

1. Debes declarar una función llamada `is_even`.
2. La función `is_even` debe devolver un valor de tipo `int`.
3. La función `is_even` debe recibir **un parámetro de tipo `int`**.
4. La función `is_even` debe devolver:

   * `1` si el número recibido es par
   * `0` si el número recibido **no** es par
5. Debes modificar la función `main` para que:

   * Invoque la función `is_even`
   * Lea el número ingresado por el usuario desde la entrada estándar

---

## Comportamiento esperado

Ejemplo de ejecución:

```text
Ingrese un numero: 6
El numero es par
```

```text
Ingrese un numero: 9
El numero es impar
```

---

## Archivos esperados

El proyecto debe contener:

```text
main.c
```

---

## Compilación y ejecución

El programa debe compilarse utilizando `gcc`.

```bash
gcc main.c
./a.out
```

---

## Criterios de evaluación

| Criterio                              | Porcentaje |
| ------------------------------------- | ---------- |
| Cumple con todas las especificaciones | 50 %       |
| Uso correcto de funciones             | 30 %       |
| Lectura correcta del dato de entrada  | 20 %       |

---

## Entregable

* Archivo fuente `main.c`
* El programa debe compilar sin errores
