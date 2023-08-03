#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"lib.h"
int main()
{
	int m=3, n=1;
        double **l1, **l2, **l3;
        double **sol;
    l1 = loadtxt("l1.dat",m,n);
	l2 = loadtxt("l2.dat",m,n);
	l3 = loadtxt("l3.dat",m,n);
    sol = lin_solv(l1,l2,l3);

	print(sol,3,n);
	save(sol,3,n);
}
		
