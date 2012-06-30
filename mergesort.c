#include <stdio.h>
#include <stdlib.h>

void merge(int A[], int p, int q, int r) {
  int i, j, k;
  int n1 = q - p;
  int n2 = r - q;

  int *L = malloc((n1 + 1)*sizeof(int));
  int *R = malloc((n2 + 1)*sizeof(int));

  for (i = 0; i < n1; i++)
    L[i] = A[p + i];

  for (i = 0; i < n2; i++)
    R[i] = A[q + i];

  L[n1] = 0xfffff;
  R[n2] = 0xfffff;
  i = 0; j = 0;
  for (k = p; k < r; k++) {
    if (L[i] <= R[j]) {
      A[k] = L[i];
      i++;
    } else {
      A[k] = R[j];
      j++;
    }
  }
}


void mergeSort(int A[], int p, int r) {
  if (p == r - 1)
    return;
  int q = (p + r) / 2;
  mergeSort(A, p, q);
  mergeSort(A, q, r);
  merge(A, p, q, r);
}
int main() {
  int A[6] = {4, 2, 3, 1, 6, 5}, i;

  mergeSort(A, 0, 6);

  for (i = 0; i < 6; i++)
    printf("%d\n", A[i]);
}
