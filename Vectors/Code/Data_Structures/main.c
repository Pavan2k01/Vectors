#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "lib.h"

int main() {
    // Load coefficients and constants from l1.dat, l2.dat and l3.dat files
    double coefficients1[3];
    double coefficients2[3];
    double coefficients3[3];

    FILE* file1 = fopen("l1.dat", "r");
    FILE* file2 = fopen("l2.dat", "r");
    FILE* file3 = fopen("l3.dat", "r");

    if (file1 == NULL || file2 == NULL || file3 == NULL) {
        printf("Error: Could not open files.\n");
        return 1;
    }
    // Read coefficients for line 1
    for (int i = 0; i < 3; i++) {
        fscanf(file1, "%lf", &coefficients1[i]);
    }
    // Read coefficients for line 2
    for (int i = 0; i < 3; i++) {
        fscanf(file2, "%lf", &coefficients2[i]);
    }
    // Read coefficients for line 3
    for (int i = 0; i < 3; i++) {
        fscanf(file3, "%lf", &coefficients3[i]);
    }

    fclose(file1);
    fclose(file2);
    fclose(file3);
    // Create matrices for the two lines
    Node* line1 = assign(3, 1, coefficients1);
    Node* line2 = assign(3, 1, coefficients2);
    Node* line3 = assign(3, 1, coefficients3);

    find_intersection(line1, line2, line3);

    // Free the memory
    while (line1 != NULL) {
        Node* temp = line1;
        line1 = line1->next;
        free(temp);
    }
    while (line2 != NULL) {
        Node* temp = line2;
        line2 = line2->next;
        free(temp);
    }
    while (line3 != NULL) {
        Node* temp = line3;
        line3 = line3->next;
        free(temp);
    }

    return 0;
}



