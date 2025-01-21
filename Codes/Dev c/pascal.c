#include <stdio.h>

// A function to calculate the binomial coefficient
// nCk = n! / (k! * (n - k)!)
int binomialCoeff(int n, int k) {
    // Base cases
    if (k == 0 || k == n)
        return 1;
    // Recursive formula
    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k);
}

// A function to print the Pascal's Triangle
void printPascal(int rows) {
	int i,j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j <= i; j++)
            printf("%d ", binomialCoeff(i, j));
        printf("\n");
    }
}

// Driver code
int main() {
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    
    printPascal(rows);
    
    return 0;
}

