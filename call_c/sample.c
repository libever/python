#include <stdio.h>  
#include <stdlib.h>  
#include <string.h>

int foo(int a, int b)  
{  
	printf("you input %d and %d\n", a, b);  
	return a+b;  
} 

char *reverse(char *s)  
{  
	register char t,                    /* tmp */  
			 *p = s,                     /* fwd */  
			 *q = (s + (strlen(s) - 1)); /* bwd */  

	while (p < q)               /* if p < q */  
	{  
		t = *p;         /* swap & move ptrs */  
		*p++ = *q;  
		*q-- = t;  
	}  
	return(s);  
}   
