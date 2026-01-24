#include <stdio.h>

int is_even(int n)
{
	return (n % 2 == 0) ? 1 : 0;
}

int main(void)
{
	int n;
	printf("Ingrese un numero: ");
	if (scanf("%d", &n) != 1) {
		return 1;
	}

	if (is_even(n))
		printf("El numero es par\n");
	else
		printf("El numero es impar\n");

	return 0;
}
