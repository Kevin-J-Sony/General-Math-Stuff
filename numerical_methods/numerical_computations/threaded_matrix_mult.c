#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

typedef struct {
	int** m;
	int row_size, col_size;
} matrix;


typedef struct {
	int** m1;
	int** m2;
	int** m3;
	int row;
	int col;
	int middle;
} arg_list;

void free_mat(matrix* m) {
	for (int i = 0; i < m->row_size; i++) {
		free(m->m[i]);
	}
	free(m->m);
	free(m);
}

// calculate ij element
// m1->col_size must be the same as m2->row_size
void* calc(void* args) {
	int** mat1 = ((arg_list*)args)->m1;
	int** mat2 = ((arg_list*)args)->m2;
	int** mat3 = ((arg_list*)args)->m3;
	int row = ((arg_list*)args)->row;
	int col = ((arg_list*)args)->col;
	int middle = ((arg_list*)args)->middle;
	mat3[row][col] = 0;
	for (int i = 0; i < middle; i++) {
		mat3[row][col] += mat1[row][i] + mat2[i][col];
	}
}

// take two matrices m1, m2, and return the result of these two multiplied
// if the matrices are not of correct size, output a statement and return
// the first matrix.
matrix* multiply(matrix* m1, matrix* m2) {

	if (m1->col_size != m2->row_size) {
		fprintf(stdout, "Dimensions do not match");
		return (matrix*)NULL;
	}
	int f_row_size = m1->row_size;
	int f_col_size = m2->col_size;
	int middle = m1->col_size;
	// int num_of_threads = m1->col_size;
	// pthread_t threads = (pthread_t*)

	int** mat1 = m1->m;
	int** mat2 = m2->m;
	int** mat3 = (int**)malloc(sizeof(int*) * f_row_size);

	for (int i = 0; i < f_row_size; i++) {
		mat3[i] = (int*)malloc(sizeof(int) * f_col_size);
	}

	pthread_t* threads = (pthread_t*)malloc(sizeof(pthread_t) * m1->row_size * m2->col_size);
	arg_list* list_of_args = (arg_list*)malloc(sizeof(arg_list) * m1->row_size * m2->col_size);
	for (int i = 0; i < f_row_size; i++) {
		for (int j = 0; j < f_col_size; j++) {
			list_of_args[i*f_row_size + j].m1 = mat1;
			list_of_args[i*f_row_size + j].m2 = mat2;
			list_of_args[i*f_row_size + j].m3 = mat3;
			list_of_args[i*f_row_size + j].row = i;
			list_of_args[i*f_row_size + j].col = j;
			list_of_args[i*f_row_size + j].middle = middle;
			
			pthread_create(&threads[i*f_row_size + j], NULL, &calc, &list_of_args[i*f_row_size + j]);
		}
	}

	for (int idx = 0; idx < f_row_size * f_col_size; idx++) {
		int val;
		pthread_join(threads[idx], (void**)val);
		if (val != 0) fprintf(stdout, "something went wrong when joining\n");
	}

	free(threads);
	free(list_of_args);

	matrix* m3 = (matrix*)malloc(sizeof(matrix));
	m3->m = mat3;
	m3->row_size = m1->row_size;
	m3->col_size = m2->col_size;

	return m3;
}

int get_value_of_matrix_at_ij(matrix* m, int i, int j) {
	return m->m[i][j];
}

int main() {
	
	int N[5] = {100, 100, 100, 100, 100};
	FILE *file_pointer = fopen("threaded_matrix_mult_data.txt", "w+");
	for (int s = 0; s < 5; s++) {
		// LOOP 10 TIMES TO GET CONSISTENT DATA
		double ms = 0;
		for (int t = 0; t < 10; t++) {
			matrix* m1 = (matrix*)malloc(sizeof(matrix));
			matrix* m2 = (matrix*)malloc(sizeof(matrix));
			m1->row_size = N[s], m1->col_size = N[s]+1;
			m2->row_size = N[s]+1, m2->col_size = N[s];

			int** matrix1 = (int**)malloc(sizeof(int*) * m1->row_size);
			for (int i = 0; i < m1->row_size; i++) {
				matrix1[i] = (int*)malloc(sizeof(int) * m1->col_size);
				for (int j = 0; j < m1->col_size; j++) {
					matrix1[i][j] = 1;
				}
			}

			int** matrix2 = (int**)malloc(sizeof(int*) * m2->row_size);
			for (int i = 0; i < m2->row_size; i++) {
				matrix2[i] = (int*)malloc(sizeof(int) * m2->col_size);
				for (int j = 0; j < m2->col_size; j++) {
					matrix2[i][j] = 1;
				}
			}
			m1->m = matrix1;
			m2->m = matrix2;
			
			
			clock_t start = clock();
			matrix* m3 = multiply(m1, m2);
			clock_t end = clock();
			ms += (end - start) * 1000 / CLOCKS_PER_SEC;
			//printf("time in milliseconds: %f\n", ms);
			
			int (*function)(matrix*, int, int);
			function = &get_value_of_matrix_at_ij;
			int sum = function(m3, 0, 0);
			fprintf(stdout, "value of m3 at (%i, %i): %i\n", 0, 0, sum);

			

			free_mat(m1);
			free_mat(m2);
			free_mat(m3);
		}
		// fprintf(file_pointer, "Average time to multiply (%d x %d) and (%d x %d) in milliseconds: %f\n", N[s], N[s]+1, N[s]+1, N[s], ms/10); 
	}
	fclose(file_pointer);
	
	return 0;
}
