#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int** m;
    int row_size, col_size;
} matrix;


void free_mat(matrix* m) {
    for (int i = 0; i < m->row_size; i++) {
        free(m->m[i]);
    }
    free(m->m);
    free(m);
}

// take two matrices m1, m2, and return the result of these two multiplied
// if the matrices are not of correct size, output a statement and return
// the first matrix.
matrix* multiply(matrix* m1, matrix* m2) {
    if (m1->col_size != m2->row_size) {
        fprintf(stdout, "Dimensions do not match");
        return (matrix*)NULL;
    }

    int** mat1 = m1->m;
    int** mat2 = m2->m;
    int** mat3 = (int**)malloc(sizeof(int*) * m1->row_size);

    for (int i = 0; i < m1->row_size; i++) {
        mat3[i] = (int*)malloc(sizeof(int) * m1->col_size);
    }

    
    for (int i = 0; i < m1->row_size; i++) {
        for (int j = 0; j < m2->col_size; j++) {
            mat3[i][j] = 0;
            for (int k = 0; k < m1->col_size; k++) {
                mat3[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }

    matrix* m3 = (matrix*)malloc(sizeof(matrix));
    m3->m = mat3;
    m3->row_size = m1->row_size;
    m3->col_size = m2->col_size;

    return m3;
}

int main() {
    int N = 100;
    matrix* m1 = (matrix*)malloc(sizeof(matrix));
    matrix* m2 = (matrix*)malloc(sizeof(matrix));
    m1->row_size = N, m1->col_size = N+1;
    m2->row_size = N+1, m2->col_size = N;

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
    
    matrix* m3 = multiply(m1, m2);

    /*
    for (int i = 0; i < m3->row_size; i++) {
        for (int j = 0; j < m3->col_size; j++) {
            fprintf(stdout, "%i ", m3->m[i][j]);
        }
        fprintf(stdout, "\n");
    }
    */

    free_mat(m1);
    free_mat(m2);
    free_mat(m3);
    
    return 0;
}