#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
  int n;
  scanf("%d", &n);
  int a[n][n];
  int diagonalLeftSum = 0;
  int digonalRightSum = 0;

  for(int a_i = 0; a_i < n; a_i++) {
    for(int a_j = 0; a_j < n; a_j++) {
      scanf("%d", &a[a_i][a_j]);
    }
  }
  for(int j = 0; j < n; j++) {
    for(int k = 0; k < n; k++) {
      if (j == k) {
	diagonalLiftSum += a[j][k];
      }
      if (j + k == n - 1) {
	diagonalRightSum += a[j][k];
      }
    }
  }
  int difference = abs(diagonalRightSum - diagonaleftSum);
  printf("%i", difference);
  return 0;
}
