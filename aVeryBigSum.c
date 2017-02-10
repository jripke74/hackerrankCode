#include <stdio.h>

int main() {
  int N, i, n;
  long long sum = 0;

  scanf("%d", &N);
  long long nArray[N];
    
  for (i = 0; i < N; i++) {
    scanf("%lli", &nArray[i]);
  }
    
  for (n = 0; n < N; n++) {
    sum = sum + nArray[n];
  }
    
  printf("%lli", sum);
    
  return 0;
}

