#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
	int* m;
	int nrow, ncol;
} matrix;


void free_mat(matrix* m) {
	free(m->m);
	free(m);
}

// take two matrices m1, m2, and return the result of these two multiplied
// if the matrices are not of correct size, output a statement and return
// the first matrix.
matrix* multiply(matrix* m1, matrix* m2) {
	if (m1->ncol != m2->nrow) {
		fprintf(stdout, "Dimensions do not match");
		return (matrix*)NULL;
	}
	int f_nrow = m1->nrow;
	int f_ncol = m2->ncol;
	int middle = m1->ncol;

	int* mat1 = m1->m;
	int* mat2 = m2->m;
	int* mat3 = (int*)malloc(sizeof(int) * f_nrow * f_ncol);

	for (int i = 0; i < f_nrow; i++) {
		for (int j = 0; j < f_ncol; j++) {
			mat3[i * f_ncol + j] = 0;
			for (int k = 0; k < middle; k++) {
				mat3[i * f_ncol + j] += mat1[i * middle + k] * mat2[k * f_ncol + j];
			}
		}
	}

	matrix* m3 = (matrix*)malloc(sizeof(matrix));
	m3->m = mat3;
	m3->nrow = m1->nrow;
	m3->ncol = m2->ncol;
	return m3;
}

int main() {
	// int N[5] = {100, 200, 500, 1000, 1500};	
	int N[5] = {100, 200, 500, 500, 500};
	
	
	FILE *file_pointer = fopen("simple_matrix_mult_data.txt", "w+");
	for (int s = 0; s < 5; s++) {
		// LOOP 10 TIMES TO GET CONSISTENT DATA
		double ms = 0;
		for (int t = 0; t < 10; t++) {
			matrix* m1 = (matrix*)malloc(sizeof(matrix));
			matrix* m2 = (matrix*)malloc(sizeof(matrix));
			m1->nrow = N[s], m1->ncol = N[s]+1;
			m2->nrow = N[s]+1, m2->ncol = N[s];

			int* matrix1 = (int*)malloc(sizeof(int) * m1->nrow * m1->ncol);
			for (int i = 0; i < m1->nrow; i++) {
				for (int j = 0; j < m1->ncol; j++) {
					matrix1[i * m1->ncol + j] = 1;
				}
			}

			int* matrix2 = (int*)malloc(sizeof(int) * m2->nrow * m2->ncol);
			for (int i = 0; i < m2->nrow; i++) {
				for (int j = 0; j < m2->ncol; j++) {
					matrix2[i * m2->ncol + j] = 1;
				}
			}
			m1->m = matrix1;
			m2->m = matrix2;
			
			clock_t start = clock();
			matrix* m3 = multiply(m1, m2);
			clock_t end = clock();
			ms += (end - start) * 1000 / CLOCKS_PER_SEC;
			printf("time in milliseconds: %f\n", ms);

			/*
			for (int i = 0; i < m3->nrow; i++) {
				for (int j = 0; j < m3->ncol; j++) {
					fprintf(stdout, "%i ", m3->m[i][j]);
				}
				fprintf(stdout, "\n");
			}
			*/

			free_mat(m1);
			free_mat(m2);
			free_mat(m3);
		}
		fprintf(file_pointer, "Average time to multiply (%d x %d) and (%d x %d) in milliseconds: %f\n", N[s], N[s]+1, N[s]+1, N[s], ms); 
	}
	fclose(file_pointer);

	matrix* m1 = (matrix*)malloc(sizeof(matrix));
	matrix* m2 = (matrix*)malloc(sizeof(matrix));
	m1->nrow = 3, m1->ncol = 4;
	m2->nrow = 4, m2->ncol = 5;

	int* matrix1 = (int*)malloc(sizeof(int) * m1->nrow * m1->ncol);
	int idx = 1;
	for (int i = 0; i < m1->nrow; i++) {
		for (int j = 0; j < m1->ncol; j++) {
			matrix1[i * m1->ncol + j] = idx++;
		}
	}

	int* matrix2 = (int*)malloc(sizeof(int) * m2->nrow * m2->ncol);
	idx = 1;
	for (int i = 0; i < m2->nrow; i++) {
		for (int j = 0; j < m2->ncol; j++) {
			matrix2[i * m2->ncol + j] = idx++;
		}
	}
	m1->m = matrix1;
	m2->m = matrix2;
	matrix* m3 = multiply(m1, m2);

	for (int i = 0; i < m1->nrow; i++) {
		for (int j = 0; j < m1->ncol; j++) {
			fprintf(stdout, "%i ", m1->m[i * m1->ncol + j]);
		}
		fprintf(stdout, "\n");
	}
	fprintf(stdout, "\n-----------------------------------------\n");

	for (int i = 0; i < m2->nrow; i++) {
		for (int j = 0; j < m2->ncol; j++) {
			fprintf(stdout, "%i ", m2->m[i * m2->ncol + j]);
		}
		fprintf(stdout, "\n");
	}
	fprintf(stdout, "\n-----------------------------------------\n");

	for (int i = 0; i < m3->nrow; i++) {
		for (int j = 0; j < m3->ncol; j++) {
			fprintf(stdout, "%i ", m3->m[i * m3->ncol + j]);
		}
		fprintf(stdout, "\n");
	}
		

	free_mat(m1);
	free_mat(m2);
	free_mat(m3);
	
	return 0;
}
